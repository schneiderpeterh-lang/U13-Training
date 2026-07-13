import streamlit as st

# Seiten-Konfiguration für mobile Ansicht optimieren
st.set_page_config(page_title="U13 Trainingsplan", page_icon="🏐", layout="centered")

st.title("🏐 U13 Trainingsplan")
st.markdown("Übersicht für das 3-gegen-3 Läufersystem")

# Navigation per Dropdown
monat = st.selectbox(
    "Wähle den Trainingsmonat:", 
    ["Monat 1: Grundlagen & Laufwege", "Monat 2: Systemfestigung", "Monat 3: Matchpraxis"]
)

# Inhalt für Monat 1
if monat == "Monat 1: Grundlagen & Laufwege":
    st.header("Monat 1: Zielgenauigkeit & Einführung")
    
    tab1, tab2 = st.tabs(["TE 1 (Fokus Technik)", "TE 2 (Fokus System)"])
    
    with tab1:
        st.subheader("Trainingseinheit 1")
        with st.expander("🏃‍♂️ 1. Warm-up & Athletik (20 Min)"):
            st.markdown("""
            * **Linien-Fangen:** Bewegung nur auf Linien. Wer gefangen ist: 5 Strecksprünge.
            * **Reaktions-Tic-Tac-Toe:** Sprints zum 3x3-Feld, Markierungshemden ablegen.
            """)
            
        with st.expander("🎯 2. Technik (30 Min)"):
            st.markdown("""
            * **Die Insel-Challenge:** Matten als Ziel auf der Gegenseite auslegen. Teams sammeln Punkte.
            * **Volleyball-Biathlon:** Gezieltes Pritschen in einen Basketballkorb/Reifen. Fehlversuch = Strafrunde.
            """)
            
        with st.expander("🧠 3. Taktik (30 Min)"):
            st.markdown("""
            * **Schattenlauf:** Ohne Ball. Auf Kommando sprintet Zuspieler ans Netz, Annahme öffnet sich.
            * **Der Einwerfer:** Trainer wirft Ball leicht ein. Läufer stellt, Annahme fängt und wirft.
            """)
            
        with st.expander("🏆 4. Abschlussspiel (20 Min)"):
            st.markdown("""
            * **Kaiserplatz (King of the Court):** 3v3. Läufersystem ist Pflicht. Fehler beim Einlaufen = Punktabzug.
            """)

    with tab2:
        st.subheader("Trainingseinheit 2")
        st.info("Hier kannst du die Übungen für den zweiten Trainingstag der Woche eintragen und variieren.")
        # Platzhalter für weitere Inhalte

# Inhalt für Monat 2
elif monat == "Monat 2: Systemfestigung":
    st.header("Monat 2: Präzision unter Druck")
    st.success("Hier folgt der Content für Monat 2 (Bagger-Tennis, Zonen-Bingo, Dankeball-Läufer).")

# Inhalt für Monat 3
elif monat == "Monat 3: Matchpraxis":
    st.header("Monat 3: Spielintelligenz")
    st.success("Hier folgt der Content für Monat 3 (Ball-Klau, Chaos-Aufbau, Bundesliga-Turnier).")
