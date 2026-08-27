import streamlit as st

# Seiten-Konfiguration
st.set_page_config(page_title="U13/U14 Trainingsplan", page_icon="🏐", layout="centered")

st.title("🏐 U13 & U14 PRO Trainingsplan")
st.markdown("Kombi-Training TuB Bocholt (1 Feld, 3v3 und 4v4 kombiniert).")

# Navigation
monat = st.selectbox(
    "Wähle den Trainingsbereich:", 
    [
        "Monat 1: Tempo & Aufschlag von oben", 
        "Monat 2: Angriff & Sicherung", 
        "Monat 3: Out-of-System & Match-Speed",
        "System-Spezial: 3v3 meets 4v4"
    ]
)

# ---------------------------------------------------------
# MONAT 1
# ---------------------------------------------------------
if monat == "Monat 1: Tempo & Aufschlag von oben":
    st.header("Monat 1: Schnelles System & Aufschlagdruck")
    
    tab1, tab2 = st.tabs(["TE 1 (Fokus Tempo)", "TE 2 (Fokus Aufschlag)"])
    
    with tab1:
        st.subheader("Trainingseinheit 1: Volley-Tempo")
        
        with st.expander("🏃‍♂️ 1. Warm-up: Kognitives Chaos (10 Min)"):
            st.markdown("""
            **Gemeinsames Warm-up (Alle Spieler):** 
            Paarweise am Netz (U13 und U14 gemischt). A pritscht Ball 1 zu B, B rollt Ball 2 über Boden zu A. Auf Pfiff: Ball liegen lassen, Sprint zur Grundlinie, Sidesteps zurück.
            """)
            
        with st.expander("🎯 2. Technik: Zuspiel im Sprung (30 Min)"):
            st.markdown("""
            **Gemeinsames Techniktraining:** 
            3er-Gruppen quer über das Feld. Trainer schlägt Dankebälle ein. Annahme baggert hart. Zuspieler *muss* springen und im Sprung pritschen.
            *Tipp:* Lass gezielt die U14-Spieler die Bälle auf die U13-Spieler schlagen, um die U13 an die Härte zu gewöhnen!
            """)
            
        with st.expander("🧠 3. Taktik: Mixed-System Wellenprinzip (30 Min)"):
            st.markdown("""
            **U13/U14-Split am Netz:** 
            Trainer steht auf der Kiste mittig. 
            * **Seite A (U14):** Baut sich im 4-gegen-4 (Rauten-System) auf. 
            * **Seite B (U13):** Baut sich im 3-gegen-3 (1:2 Läufer) auf. 
            Trainer schlägt abwechselnd ein. Sobald der Ball drüben ist, rücken auf beiden Seiten die wartenden Teams der jeweiligen Altersklasse nach.
            """)
            
        with st.expander("🏆 4. Abschlussspiel: Das 4-gegen-3 Handicap (20 Min)"):
            st.markdown("""
            **Wash-Game mit Überzahl:** 
            Seite A spielt zu viert (U14), Seite B spielt zu dritt (U13). 
            *U14-Regel:* Die U14 muss den Ball zwingend gesprungen angreifen (kein Lob), da sie in Überzahl ist.
            *U13-Regel:* Die U13 darf alle Lücken im 4er-Feld mit cleveren Lobs ausnutzen. 
            """)

    with tab2:
        st.subheader("Trainingseinheit 2: Der Tennis-Aufschlag")
        
        with st.expander("🏃‍♂️ 1. Warm-up: Aufschlag-Staffel (10 Min)"):
            st.markdown("**Gemeinsam:** Teams an der Grundlinie. Spieler sprintet zum Netz, nimmt Ball, simuliert den Anwurf für den Tennis-Aufschlag, fängt ihn wieder auf, rennt zurück. Staffel-Modus.")
            
        with st.expander("🎯 2. Technik: Aufschlag von oben (30 Min)"):
            st.markdown("**Gemeinsam:** 1. Gegen die Wand werfen und schlagen (Handgelenk!). 2. Aufschlag von der 3m-Linie über das Netz. U14 muss von der Grundlinie aufschlagen, U13 darf ab der 4,50m/6m-Linie aufschlagen.")
            
        with st.expander("🧠 3. Taktik: Serve & Pass Komplex (30 Min)"):
            st.markdown("**U13/U14-Split:** Team A (U14) schlägt von oben auf. Team B (U13) muss die harte Annahme kontrollieren, den Läufer anspielen und druckvoll zurückspielen. Nach 5 Aufschlägen Rollentausch.")
            
        with st.expander("🏆 4. Abschlussspiel: 4v4 Integration (20 Min)"):
            st.markdown("**Hochziehen der Jüngeren:** Es wird reines 4-gegen-4 gespielt. Die U13-Spieler werden in die U14-Teams integriert. Sie lernen das 4er-System (Raute) kennen. Das schult ihr Raumgefühl für das spätere 3v3 enorm!")

