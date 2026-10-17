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
WOCHENTAGE = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]


@st.cache_data
def lade_plan(geaendert):
    # "geaendert" sorgt dafür, dass Änderungen an der YAML-Datei sofort sichtbar werden
    return yaml.safe_load(PLAN_DATEI.read_text(encoding="utf-8"))


def berechne_termine(plan, kalender):
    # Datum jeder Einheit aus dem Abschnitt "kalender" der YAML-Datei: {(m, w, e): Datum}
    if not kalender:
        return {}
    tage = [WOCHENTAGE.index(t) for t in kalender.get("tage", ["Mittwoch", "Freitag"])]
    pausen = [(p["von"], p["bis"]) for p in kalender.get("pausen") or []]
    montag = kalender["start"]
    termine = {}
    for m in range(kalender.get("ab_monat", 1) - 1, len(plan)):
        for w, woche in enumerate(plan[m]["wochen"]):
            # Wochen überspringen, in denen ein Trainingstag in Ferien/Pausen fällt
            while any(von <= montag + dt.timedelta(days=t) <= bis for t in tage for von, bis in pausen):
                montag += dt.timedelta(days=7)
            for e in range(len(woche["einheiten"])):
                termine[(m, w, e)] = montag + dt.timedelta(days=tage[min(e, len(tage) - 1)])
            montag += dt.timedelta(days=7)
    return termine


daten = lade_plan(PLAN_DATEI.stat().st_mtime)
plan = daten["monate"]
termine = berechne_termine(plan, daten.get("kalender"))
# Nächste Einheit ab heute (oder None, wenn der Plan vorbei ist)
heute = next((k for k, d in sorted(termine.items(), key=lambda x: x[1]) if d >= dt.date.today()), None)
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
# Ohne Auswahl in der Adresse startet die App mit dem nächsten Training
ohne_auswahl = "m" not in st.query_params and heute is not None
for key, default in [
    ("m", lambda: heute[0] if ohne_auswahl else aus_url("m", 0)),
    ("w", lambda: heute[1] if ohne_auswahl else aus_url("w", 0)),
    ("e", lambda: heute[2] if ohne_auswahl else aus_url("e", 0)),
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


def oeffne_heute():
    ss.m, ss.w, ss.e = heute
    neue_einheit()
    ss.ansicht = "training"


def datum_text(datum):
    return f"{WOCHENTAGE[datum.weekday()][:2]} {datum:%d.%m.}"


def einheit_name(m, w, e):
    einheit = plan[m]["wochen"][w]["einheiten"][e]
    if (m, w, e) in termine:
        tag = f" · {datum_text(termine[(m, w, e)])}"
    else:
        tag = f" ({einheit['tag']})" if einheit.get("tag") else ""
    return f"{einheit['name']}{tag} · {einheit['dauer']} Min"


def zeige_schwerpunkt(einheit):
    # Beobachtungsschwerpunkt: eine Sache, auf die der Trainer in dieser Einheit achtet
    sp = einheit.get("schwerpunkt")
    if sp:
        with st.expander(f"👁️ Im Blick: {sp['kurz']}"):
            st.markdown(f"**Achte auf:** {sp['achte_auf']}\n\n**Sag dazu:** „{sp['sag_dazu']}“")
            st.caption("Heute nur dazu Rückmeldung geben, alles andere darf warten.")


monat = plan[ss.m]
woche = monat["wochen"][ss.w]
einheit = woche["einheiten"][ss.e]
uebungen = einheit["uebungen"]

# ---------------------------------------------------------
# Kopf: kurzer Titel + aufklappbare Auswahl
# ---------------------------------------------------------
st.markdown("**🏐 U13/U14 Training · TuB Bocholt**")

if heute is not None and heute != (ss.m, ss.w, ss.e):
    st.button(
        f"📅 Nächstes Training: {datum_text(termine[heute])} · {plan[heute[0]]['name']} · {plan[heute[0]]['wochen'][heute[1]]['einheiten'][heute[2]]['name']}",
        on_click=oeffne_heute,
        use_container_width=True,
    )

kurz = monat["name"] if len(monat["wochen"]) == 1 else f"{monat['name']} · {woche['name']}"
with st.expander(f"📅 {kurz} · {einheit_name(ss.m, ss.w, ss.e)}"):
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
            format_func=lambda e: einheit_name(ss.m, ss.w, e),
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


def datei_oder_link(pfad):
    pfad = str(pfad)
    return pfad if pfad.startswith(("http://", "https://")) else str(PLAN_DATEI.parent / pfad)


def zeige_medien(uebung):
    # Optionale Felder in der YAML-Datei: bild, video, link
    if uebung.get("bild"):
        bild = datei_oder_link(uebung["bild"])
        try:
            if bild.endswith(".svg") and not bild.startswith("http"):
                st.image(Path(bild).read_text(encoding="utf-8"), width="stretch")
            else:
                st.image(bild, width="stretch")
        except (OSError, ValueError):
            st.caption(f"Bild nicht gefunden: {uebung['bild']}")
    if uebung.get("video"):
        st.video(datei_oder_link(uebung["video"]))
    if uebung.get("link"):
        st.markdown(f"🔗 [Zur Quelle]({uebung['link']})")


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

    zeige_schwerpunkt(einheit)

    u = uebungen[ss.i]
    st.progress((ss.i + 1) / len(uebungen), text=f"Übung {ss.i + 1} von {len(uebungen)} · {zeiten[ss.i][0]}–{zeiten[ss.i][1]}")
    st.markdown(f"### {u['icon']} {u['phase']} · {u['dauer']} Min")
    if u.get("titel"):
        st.markdown(f"**{u['titel']}**")

    if ss.t0:
        countdown(ss.t0, u["dauer"])
    else:
        st.button("▶️ Timer starten", on_click=gehe_zu, args=(ss.i,), use_container_width=True)

    zeige_medien(u)

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
                st.markdown(f"#### {einheit_name(ss.m, w_index, e_index)}: {e['titel']}")
                zeige_schwerpunkt(e)
                for x in e["uebungen"]:
                    with st.expander(uebung_titel(x)):
                        zeige_medien(x)
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
