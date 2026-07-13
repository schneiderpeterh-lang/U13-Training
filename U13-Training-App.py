import streamlit as st
import os

# Seiten-Konfiguration
st.set_page_config(page_title="U13 Trainingsplan", page_icon="🏐", layout="centered")

st.title("🏐 U13 Trainingsplan")
st.markdown("Übersicht für das 3-gegen-3 Läufersystem (Fokus: 1 Feld, hohe Intensität)")

# Navigation
monat = st.selectbox(
    "Wähle den Trainingsmonat:", 
    ["Monat 1: Grundlagen & Laufwege", "Monat 2: Systemfestigung", "Monat 3: Matchpraxis"]
)

# Hilfsfunktion für lokale Bilder
def load_local_image(filename):
    if os.path.exists(filename):
        return filename
    else:
        return f"https://dummyimage.com/600x300/ccc/000&text=Bild+{filename}+fehlt"

# ---------------------------------------------------------
# MONAT 1
# ---------------------------------------------------------
if monat == "Monat 1: Grundlagen & Laufwege":
    st.header("Monat 1: Zielgenauigkeit & Einführung")
    
    tab1, tab2 = st.tabs(["TE 1 (Fokus Technik)", "TE 2 (Fokus System)"])
    
    with tab1:
        st.subheader("Trainingseinheit 1")
        with st.expander("🏃‍♂️ 1. Warm-up & Athletik (10 Min)"):
            st.markdown("""
            **Linien-Fangen & Reaktions-Tic-Tac-Toe**
            * **Aufbau (1 Feld):** Beim Linien-Fangen wird das gesamte 9x9m-Feld inkl. Mittellinie genutzt. Für Tic-Tac-Toe baust du zwei 3x3-Felder (aus Reifen oder Klebeband) links und rechts vom Netz auf der Auslinie auf.
            * **Ablauf:** Die Teams starten von der jeweiligen Grundlinie. Da alle gleichzeitig aktiv sind, gibt es keine Wartezeiten.
            * **Coaching-Tipp:** Tiefe Grundhaltung beim Linienspiel einfordern.
            """)
            st.image(load_local_image("aufwaermen.jpg"), caption="Warm-Up: Linien-Fangen & Tic-Tac-Toe")
            
        with st.expander("🎯 2. Technik (30 Min)"):
            st.markdown("""
            **Insel-Challenge (Stationsbetrieb auf 1 Feld)**
            * **Aufbau:** Nutze das Feld quer! Spanne ein Zauberschnur/Gummiband längs über das Feld oder nutze das Netz intensiv. Teile das Team: Gruppe A wirft an, Gruppe B spielt über das Netz auf Matten, Gruppe C sammelt Bälle.
            * **Ablauf:** Fliegender Wechsel nach 2 Minuten. So sind alle 12 Kinder gleichzeitig eingebunden (Werfer, Spieler, Sammler).
            * **Coaching-Tipp:** Beinarbeit! Erst unter den Ball laufen, dann aus den Beinen spielen.
            """)
            st.image(load_local_image("technik_inseln.jpg"), caption="Technik: Gezieltes Pritschen/Baggern auf Matten")
            
        with st.expander("🧠 3. Taktik (30 Min)"):
            st.markdown("""
            **Der Einwerfer (Wellenprinzip)**
            * **Aufbau (1 Feld):** Trainer steht in der Mitte am Netz (auf einem Kasten). Beide Netzhälften werden besetzt (jeweils 3 Spieler auf dem Feld, die restlichen Spieler warten spielbereit direkt hinter der Grundlinie).
            * **Ablauf (Die Welle):** Trainer wirft im Wechsel auf Feld A und Feld B ein. Sobald ein 3er-Team den Ball über das Netz gespielt hat, rennen sie unten durchs Netz holen den Ball und das **nächste 3er-Team** sprintet sofort auf das freie Feld.
            * **Coaching-Tipp:** Timing! Läufer startet erst, wenn der Ball die Hand des Trainers verlässt.
            """)
            st.image(load_local_image("taktik_laeufer.jpg"), caption="Taktik: Das Läufersystem Laufweg-Erklärung")
            
        with st.expander("🏆 4. Abschlussspiel (20 Min)"):
            st.markdown("""
            **Kaiserplatz (King of the Court)**
            * **Aufbau (1 Feld):** Perfekt für ein Feld. 3 Spieler sind "Kaiser" (Seite A). Der Rest teilt sich in 3er-Teams auf der Seite B (Herausforderer) auf.
            * **Ablauf:** Trainer wirft den Ball bei den Herausforderern ein. Wer den Punkt macht, wechselt auf die Kaiser-Seite. Wer auf der Kaiserseite gewinnt, bekommt einen Punkt.
            * **Coaching-Tipp:** Kurze Ballwechsel! Trainer wirft sofort den nächsten Ball ein, sobald der Punkt vorbei ist. Das hält die Warteschlange kurz. Systempflicht einfordern!
            """)
            st.image(load_local_image("kaiserplatz.jpg"), caption="Abschlussspiel: Kaiserplatz Turnier-Setup")

    with tab2:
        st.subheader("Trainingseinheit 2")
        st.info("Wiederholung von TE 1. Tausche die Insel-Ziele gegen kleinere Markierungen aus.")