# ---------------------------------------------------------
# MONAT 2
# ---------------------------------------------------------
elif monat == "Monat 2: Angriff & Sicherung":
    st.header("Monat 2: Harter Angriff und Angriffs-Sicherung")
    
    tab1, tab2 = st.tabs(["TE 1 (Fokus Angriffshärte)", "TE 2 (Fokus Block/Abwehr)"])
    
    with tab1:
        st.subheader("Trainingseinheit 1: Der harte Schlag")
        
        with st.expander("🏃‍♂️ 1. Warm-up: Hechten & Block-Schatten (10 Min)"):
            st.markdown("**Gemeinsam:** Auf Pfiff: Blocksprung am Netz, landen, rückwärts ausweichen, auf den Bauch hechten, schnell aufstehen. U14 muss beim Blocksprung weiter über das Netz greifen.")
            
        with st.expander("🎯 2. Technik: Der Schlagangriff (30 Min)"):
            st.markdown("**Gemeinsam:** Spieler auf Pos IV. Trainer wirft Pass. 3er-Rhythmus, Absprung, Schlag. U14 bekommt den Pass weiter nach außen, U13 eher etwas zentraler für mehr Ballsicherheit.")
            
        with st.expander("🧠 3. Taktik: Die Angriffssicherung (30 Min)"):
            st.markdown("**U13/U14-Split:** Ein 4er-Team (U14) stellt einen starren Doppelblock auf dem Kasten. Die U13 greift im 3v3 an und schlägt absichtlich in den Doppelblock der Großen. Die U13 muss den Abpraller blitzschnell im 2er-Sicherungs-System hochkratzen.")
            
        with st.expander("🏆 4. Abschlussspiel: Angriffs-Bingo (20 Min)"):
            st.markdown("**Punkte nur bei Angriff:** Es spielen 4v4 Teams (gemischt aus U13/U14). Punkt zählt nur, wenn der letzte Ball gesprungen und geschlagen wurde. U13-Spieler dürfen als Zuspieler agieren, U14 als Angreifer.")

    with tab2:
        st.subheader("Trainingseinheit 2: Block & Lob")
        
        with st.expander("🏃‍♂️ 1. Warm-up: Block-Sidesteps (10 Min)"):
            st.markdown("**Gemeinsam:** Paare am Netz. A wirft den Ball seitlich am Netzrand entlang. B macht schnelle Sidesteps, springt und blockt den Ball im Sprung zurück zu A.")
            
        with st.expander("🎯 2. Technik: Der gezielte Lob / Tip (30 Min)"):
            st.markdown("**Gemeinsam:** Voll abspringen, Armzug in der Luft abstoppen und den Ball sanft tippen. Wichtig: Der Ball muss *hoch* über den Block getippt werden, nicht geworfen!")
            
        with st.expander("🧠 3. Taktik: Blocken (3v3 vs 4v4) (30 Min)"):
            st.markdown("**U13/U14-Split:** \n*   **U14:** Trainiert den echten Doppelblock gegen Angriffe des Trainers.\n*   **U13:** Trainiert daneben den 1er-Block mit V-Abwehr (die beiden anderen Spieler sichern die Ecken).")
            
        with st.expander("🏆 4. Abschlussspiel: Hit or Tip Handicap (20 Min)"):
            st.markdown("**4-gegen-3:** U14 (zu viert) gegen U13 (zu dritt). \n*Handicap:* Die U14 darf *nur* hart angreifen (keine Lobs), da sie 4 Spieler haben. Die U13 darf *nur* tippen/loben, um die Lücken der U14 zu finden.")

