import datetime as dt
import time
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components
import yaml

# Seiten-Konfiguration
st.set_page_config(page_title="U13/U14 Training", page_icon="🏐", layout="centered")

# Kompaktere Darstellung fürs Handy
st.markdown(
    """
    <style>
    .block-container {padding-top: 2.5rem; padding-bottom: 3rem;}
    h3 {font-size: 1.35rem !important;}
    h4 {font-size: 1.1rem !important;}
    /* Zurück/Weiter auch auf dem Handy nebeneinander */
    .st-key-nav [data-testid="stHorizontalBlock"] {flex-wrap: nowrap; gap: 0.5rem;}
    .st-key-nav [data-testid="stColumn"], .st-key-nav [data-testid="column"] {min-width: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

PLAN_DATEI = Path(__file__).with_name("trainingsplan.yaml")
SPIELER = {
    "9-12": "9-12 Spieler (Wellen-/Gruppenprinzip)",
    "6-8": "6-8 Spieler (Intensiv)",
}
ANSICHTEN = {"training": "⏱️ Training", "uebersicht": "📋 Übersicht"}


@st.cache_data
def lade_plan(geaendert):
    # "geaendert" sorgt dafür, dass Änderungen an der YAML-Datei sofort sichtbar werden
    return yaml.safe_load(PLAN_DATEI.read_text(encoding="utf-8"))["monate"]


plan = lade_plan(PLAN_DATEI.stat().st_mtime)
ss = st.session_state


# ---------------------------------------------------------
# Auswahl aus der Adresse (URL) übernehmen, damit Neuladen nichts zurücksetzt
# ---------------------------------------------------------
def aus_url(key, default):
    wert = st.query_params.get(key)
    if wert is None:
        return default
    try:
        return type(default)(wert)
    except ValueError:
        return default


def startzeit():
    try:
        return dt.time.fromisoformat(aus_url("start", "18:00"))
    except ValueError:
        return dt.time(18, 0)


# Fehlende Werte (erster Aufruf, oder Auswahlfeld war kurz ausgeblendet) aus der Adresse holen
for key, default in [
    ("m", lambda: aus_url("m", 0)),
    ("w", lambda: aus_url("w", 0)),
    ("e", lambda: aus_url("e", 0)),
    ("i", lambda: aus_url("i", 0)),
    ("t0", lambda: aus_url("t", 0)),  # Startzeitpunkt der aktuellen Übung (ms), 0 = Timer aus
    ("spieler", lambda: aus_url("sp", "9-12")),
    ("ansicht", lambda: aus_url("ansicht", "training")),
    ("start", startzeit),
]:
    if key not in ss:
        ss[key] = default()


def begrenzen(wert, anzahl):
    return wert if 0 <= wert < anzahl else 0


ss.m = begrenzen(ss.m, len(plan))
ss.w = begrenzen(ss.w, len(plan[ss.m]["wochen"]))
ss.e = begrenzen(ss.e, len(plan[ss.m]["wochen"][ss.w]["einheiten"]))
ss.i = begrenzen(ss.i, len(plan[ss.m]["wochen"][ss.w]["einheiten"][ss.e]["uebungen"]))
if ss.spieler not in SPIELER:
    ss.spieler = "9-12"
if ss.ansicht not in ANSICHTEN:
    ss.ansicht = "training"


def neue_einheit():
    ss.i = 0
    ss.t0 = 0


def neuer_monat():
    ss.w = 0
    ss.e = 0
    neue_einheit()


def neue_woche():
    ss.e = 0
    neue_einheit()


def gehe_zu(index, timer=True):
    ss.i = index
    ss.t0 = int(time.time() * 1000) if timer else 0


def oeffne_im_training(w, e):
    ss.w, ss.e = w, e
    neue_einheit()
    ss.ansicht = "training"


def einheit_name(einheit):
    tag = f" ({einheit['tag']})" if einheit.get("tag") else ""
    return f"{einheit['name']}{tag} · {einheit['dauer']} Min"


monat = plan[ss.m]
woche = monat["wochen"][ss.w]
einheit = woche["einheiten"][ss.e]
uebungen = einheit["uebungen"]

# ---------------------------------------------------------
# Kopf: kurzer Titel + aufklappbare Auswahl
# ---------------------------------------------------------
st.markdown("**🏐 U13/U14 Training · TuB Bocholt**")

kurz = monat["name"] if len(monat["wochen"]) == 1 else f"{monat['name']} · {woche['name']}"
with st.expander(f"📅 {kurz} · {einheit_name(einheit)}"):
    st.selectbox(
        "Monat",
        range(len(plan)),
        format_func=lambda m: f"{plan[m]['name']}: {plan[m]['thema']}",
        key="m",
        on_change=neuer_monat,
    )
    if len(monat["wochen"]) > 1:
        st.radio(
            "Woche",
            range(len(monat["wochen"])),
            format_func=lambda w: monat["wochen"][w]["name"],
            key="w",
            horizontal=True,
            on_change=neue_woche,
        )
    if len(woche["einheiten"]) > 1:
        st.radio(
            "Einheit",
            range(len(woche["einheiten"])),
            format_func=lambda e: einheit_name(woche["einheiten"][e]),
            key="e",
            horizontal=True,
            on_change=neue_einheit,
        )
    st.radio(
        "Anzahl anwesender Spieler",
        list(SPIELER),
        format_func=SPIELER.get,
        key="spieler",
        horizontal=True,
    )
    st.time_input("Trainingsbeginn", key="start", step=300)

st.radio(
    "Ansicht",
    list(ANSICHTEN),
    format_func=ANSICHTEN.get,
    key="ansicht",
    horizontal=True,
    label_visibility="collapsed",
)


def zeige_variante(uebung):
    variante = uebung.get("varianten", {}).get(ss.spieler)
    if variante:
        st.info(f"**Bei {SPIELER[ss.spieler]}:** {variante}")


def uebung_titel(uebung):
    titel = f"{uebung['icon']} {uebung['phase']} ({uebung['dauer']} Min)"
    if uebung.get("titel"):
        titel += f": {uebung['titel']}"
    return titel


def countdown(t0, minuten):
    # Läuft im Browser weiter, auch wenn die Verbindung kurz weg ist
    components.html(
        f"""
        <div id="cd" style="font-family: sans-serif; font-size: 2.6rem; font-weight: 700;
             text-align: center; font-variant-numeric: tabular-nums;"></div>
        <script>
        const t0 = {t0}, dauer = {minuten} * 60;
        const el = document.getElementById("cd");
        const dunkel = window.parent.matchMedia &&
            window.parent.matchMedia("(prefers-color-scheme: dark)").matches;
        function zeige() {{
            const rest = Math.round(dauer - (Date.now() - t0) / 1000);
            const s = Math.abs(rest);
            const txt = String(Math.floor(s / 60)).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0");
            el.textContent = rest >= 0 ? "⏱️ " + txt : "⏰ +" + txt;
            el.style.color = rest < 0 ? "#e5484d" : (rest < 60 ? "#f5a524" : (dunkel ? "#fafafa" : "#31333f"));
        }}
        zeige();
        setInterval(zeige, 1000);
        </script>
        """,
        height=70,
    )


# ---------------------------------------------------------
# Ansicht: Training (eine Übung nach der anderen)
# ---------------------------------------------------------
if ss.ansicht == "training":
    beginn = dt.datetime.combine(dt.date.today(), ss.start)
    zeiten = []
    for u in uebungen:
        ende = beginn + dt.timedelta(minutes=u["dauer"])
        zeiten.append((beginn.strftime("%H:%M"), ende.strftime("%H:%M")))
        beginn = ende

    u = uebungen[ss.i]
    st.progress((ss.i + 1) / len(uebungen), text=f"Übung {ss.i + 1} von {len(uebungen)} · {zeiten[ss.i][0]}–{zeiten[ss.i][1]}")
    st.markdown(f"### {u['icon']} {u['phase']} · {u['dauer']} Min")
    if u.get("titel"):
        st.markdown(f"**{u['titel']}**")

    if ss.t0:
        countdown(ss.t0, u["dauer"])
    else:
        st.button("▶️ Timer starten", on_click=gehe_zu, args=(ss.i,), use_container_width=True)

    with st.container(border=True):
        st.markdown(u["inhalt"])
        zeige_variante(u)

    with st.container(key="nav"):
        links, rechts = st.columns(2)
        links.button("◀ Zurück", on_click=gehe_zu, args=(ss.i - 1,), disabled=ss.i == 0, use_container_width=True)
        rechts.button(
            "Weiter ▶",
            on_click=gehe_zu,
            args=(ss.i + 1,),
            disabled=ss.i == len(uebungen) - 1,
            type="primary",
            use_container_width=True,
        )

    st.markdown(f"#### Ablauf: {einheit['titel']}")
    with st.container(key="ablauf"):
        for j, x in enumerate(uebungen):
            zeichen = "✅" if j < ss.i else ("▶️" if j == ss.i else "⬜")
            st.button(
                f"{zeichen} {zeiten[j][0]} · {x['phase']} ({x['dauer']}′)",
                key=f"springe_{j}",
                on_click=gehe_zu,
                args=(j,),
                type="primary" if j == ss.i else "secondary",
                use_container_width=True,
            )

# ---------------------------------------------------------
# Ansicht: Übersicht (zum Vorbereiten)
# ---------------------------------------------------------
else:
    st.markdown(f"### {monat['name']}: {monat['titel']}")
    reiter = st.tabs([w["name"] for w in monat["wochen"]]) if len(monat["wochen"]) > 1 else [st.container()]
    for w_index, (tab, w) in enumerate(zip(reiter, monat["wochen"])):
        with tab:
            for e_index, e in enumerate(w["einheiten"]):
                st.markdown(f"#### {einheit_name(e)}: {e['titel']}")
                for x in e["uebungen"]:
                    with st.expander(uebung_titel(x)):
                        st.markdown(x["inhalt"])
                        zeige_variante(x)
                st.button(
                    "⏱️ Im Training öffnen",
                    key=f"oeffne_{w_index}_{e_index}",
                    on_click=oeffne_im_training,
                    args=(w_index, e_index),
                )
                st.divider()

# Auswahl in die Adresse schreiben (Lesezeichen / Neuladen)
st.query_params.from_dict(
    {
        "m": ss.m,
        "w": ss.w,
        "e": ss.e,
        "i": ss.i,
        "t": ss.t0,
        "sp": ss.spieler,
        "start": ss.start.strftime("%H:%M"),
        "ansicht": ss.ansicht,
    }
)
