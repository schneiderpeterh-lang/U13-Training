import datetime as dt
import html
import time
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components
import yaml

# Seiten-Konfiguration
st.set_page_config(page_title="U13/U14 Training", page_icon="🏐", layout="centered")

PLAN_DATEI = Path(__file__).with_name("trainingsplan.yaml")
STIL = Path(__file__).with_name("stil")


@st.cache_data
def lade_stil(geaendert):
    # Design (Hallmark, Theme Wayfind): tokens.css + base.css + app.css, ohne die @import-Zeilen
    teile = [(STIL / name).read_text(encoding="utf-8") for name in ("tokens.css", "base.css", "app.css")]
    return "\n".join(z for z in "\n".join(teile).splitlines() if z.strip() and not z.startswith("@import"))


# st.markdown statt st.html: st.html lädt auf manchen iPhones nicht ("Importing a module script failed")
st.markdown(f"<style>{lade_stil(max(p.stat().st_mtime for p in STIL.glob('*.css')))}</style>", unsafe_allow_html=True)
TOKENS = (STIL / "tokens.css").read_text(encoding="utf-8")
SPIELER = {
    "9-12": "9-12 Spieler (Wellen-/Gruppenprinzip)",
    "6-8": "6-8 Spieler (Intensiv)",
}
ANSICHTEN = {"training": "Training", "uebersicht": "Übersicht"}
WOCHENTAGE = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]


@st.cache_data
def lade_plan(geaendert):
    # "geaendert" sorgt dafür, dass Änderungen an der YAML-Datei sofort sichtbar werden
    return yaml.safe_load(PLAN_DATEI.read_text(encoding="utf-8"))


def berechne_termine(plan, kalender):
    # Datum jeder Einheit aus dem Abschnitt "kalender" der YAML-Datei: {(m, w, e): Datum}
    termine = {}
    if kalender:
        termine = kalender_termine(plan, kalender)
    # Einheiten mit eigenem "datum" (z. B. Extra-Training) haben Vorrang
    for m, monat in enumerate(plan):
        for w, woche in enumerate(monat["wochen"]):
            for e, einheit in enumerate(woche["einheiten"]):
                if isinstance(einheit.get("datum"), dt.date):
                    termine[(m, w, e)] = einheit["datum"]
    return termine


def kalender_termine(plan, kalender):
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
        tag = f", {datum_text(termine[(m, w, e)])}"
    else:
        tag = f" ({einheit['tag']})" if einheit.get("tag") else ""
    return f"{einheit['name']}{tag}, {einheit['dauer']} Min"


def zeige_schwerpunkt(einheit):
    # Beobachtungsschwerpunkt: eine Sache, auf die der Trainer in dieser Einheit achtet
    sp = einheit.get("schwerpunkt")
    if sp:
        with st.expander(f"Im Blick: {sp['kurz']}"):
            st.markdown(f"**Achte auf:** {sp['achte_auf']}\n\n**Sag dazu:** „{sp['sag_dazu']}“")
            st.caption("Heute nur dazu Rückmeldung geben, alles andere darf warten.")


monat = plan[ss.m]
woche = monat["wochen"][ss.w]
einheit = woche["einheiten"][ss.e]
uebungen = einheit["uebungen"]

# ---------------------------------------------------------
# Kopf: kurzer Titel + aufklappbare Auswahl
# ---------------------------------------------------------
with st.container(key="kopf"):
    st.markdown('<p class="wortmarke">U13/U14 Training</p><p class="verein">TuB Bocholt, Volleyball</p>', unsafe_allow_html=True)

st.radio(
    "Ansicht",
    list(ANSICHTEN),
    format_func=ANSICHTEN.get,
    key="ansicht",
    horizontal=True,
    label_visibility="collapsed",
)

if heute is not None and heute != (ss.m, ss.w, ss.e):
    st.button(
        f"Zum nächsten Training: {datum_text(termine[heute])}, {plan[heute[0]]['name']}, {plan[heute[0]]['wochen'][heute[1]]['einheiten'][heute[2]]['name']}",
        on_click=oeffne_heute,
        use_container_width=True,
    )

kurz = monat["name"] if len(monat["wochen"]) == 1 else f"{monat['name']}, {woche['name']}"
with st.container(key="wahl"), st.expander(f"{kurz}, {einheit_name(ss.m, ss.w, ss.e)}"):
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


def zeige_variante(uebung, key):
    # Variante unter einer Linie im selben Feld, keine eigene Karte
    variante = uebung.get("varianten", {}).get(ss.spieler)
    if variante:
        with st.container(key=f"variante_{key}"):
            st.markdown(f"**Bei {SPIELER[ss.spieler]}:** {variante}")


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
        st.markdown(f"[Quelle öffnen]({uebung['link']})")


def uebung_titel(uebung):
    titel = f"{uebung['phase']} ({uebung['dauer']} Min)"
    if uebung.get("titel"):
        titel += f": {uebung['titel']}"
    return titel


