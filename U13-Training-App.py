import streamlit as st

# Seiten-Konfiguration für mobile Ansicht optimieren
st.set_page_config(page_title="U13 Trainingsplan", page_icon="🏐", layout="centered")

st.title("🏐 U13 Trainingsplan")
st.markdown("Übersicht für das 3-gegen-3 Läufersystem (90 Min. Fokus)")

# Navigation per Dropdown
monat = st.selectbox(
    "Wähle den Trainingsmonat:", 
    ["Monat 1: Grundlagen & Laufwege", "Monat 2: Systemfestigung", "Monat 3: Matchpraxis"]
)

# ---------------------------------------------------------
# MONAT 1
# ---------------------------------------------------------
if monat == "Monat 1: Grundlagen & Laufwege":
    st.header("Monat 1: Zielgenauigkeit & Einführung")
    
    tab1, tab2 = st.tabs(["TE 1 (Fokus Technik)", "TE 2 (Fokus System)"])
    
    with tab1:
        st.subheader("Trainingseinheit 1")
        with st.expander("🏃‍♂️ 1. Warm-up & Athletik (10 Min)"):
            st.markdown("**Linien-Fangen & Reaktions-Tic-Tac-Toe**")
            st.code("""
Linienspiel:                 Tic-Tac-Toe:
+-----------------+          Start: X X X
|        |        |            | sprint
|--O-----|----O---|            v
|    x   |        |          [ ][ ][ ]
+-----------------+          [ ][O][ ]
O = Spieler, x = Fänger      [ ][ ][x]
            """, language="text")
            
        with st.expander("🎯 2. Technik (30 Min)"):
            st.markdown("**Insel-Challenge & Volleyball-Biathlon**")
            st.code("""
Insel-Challenge:
+-----------------+
|  [Matte]        | <-- Ziel
|        [Matte]  | 
|--------|--------| (Netz)
|   O    |    O   | <-- Pritschen/Baggern
+-----------------+
            """, language="text")
            
        with st.expander("🧠 3. Taktik (30 Min)"):
            st.markdown("**Schattenlauf & Einwerfer**")
            st.code("""
Läufersystem (Z von Pos 1):
+-----------------+
|                 |
|--------|--------| (Netz)
| A(4)   Z(3)   A(2)
|        ^        |
|        | sprint |
| Ann(5) Z(1)   Ann(6)
+-----------------+
            """, language="text")
            
        with st.expander("🏆 4. Abschlussspiel (20 Min)"):
            st.markdown("**Kaiserplatz (King of the Court)**")
            st.code("""
[Warteschlange] -> Team C
+-----------------+
|     Team A      | <-- Herausforderer
|--------|--------| (Netz)
|     Team B      | <-- Kaiser (Gewinner)
+-----------------+
            """, language="text")

    with tab2:
        st.subheader("Trainingseinheit 2")
        st.info("Wiederholung von TE 1 mit leichten Variationen bei den Zielen (z.B. kleinere Matten).")

# ---------------------------------------------------------
# MONAT 2
# ---------------------------------------------------------
elif monat == "Monat 2: Systemfestigung":
    st.header("Monat 2: Präzision unter Druck")
    
    tab1, tab2 = st.tabs(["TE 1 (Fokus Präzision)", "TE 2 (Fokus Umschaltspiel)"])
    
    with tab1:
        st.subheader("Trainingseinheit 1")
        with st.expander("🏃‍♂️ 1. Warm-up & Athletik (10 Min)"):
            st.markdown("**Spiegelbild am Netz**")
            st.code("""
(Schatten)   O <--> (Sidesteps)
-------------|------------- (Netz)
(Leader)     X <--> (Sidesteps)
            """, language="text")
            
        with st.expander("🎯 2. Technik (30 Min)"):
            st.markdown("**Bagger-Tennis & Zonen-Bingo**")
            st.code("""
Zonen-Bingo:
+-----------------+
| Z1 | Z2 | Z3 |  | <-- Zielzonen
| Z4 | Z5 | Z6 |  |
|--------|--------| (Netz)
|                 |
|        O        | <-- Zielen nach Karte
+-----------------+
            """, language="text")
            
        with st.expander("🧠 3. Taktik (30 Min)"):
            st.markdown("**Dankeball-Läufer & System-Drill**")
            st.code("""
Dankeball-Läufer:
+-----------------+
|   Trainer (T)   |
|---(Ball)---|----| (Netz)
| A4     Z     A2 |
|        ^        |
|   O    | sprint |
+-----------------+
            """, language="text")
            
        with st.expander("🏆 4. Abschlussspiel (20 Min)"):
            st.markdown("**Zusatzpunkt-Spiel**")
            st.code("""
Normale Punkte: 1 Punkt
Zusatzpunkt (+2):
Wenn der Ball über den 
eingelaufenen Zuspieler 
(Läufersystem) aufgebaut wurde!
            """, language="text")

    with tab2:
        st.subheader("Trainingseinheit 2")
        st.info("Wiederholung von TE 1. Tempo bei den Einwürfen durch den Trainer leicht erhöhen.")

# ---------------------------------------------------------
# MONAT 3
# ---------------------------------------------------------
elif monat == "Monat 3: Matchpraxis":
    st.header("Monat 3: Spielintelligenz")
    
    tab1, tab2 = st.tabs(["TE 1 (Fokus Chaos & Lösung)", "TE 2 (Turniermodus)"])
    
    with tab1:
        st.subheader("Trainingseinheit 1")
        with st.expander("🏃‍♂️ 1. Warm-up & Athletik (10 Min)"):
            st.markdown("**Ball-Klau**")
            st.code("""
+-----------------+
| O(b) --> X(b)   | (b) = eigener Ball
|  |              |
|  v              | Ziel: Ball der anderen
| Y(b) <-- Z(b)   | wegschlagen!
+-----------------+
            """, language="text")
            
        with st.expander("🎯 2. Technik (30 Min)"):
            st.markdown("**Boss-Level & Schere-Stein-Papier-Sprint**")
            st.code("""
Boss-Level:
+-----------------+
|      [Boss]     | <-- Trainer bewegt sich
|   X         X   | <-- Freie Räume anspielen!
|--------|--------| (Netz)
|    O       O    |
+-----------------+
            """, language="text")
            
        with st.expander("🧠 3. Taktik (30 Min)"):
            st.markdown("**Chaos-Aufbau & Der blinde Pass**")
            st.code("""
Der blinde Pass:
+-----------------+
|      (T)        |
|--------|--------| (Netz)
| A(4) (Z-Rücken) A(2)
|                 | 
|       O(Ann)    | 
+-----------------+
(Z dreht sich erst um, wenn Annahme berührt!)
            """, language="text")
            
        with st.expander("🏆 4. Abschlussspiel (20 Min)"):
            st.markdown("**Bundesliga-Turnier mit Level-Up**")
            st.code("""
+-----------------+
|   Team 'Löwen'  |
|--------|--------| 
|  Team 'Haie'    |
+-----------------+
Jedes Team hat 3 Joker-Karten. 
Einsatz vor Aufschlag: Nächster 
Punkt zählt doppelt (bei System)!
            """, language="text")

    with tab2:
        st.subheader("Trainingseinheit 2")
        st.info("Fokus liegt komplett auf dem Bundesliga-Turnier. Trainer pfeift strenger auf Technikfehler.")