# ---------------------------------------------------------
# MONAT 3
# ---------------------------------------------------------
elif monat == "Monat 3: Out-of-System & Match-Speed":
    st.header("Monat 3: Lösungen unter Stress")
    
    tab1, tab2 = st.tabs(["TE 1 (Fokus Not-Zuspiel)", "TE 2 (Match-Day)"])
    
    with tab1:
        st.subheader("Trainingseinheit 1: Chaos-Management")
        
        with st.expander("🏃‍♂️ 1. Warm-up: Periphere Sicht (10 Min)"):
            st.markdown("**Gemeinsam:** Paarweises Baggern. A hält vor dem Ballkontakt 1, 2 oder 3 Finger hoch. B muss rufen, wie viele Finger es waren, *bevor* er den Ball spielt.")
            
        with st.expander("🎯 2. Technik: Out-of-System Zuspiel (30 Min)"):
            st.markdown("**Gemeinsam:** Trainer wirft tief ins Hinterfeld. Zuspieler muss den Ball im Bagger als extrem hohen Pass an die Antenne spielen. Schulterachse zeigt zum Ziel!")
            
        with st.expander("🧠 3. Taktik: Freeball-Kill (30 Min)"):
            st.markdown("**Mixed-Wellenprinzip:** Trainer schlägt leichten Dankeball ein. \n*   Welle 1 (U14): Hat exakt 3 Sekunden für Annahme, Pass und harten Angriff.\n*   Welle 2 (U13): Hat 4 Sekunden Zeit für den gleichen Aufbau.")
            
        with st.expander("🏆 4. Abschlussspiel: Profi-Kaiserplatz (20 Min)"):
            st.markdown("**Vollgas:** Kaiserplatz im Modus 4-gegen-4. Die U13 Spieler, die nicht in ein 4er-Team passen, agieren als ständige Aufschläger von außen für alle Teams und bringen so permanenten Druck.")

    with tab2:
        st.subheader("Trainingseinheit 2: Der perfekte Wettkampf")
        
        with st.expander("🏃‍♂️ 1. Warm-up: Profi-Einspielen (15 Min)"):
            st.markdown("**Die Pre-Game-Routine:** Einschlagen wie beim echten Spieltag. Erst paarweise, dann ans Netz. Angriffsreihen über Pos IV und II mit Block durch den Trainer.")
            
        with st.expander("🎯 2. Technik: Der Not-Aufschlag (15 Min)"):
            st.markdown("**Sicherer Ball unter Druck:** Wenn es 14:14 steht, darf kein Aufschlag verschlagen werden. Jeder Spieler muss 5 sichere Aufschläge (von unten oder leichter Float) fehlerfrei ins gegnerische Feld bringen.")
            
        with st.expander("🧠 3. Taktik: Wash-Drill extrem (30 Min)"):
            st.markdown("**Rallye aufrechterhalten:** U14 spielt gegen U13 (Überzahl-Abwehr). Der Trainer wirft sofort den nächsten Ball ein, wenn der erste tot ist. Wer gewinnt 3 Bälle in Folge (Triple-Wash)?")
            
        with st.expander("🏆 4. Abschlussspiel: TuB Bocholt Liga (30 Min)"):
            st.markdown("**Das große Finale:** Zwei separate kleine Finals, wenn möglich (Feld quer teilen für 2 kleine Felder). Falls nicht: Ein großes 4v4 Turnier, bei dem U13 und U14 gemischt werden. Die Älteren coachen die Jüngeren!")

# ---------------------------------------------------------
# SYSTEM-SPEZIAL
# ---------------------------------------------------------
elif monat == "System-Spezial: 3v3 meets 4v4":
    st.header("System-Spezial: Transition & Kognition")
    st.success("Tipp: Wenn U13 und U14 zusammen trainieren, lernen die Jüngeren extrem schnell von der Härte und Übersicht der Älteren.")
    
    with st.expander("⏱️ 1. Der Transition-Läufer (U13 & U14) (15 Min)"):
        st.markdown("""
        **Aus der Abwehr ins Zuspiel:** 
        Trainer schlägt auf den Zuspieler. Der Zuspieler wehrt ab, ein anderer übernimmt das Not-Zuspiel.
        *   **U13:** Der Läufer startet von hinten (Pos I).
        *   **U14:** Der Zuspieler (meist Pos II) lässt sich in die Abwehr fallen und wird vertreten.
        """)

    with st.expander("👀 2. Das Scanner-Zuspiel (20 Min)"):
        st.markdown("""
        **Zuspieler muss den Block lesen:** 
        Trainer auf Gegenseite hebt linke oder rechte Hand (simuliert Block). Zuspieler pritscht dorthin, wo die Hand *unten* ist. Die U14 Zuspieler müssen hierbei im Sprung zuspielen!
        """)

    with st.expander("🌪️ 3. Der Dauerläufer (20 Min)"):
        st.markdown("""
        **Physische Härte für den Spielmacher:** 
        *   **U13:** Sprint Pos I -> III -> Zuspiel IV. Zurück auf I. 10x am Stück.
        *   **U14:** Start auf Pos II. Block-Sprung -> Zurückziehen auf 3m-Linie -> Zuspiel aus der Bewegung auf IV. 10x am Stück.
        """)

    with st.expander("🏆 4. Spielform: Der Libero-Joker (20 Min)"):
        st.markdown("""
        **3v3 mit Abwehr-Chef:** 
        U13 Teams spielen 3v3. Ein U14 Spieler agiert als "Libero" auf der Grundlinie hinter dem Feld. Geht ein Ball der U13 zu weit nach hinten oder droht ins Aus zu fallen, darf der U14-Libero eingreifen und den Ball hoch ins Feld retten. Schult die U14 in der Feldabwehr und hält die Rallyes der U13 am Leben.
        """)