def tafel(u, nummer, anzahl, von, bis, t0):
    # Die Anzeigetafel: Übung, Zeitfenster und Countdown auf einer Tinten-Platte.
    # Läuft im Browser weiter, auch wenn die Verbindung kurz weg ist.
    segmente = "".join(
        f'<li class="{"fertig" if j < nummer else ("jetzt" if j == nummer else "")}"></li>' for j in range(anzahl)
    )
    titel = html.escape(u.get("titel", ""))
    components.html(
        f"""
        <link href="https://fonts.googleapis.com/css2?family=Chivo+Mono:wght@400;500;800&display=swap" rel="stylesheet">
        <style>
        {TOKENS}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        html, body {{ overflow-x: clip; background: var(--color-paper); }}
        body {{ font-family: var(--font-body); font-variant-numeric: tabular-nums; color: var(--color-paper-3); }}
        .platte {{ height: 100vh; display: flex; flex-direction: column; gap: var(--space-sm);
                   padding: var(--space-md); background: var(--color-ink); border: var(--rule-bar) solid var(--color-ink); }}
        .kopf {{ display: flex; justify-content: space-between; gap: var(--space-sm); font-size: var(--text-sm); font-weight: 500; color: var(--color-rule); }}
        ol {{ list-style: none; display: grid; grid-template-columns: repeat({anzahl}, minmax(0, 1fr)); gap: var(--space-2xs); }}
        li {{ height: 6px; background: var(--color-ink-rule); }}
        li.fertig {{ background: var(--color-rule); }}
        li.jetzt {{ background: var(--color-accent-2); }}
        h2 {{ font-weight: 800; font-size: var(--text-3xl); letter-spacing: var(--tracking-display); line-height: 1;
              overflow-wrap: break-word; min-width: 0; }}
        .titel {{ font-size: var(--text-md); font-weight: 500; line-height: 1.35; color: var(--color-paper-2);
                  display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }}
        .uhr {{ margin-top: auto; display: flex; align-items: baseline; justify-content: space-between; gap: var(--space-sm);
                padding: var(--space-2xs) var(--space-xs); }}
        .uhr.knapp {{ background: var(--color-accent-2); color: var(--color-ink); }}
        .zahl {{ font-weight: 800; font-size: clamp(3rem, 16vw, 4.75rem); line-height: 1; letter-spacing: var(--tracking-display); color: var(--color-accent-2); }}
        .knapp .zahl {{ color: var(--color-ink); }}
        .status {{ font-size: var(--text-sm); font-weight: 500; text-align: right; }}
        .platte.fokus {{ outline: 2px solid var(--color-accent-2); outline-offset: -6px; }}
        </style>
        <div class="platte">
          <div class="kopf"><span>Übung {nummer + 1} von {anzahl}</span><span>{von} bis {bis}</span></div>
          <ol aria-hidden="true">{segmente}</ol>
          <h2>{html.escape(u["phase"])}, {u["dauer"]} Min</h2>
          <p class="titel">{titel}</p>
          <div class="uhr" id="uhr"><span class="zahl" id="cd">{u["dauer"]:02d}:00</span><span class="status" id="st">{"läuft" if t0 else "bereit"}</span></div>
        </div>
        <script>
        const t0 = {t0}, dauer = {u["dauer"]} * 60;
        const uhr = document.getElementById("uhr"), el = document.getElementById("cd"), st = document.getElementById("st");
        function zeige() {{
            const rest = Math.round(dauer - (Date.now() - t0) / 1000);
            const s = Math.abs(rest);
            const txt = String(Math.floor(s / 60)).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0");
            el.textContent = rest >= 0 ? txt : "+" + txt;
            st.textContent = rest < 0 ? "Zeit um" : (rest < 60 ? "letzte Minute" : "läuft");
            uhr.classList.toggle("knapp", rest < 60);
        }}
        if (t0) {{ zeige(); setInterval(zeige, 1000); }}
        // Die Tafel zeigt, wenn sie per Tastatur den Fokus hat
        const platte = document.querySelector(".platte");
        window.addEventListener("focus", () => platte.classList.add("fokus"));
        window.addEventListener("blur", () => platte.classList.remove("fokus"));
        </script>
        """,
        height=262,
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
    tafel(u, ss.i, len(uebungen), zeiten[ss.i][0], zeiten[ss.i][1], ss.t0)
    if not ss.t0:
        st.button("Timer starten", on_click=gehe_zu, args=(ss.i,), type="primary", use_container_width=True)

    zeige_medien(u)

    with st.container(key="inhalt"):
        st.markdown(u["inhalt"])
        zeige_variante(u, "training")

    with st.container(key="nav"):
        links, rechts = st.columns(2)
        links.button("Zurück", on_click=gehe_zu, args=(ss.i - 1,), disabled=ss.i == 0, use_container_width=True)
        rechts.button(
            "Weiter",
            on_click=gehe_zu,
            args=(ss.i + 1,),
            disabled=ss.i == len(uebungen) - 1,
            type="primary" if ss.t0 else "secondary",
            use_container_width=True,
        )

    st.markdown(f"### Ablauf: {einheit['titel']}")
    breite = max(len(x["phase"]) for x in uebungen)
    with st.container(key="ablauf"):
        for j, x in enumerate(uebungen):
            zustand = "fertig" if j < ss.i else ("jetzt" if j == ss.i else "offen")
            with st.container(key=f"zeile_{zustand}_{j}"):
                st.button(
                    f"{zeiten[j][0]}  {x['phase'].ljust(breite)}  {x['dauer']:>2} Min",
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
                for x_index, x in enumerate(e["uebungen"]):
                    with st.expander(uebung_titel(x)):
                        zeige_medien(x)
                        st.markdown(x["inhalt"])
                        zeige_variante(x, f"{w_index}_{e_index}_{x_index}")
                st.button(
                    "Im Training öffnen",
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