# ---------------------------------------------------------
# MONAT 2
# ---------------------------------------------------------
elif monat == "Monat 2: Systemfestigung":
    st.header("Monat 2: Präzision unter Druck")
    
    tab1, tab2 = st.tabs(["TE 1 (Fokus Präzision)", "TE 2 (Fokus Umschaltspiel)"])
    
    with tab1:
        st.subheader("Trainingseinheit 1")
        with st.expander("🏃‍♂️ 1. Warm-up & Athletik (10 Min)"):
            st.markdown("""
            **Spiegelbild am Netz (Ganzes Feld nutzen)**
            * **Aufbau:** Alle Spielerpaare verteilen sich entlang der kompletten Netzkante (und zur Not der 3-Meter-Linie, falls das Netz zu kurz ist).
            * **Ablauf:** Leader macht Sidesteps, Schatten folgt. Nach 60 Sekunden Wechsel. Alle sind gleichzeitig aktiv.
            """)
            
        with st.expander("🎯 2. Technik (30 Min)"):
            st.markdown("""
            **Bagger-Tennis im Endlos-Modus**
            * **Aufbau (1 Feld):** 3-gegen-3 auf dem regulären Feld. Die wartenden Spieler stehen auf Position 1 hinter dem Feld.
            * **Ablauf:** Sobald ein Team den Ball über das Netz spielt, wechselt der Spieler, der den Ball zuletzt berührt hat, sofort vom Feld und ein neuer Spieler von außen sprintet auf seine Position. Extrem dynamisch!
            """)
            
        with st.expander("🧠 3. Taktik (30 Min)"):
            st.markdown("""
            **System-Drill im Wellenprinzip**
            * **Aufbau:** Zwei 3er-Teams auf der Annahmeseite (Team A auf dem Feld, Team B dahinter). Die restlichen Spieler sind auf der anderen Seite zum Blocken/Abwehren und Bälle sammeln.
            * **Ablauf:** Trainer schlägt 3 Bälle ("Freeballs") scharf ein. Team A spielt das Läufersystem. Nach 3 Bällen sofortiger Wechsel mit Team B. Nach 5 Durchgängen wechseln Annahme und Abwehr die Seiten.
            """)
            
        with st.expander("🏆 4. Abschlussspiel (20 Min)"):
            st.markdown("""
            **Zusatzpunkt-Wash-Spiel**
            * **Aufbau:** Zwei feste 3er-Teams auf dem Feld, die anderen warten.
            * **Ablauf:** Um einen "großen" Punkt zu erzielen, muss ein Team 2 Ballwechsel am Stück (Wash) gewinnen. Verliert es den ersten, rückt sofort das nächste 3er-Team von außen rein. Das erzwingt Fokus und ständige Rotation auf dem einen Feld. Zusatzpunkt für sauberes Läufersystem bleibt bestehen.
            """)

    with tab2:
        st.subheader("Trainingseinheit 2")
        st.info("Wiederholung von TE 1. Erhöhe den Druck, indem der Trainer die Dankebälle schärfer wirft/schlägt.")

# ---------------------------------------------------------
# MONAT 3
# ---------------------------------------------------------
elif monat == "Monat 3: Matchpraxis":
    st.header("Monat 3: Spielintelligenz")
    
    tab1, tab2 = st.tabs(["TE 1 (Fokus Chaos & Lösung)", "TE 2 (Turniermodus)"])
    
    with tab1:
        st.subheader("Trainingseinheit 1")
        with st.expander("🏃‍♂️ 1. Warm-up & Athletik (10 Min)"):
            st.markdown("""
            **Ball-Klau**
            * **Aufbau (1 Feld):** Begrenze das Feld auf die beiden 3-Meter-Räume (sehr eng) für maximale Interaktion. 
            * **Ablauf:** Alle dribbeln ihren Ball und schlagen die Bälle der anderen weg. Wer seinen verliert, muss 3 Strecksprünge am Netz machen und darf wieder rein.
            """)
            
        with st.expander("🎯 2. Technik (30 Min)"):
            st.markdown("""
            **Schere-Stein-Papier-Sprint (Beide Hälften)**
            * **Aufbau:** Trainer und Co-Trainer (oder ein starker Spieler) stehen als "Bosse" auf den beiden 3-Meter-Linien. Die Spieler teilen sich auf beide Netzhälften auf.
            * **Ablauf:** Nach jedem Ball über das Netz sprinten die Spieler zur Seitenlinie, spielen SSP gegen den Wartenden. So ist auf 1 Feld Daueraction.
            """)
            
        with st.expander("🧠 3. Taktik (30 Min)"):
            st.markdown("""
            **Chaos-Aufbau (Butterfly-System)**
            * **Aufbau:** 1 Feld. Auf Seite A und Seite B steht jeweils ein 3er-Team. 
            * **Ablauf:** Team A schlägt auf Team B auf. Team B baut im System auf und greift an. Team A wehrt ab und baut selbst im System auf (Endlos-Rallye). Fällt der Ball runter, rücken auf beiden Seiten sofort die wartenden Teams von der Grundlinie nach.
            """)
            
        with st.expander("🏆 4. Abschlussspiel (20 Min)"):
            st.markdown("""
            **Bundesliga-Blitzturnier**
            * **Aufbau (1 Feld):** 3-bis 4 Teams.
            * **Ablauf:** Spiele auf Zeit (z.B. exakt 4 Minuten pro Spiel). Gewinner bleibt stehen, Verlierer geht raus. Da die Spiele sehr kurz sind, friert keiner am Rand ein und jedes Team bekommt auf dem einen Feld viel Spielzeit. Joker-Karten-Regel gilt!
            """)

    with tab2:
        st.subheader("Trainingseinheit 2")
        st.info("Reiner Turniermodus. Der Trainer greift nur noch bei groben Systemfehlern ein und agiert ansonsten als Schiedsrichter.")
