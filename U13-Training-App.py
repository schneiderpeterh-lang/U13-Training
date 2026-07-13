import streamlit as st

# Seiten-Konfiguration
st.set_page_config(page_title="U13 PRO Trainingsplan", page_icon="🏐", layout="centered")

st.title("🏐 U13 PRO Trainingsplan – TuB Bocholt")
st.markdown("Für fortgeschrittene Teams (Fokus: 1 Feld, High-Speed 1:2 System, kein Fangen).")

# Navigation
monat = st.selectbox(
    "Wähle den Trainingsbereich:", 
    [
        "Monat 1: Tempo & Aufschlag von oben", 
        "Monat 2: Angriff & Sicherung", 
        "Monat 3: Out-of-System & Match-Speed",
        "Läufer-Spezial: Transition & Kognition"
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
            st.markdown("**Zwei-Ball-Koordination:** Paarweise am Netz. A pritscht Ball 1 zu B, B rollt Ball 2 über Boden zu A. Auf Pfiff: Ball liegen lassen, Sprint zur Grundlinie, Sidesteps zurück.")
            
        with st.expander("🎯 2. Technik: Zuspiel im Sprung (30 Min)"):
            st.markdown("**Ziel-Pritschen in Reichhöhe:** 3er-Gruppen. Trainer schlägt Dankebälle ein. Annahme baggert hart zur Pos III. Zuspieler *muss* springen und den Ball im Sprung pritschen.")
            
        with st.expander("🧠 3. Taktik: High-Speed 1:2 System (30 Min)"):
            st.markdown("**Volley-System unter Druck:** 3v3 auf 1 Feld. Trainer bringt Ball hart ins Spiel. Sauberes System aufbauen. **Kein Fangen!** 3. Ball wird lang ge-lobt oder im Sprung gepritscht.")
            
        with st.expander("🏆 4. Abschlussspiel: Wash-Game mit Minuspunkt (20 Min)"):
            st.markdown("**Konsequenz:** 3v3 Wash-Game (2 Rallyes in Folge gewinnen = 1 Punkt). Zusatzregel: Wer den Ball direkt beim 1. Kontakt rüberspielt, kassiert einen Minuspunkt.")

    with tab2:
        st.subheader("Trainingseinheit 2: Der Tennis-Aufschlag")
        
        with st.expander("🏃‍♂️ 1. Warm-up: Aufschlag-Staffel (10 Min)"):
            st.markdown("**Schnelligkeit & Wurf:** Teams an der Grundlinie. Spieler sprintet zum Netz, nimmt Ball, simuliert den Anwurf für den Tennis-Aufschlag, fängt ihn wieder auf, rennt zurück. Staffel-Modus.")
            
        with st.expander("🎯 2. Technik: Aufschlag von oben (30 Min)"):
            st.markdown("**Der harte Hit:** 1. Gegen die Wand werfen und schlagen (Fokus auf Handgelenk-Klappung). 2. Auf dem Feld: Aufschlag von der 3m-Linie über das Netz. Wenn 3 am Stück klappen, einen Meter zurückgehen.")
            
        with st.expander("🧠 3. Taktik: Serve & Pass Komplex (30 Min)"):
            st.markdown("**Aufschlag vs. System:** Team A schlägt von oben auf. Team B muss die harte Annahme kontrollieren, den Läufer auf Pos III anspielen und den Ball druckvoll zurückspielen. Rotation nach 5 Aufschlägen.")
            
        with st.expander("🏆 4. Abschlussspiel: Aufschlag-König (20 Min)"):
            st.markdown("**Belohnung für Asse:** 3v3 Kaiserplatz. Aber: Wenn das Herausforderer-Team durch ein direktes Aufschlag-Ass punktet, darf es *sofort* auf die Kaiser-Seite wechseln. Ein normaler Punkt gibt nur das Recht, weiter aufzuschlagen.")

# ---------------------------------------------------------
# MONAT 2
# ---------------------------------------------------------
elif monat == "Monat 2: Angriff & Sicherung":
    st.header("Monat 2: Harter Angriff und Angriffs-Sicherung")
    
    tab1, tab2 = st.tabs(["TE 1 (Fokus Angriffshärte)", "TE 2 (Fokus Clevere Lösungen)"])
    
    with tab1:
        st.subheader("Trainingseinheit 1: Der harte Schlag")
        
        with st.expander("🏃‍♂️ 1. Warm-up: Hechten & Block-Schatten (10 Min)"):
            st.markdown("**Abwehr-Dynamik:** Auf Pfiff: Blocksprung am Netz, landen, rückwärts ausweichen, auf den Bauch hechten (Defense-Sprawl), schnell wieder aufstehen.")
            
        with st.expander("🎯 2. Technik: Der Schlagangriff (30 Min)"):
            st.markdown("**Armzug & Handgelenk:** Spieler auf Pos IV. Trainer wirft perfekten Pass. 3er-Rhythmus (Links-Rechts-Links), Absprung, Schlag. Vor dem Sprung Arme nach hinten reißen!")
            
        with st.expander("🧠 3. Taktik: Die Angriffssicherung (30 Min)"):
            st.markdown("**Wer deckt den Angreifer?** 3v3. Auf Seite B stehen 2 Spieler auf einem Kasten als Doppelblock. Angreifer schlägt absichtlich in den Block. Zuspieler und Annahme müssen den Abpraller hochkratzen.")
            
        with st.expander("🏆 4. Abschlussspiel: Angriffs-Bingo (20 Min)"):
            st.markdown("**Punkte nur bei Angriff:** 3v3 Turnier. Ein Punkt zählt nur, wenn der letzte Ball gesprungen und geschlagen (oder aggressiv ge-lobt) wurde. Im Stand gepritschte Bälle geben keine Punkte.")

    with tab2:
        st.subheader("Trainingseinheit 2: Block & Lob")
        
        with st.expander("🏃‍♂️ 1. Warm-up: Block-Sidesteps (10 Min)"):
            st.markdown("**Schnelle Beine am Netz:** Paare am Netz. A wirft den Ball seitlich am Netzrand entlang. B macht schnelle Sidesteps, springt und blockt den Ball im Sprung zurück zu A.")
            
        with st.expander("🎯 2. Technik: Der gezielte Lob / Tip (30 Min)"):
            st.markdown("**Auge für den Raum:** Gleicher Aufbau wie TE 1 (Schlagangriff), aber der Spieler springt voll ab, stoppt den Armzug in der Luft ab und tippt den Ball sanft kurz hinter den (imaginären) Block.")
            
        with st.expander("🧠 3. Taktik: Blocken im 3v3 (30 Min)"):
            st.markdown("**Das Dreieck in der Abwehr:** Team A greift an. Bei Team B stellt der Netzspieler (Läufer) einen 1er-Block. Die beiden Annahmespieler formieren sich tief im Feld als V-förmige Abwehr um den Block herum.")
            
        with st.expander("🏆 4. Abschlussspiel: Hit or Tip (20 Min)"):
            st.markdown("**Entscheidungen treffen:** 3v3. Der Trainer hebt während des Angriffs heimlich die Hand (Block) oder nicht. Ist die Hand oben, gibt ein Lob 2 Punkte. Ist sie unten, gibt ein harter Schlag 2 Punkte.")

# ---------------------------------------------------------
# MONAT 3
# ---------------------------------------------------------
elif monat == "Monat 3: Out-of-System & Match-Speed":
    st.header("Monat 3: Lösungen unter Stress")
    
    tab1, tab2 = st.tabs(["TE 1 (Fokus Not-Zuspiel)", "TE 2 (Match-Day)"])
    
    with tab1:
        st.subheader("Trainingseinheit 1: Chaos-Management")
        
        with st.expander("🏃‍♂️ 1. Warm-up: Periphere Sicht (10 Min)"):
            st.markdown("**Blickkontrolle:** Paarweises Baggern. A hält vor dem Ballkontakt 1, 2 oder 3 Finger hoch. B muss rufen, wie viele Finger es waren, *bevor* er den Ball spielt.")
            
        with st.expander("🎯 2. Technik: Out-of-System Zuspiel (30 Min)"):
            st.markdown("**Notpass aus dem Feld:** Trainer wirft tief ins Hinterfeld. Zuspieler (oder Annahme) muss den Ball im Bagger als extrem hohen Pass an die Antenne spielen. Schulterachse zeigt zum Ziel!")
            
        with st.expander("🧠 3. Taktik: Freeball-Kill (30 Min)"):
            st.markdown("**Dankebälle bestrafen:** Trainer schlägt ganz leichten Dankeball ein. Das Team hat exakt 4 Sekunden Zeit, um anzunehmen, perfekt auf Pos III zu stellen und hart anzugreifen.")
            
        with st.expander("🏆 4. Abschlussspiel: Profi-Kaiserplatz (20 Min)"):
            st.markdown("**Vollgas 3v3:** Ball wird per Aufschlag von oben ins Spiel gebracht. Alle Profi-Regeln gelten (Netzfehler, Doppelkontakt werden streng abgepfiffen).")

    with tab2:
        st.subheader("Trainingseinheit 2: Der perfekte Wettkampf")
        
        with st.expander("🏃‍♂️ 1. Warm-up: Profi-Einspielen (15 Min)"):
            st.markdown("**Die Pre-Game-Routine:** Einschlagen wie beim echten Spieltag. Erst paarweise, dann ans Netz. Angriffsreihen über Pos IV und II mit Block durch den Trainer.")
            
        with st.expander("🎯 2. Technik: Der Not-Aufschlag (15 Min)"):
            st.markdown("**Sicherer Ball unter Druck:** Wenn es 14:14 steht, darf kein Aufschlag verschlagen werden. Jeder Spieler muss 5 sichere Aufschläge (von unten oder leichter Float) fehlerfrei ins gegnerische Feld bringen.")
            
        with st.expander("🧠 3. Taktik: Wash-Drill extrem (30 Min)"):
            st.markdown("**Rallye aufrechterhalten:** Team A und B spielen auf 1 Feld. Der Trainer wirft *sofort* den nächsten Ball ein, wenn der erste tot ist. Ziel: Wer gewinnt 3 Bälle in Folge (Triple-Wash)? Baut maximale Kondition und Fokus auf.")
            
        with st.expander("🏆 4. Abschlussspiel: TuB Bocholt Liga (30 Min)"):
            st.markdown("**Das große Finale:** 3v3 auf 2 Gewinnsätze bis 15. Du als Trainer bist Schiedsrichter auf dem Bock. Auszeiten dürfen von den Spielern selbst genommen werden (Taktik-Besprechung ohne Trainer).")

# ---------------------------------------------------------
# LÄUFER-SPEZIAL (PRO-LEVEL)
# ---------------------------------------------------------
elif monat == "Läufer-Spezial: Transition & Kognition":
    st.header("Läufer-Spezial: Transition für Fortgeschrittene")
    
    with st.expander("⏱️ 1. Der Transition-Läufer (15 Min)"):
        st.markdown("**Fokus:** Trainer schlägt (moderat) auf Pos I (Zuspieler). Der Läufer muss den Ball selbst abwehren (hoch in die Feldmitte). Ein Annahmespieler springt ein und übernimmt das Not-Zuspiel.")

    with st.expander("👀 2. Das Scanner-Zuspiel (20 Min)"):
        st.markdown("**Fokus:** Zuspieler läuft ein. Trainer auf Gegenseite hebt linke oder rechte Hand (simuliert Block). Zuspieler pritscht dorthin, wo die Hand *unten* ist.")

    with st.expander("🌪️ 3. Der Dauerläufer (20 Min)"):
        st.markdown("**Fokus:** 1 Zuspieler, 2 Angreifer. Zuspieler sprintet auf Pos III, pritscht auf IV. Rennt rückwärts zurück auf I, sprintet wieder vor, pritscht auf II. 10 Pässe am Stück!")

    with st.expander("🏆 4. Spielform: Der unsichtbare Zuspieler (20 Min)"):
        st.markdown("**Fokus:** 3v3. Wenn das aufschlagende Team den designierten Zuspieler (Pos I) per As trifft, gibt es 3 Punkte. Die Annahme muss den Zuspieler durch geschicktes Verschieben schützen.")
