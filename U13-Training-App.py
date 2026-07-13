import streamlit as st

# Seiten-Konfiguration
st.set_page_config(page_title="U13 Trainingsplan", page_icon="🏐", layout="centered")

st.title("🏐 U13 Trainingsplan – TuB Bocholt")
st.markdown("Basierend auf dem WVV-Schulsportportal (Fokus: 1 Feld, 3-gegen-3 im 1:2 System).")

# Navigation
monat = st.selectbox(
    "Wähle den Trainingsbereich:", 
    [
        "Monat 1: WVV Stationskarten & 1:2 System", 
        "Monat 2: WVV Powervolleyball & Analyse", 
        "Monat 3: WVV Spielabzeichen Bronze",
        "Läufer-Spezial: System-Drills"
    ]
)

# ---------------------------------------------------------
# MONAT 1
# ---------------------------------------------------------
if monat == "Monat 1: WVV Stationskarten & 1:2 System":
    st.header("Monat 1: WVV Grundtechniken & Laufwege")
    
    tab1, tab2 = st.tabs(["TE 1 (Fokus Technik)", "TE 2 (Fokus System)"])
    
    with tab1:
        st.subheader("Trainingseinheit 1")
        
        with st.expander("🏃‍♂️ 1. Warm-up: WVV Ballkoordination (10 Min)"):
            st.markdown("""
            **Die WVV Volleyball-Challenge**
            * **Organisation:** Spieler verteilen sich paarweise auf dem Feld. Jedes Paar hat einen Ball.
            * **Ablauf:** Abwechselndes Werfen und Fangen in der tiefen Volleyball-Grundstellung. Steigerung: Der Ball wird angeworfen und mit dem Unterarm-Spielbrett (ohne Schwung!) zum Partner zurückgedrückt.
            * **Trainer-Fokus:** Knie beugen! Der Schwerpunkt muss unten bleiben.
            """)
            
        with st.expander("🎯 2. Technik: WVV Stationskarten für 3er-Gruppen (30 Min)"):
            st.markdown("""
            **Methodische Übungsreihe (Pritschen & Baggern)**
            * **Organisation:** 3er-Gruppen bilden (A: Anwerfer, B: Übender, C: Fänger). Alle Gruppen nutzen das Feld quer (über das Netz oder eine Zauberschnur).
            * **Ablauf (Pritschen):** Spieler A wirft beidhändig im hohen Bogen an. Spieler B pritscht den Ball hoch über das Netz. Spieler C fängt den Ball. Rotation nach 10 Wiederholungen.
            * **Ablauf (Baggern):** Gleicher Aufbau. Der Ball wird nun flacher angeworfen und gezielt als Bagger zu C gespielt.
            * **WVV-Tipp:** Nutze die offiziellen WVV-Technikvideos für das Leitbild (Körbchen formen / Spielbrett).
            """)
            
        with st.expander("🧠 3. Taktik: WVV 3-gegen-3 (1:2 System) Einführung (30 Min)"):
            st.markdown("""
            **Das 1:2 System (1 Zuspieler, 2 Annahme)**
            * **Organisation:** Trainer steht am Netz. Zwei 3er-Teams besetzen die Netzhälften (Zuspieler in der Mitte am Netz auf Pos. III, Annahmespieler auf Pos. IV und II).
            * **Ablauf:** Trainer wirft den Ball im Wechsel auf Seite A und B ein. Die Annahme baggert zum Zuspieler. Der Zuspieler pritscht den Ball als Bogenpass zurück zu einem Angreifer, der den Ball fängt.
            * **Trainer-Fokus:** Orientierung des Zuspielers (Rücken zur Seitenlinie, Blick ins Feld). Der Ball muss im hohen Bogen gespielt werden.
            """)
            
        with st.expander("🏆 4. Abschlussspiel: WVV Kleinfeld-Turnier (20 Min)"):
            st.markdown("""
            **3-gegen-3 Spielform (Mit Fangen)**
            * **Organisation:** 1 Feld, 3-gegen-3 spielen. Wartende Teams stehen an der Grundlinie.
            * **Ablauf:** Normale Regeln, aber der 2. Ball (das Zuspiel) darf gefangen und geworfen werden, um das System zu festigen. Der 1. und 3. Ball müssen volley gespielt werden.
            * **Trainer-Fokus:** Direkte Bälle über das Netz führen zum Punktabzug.
            """)

    with tab2:
        st.subheader("Trainingseinheit 2")
        st.info("Wiederholung von TE 1. Lasst beim Abschlussspiel das Fangen weg und fordert das saubere Pritschen auf Position III ein.")

# ---------------------------------------------------------
# MONAT 2
# ---------------------------------------------------------
elif monat == "Monat 2: WVV Powervolleyball & Analyse":
    st.header("Monat 2: Powervolleyball & Spielerbeobachtung")
    
    tab1, tab2 = st.tabs(["TE 1 (Fokus Taktik)", "TE 2 (Fokus Angriff)"])
    
    with tab1:
        st.subheader("Trainingseinheit 1")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min)"):
            st.markdown("**WVV Aufwärm-Spiele**\nPaarweises Zuwerfen über das Netz. Zusatzaufgabe: Nach dem Wurf sofort den Boden berühren und wieder fangbereit stehen.")
            
        with st.expander("🎯 2. Technik (30 Min)"):
            st.markdown("**WVV Stationskarten: Der Dankeball**\n3er Gruppen. Spieler A wirft einen hohen 'Freeball' über das Netz. B baggert auf Position III. C (Zuspieler) fängt. Fliegender Wechsel.")
            
        with st.expander("🧠 3. Taktik: WVV Spielerbeobachtung (30 Min)"):
            st.markdown("**Die Beobachtungs-Aufgabe**\nEin 3er-Team spielt, ein 3er-Team beobachtet von außen. Trainer wirft Bälle zügig nacheinander ein. Beobachter machen Striche bei: *'Zuspieler bewegt sich schnell zur Pos III'* und *'Zuspieler spielt hohen Bogen'*.")
            
        with st.expander("🏆 4. Abschlussspiel (20 Min)"):
            st.markdown("**Powervolleyball-Turnier**\n3v3 Teams. Keine Aufschläge! Trainer feuert Bälle extrem schnell als 'Dankebälle' nacheinander ein. Welches Team hält sein 1:2 System?")

    with tab2:
        st.subheader("Trainingseinheit 2")
        st.info("Fokus auf den Zuspieler. Beobachtungsaufgabe für Wartende: *'Steht der Zuspieler rechtzeitig still, bevor er pritscht?'*")

# ---------------------------------------------------------
# MONAT 3
# ---------------------------------------------------------
elif monat == "Monat 3: WVV Spielabzeichen Bronze":
    st.header("Monat 3: WVV Volleyball-Spielabzeichen (Bronze)")
    
    tab1, tab2 = st.tabs(["TE 1 (Prüfungsvorbereitung)", "TE 2 (Abzeichen & Turnier)"])
    
    with tab1:
        st.subheader("Trainingseinheit 1")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min)"):
            st.markdown("**Koordination am Netz**\nBall über das Netz pritschen, unter dem Netz durchrutschen, eigenen Ball wieder fangen (nach 1x aufkommen).")
            
        with st.expander("🎯 2. Technik: Spielabzeichen Bronze (30 Min)"):
            st.markdown("**Stationstraining für die Prüfung**\n*Station 1 (Pritschen):* 10 saubere Pässe über 3 Meter in einen Reifen.\n*Station 2 (Baggern):* 5 angeworfene Bälle kontrolliert in markierten 3x3-Meter Raum spielen.")
            
        with st.expander("🧠 3. Taktik: WVV 1:2 System unter Druck (30 Min)"):
            st.markdown("**Der Ernstfall**\nDas Einwerfen wird durch Aufschläge von unten ersetzt. Team A schlägt auf, Team B baut im 1:2 System auf. Das Abzeichen erfordert saubere Annahme unter realen Bedingungen.")
            
        with st.expander("🏆 4. Abschlussspiel (20 Min)"):
            st.markdown("**Turniermodus**\n3v3 nach offiziellen WVV Schulsportregeln (Kleinfeld). Gewinnerteam bekommt extra Zeit, um die Stationen für das Abzeichen weiter zu üben.")

    with tab2:
        st.subheader("Trainingseinheit 2")
        st.info("Abnahme des WVV-Spielabzeichens (Bronze) an den Stationen für alle Kinder. Danach feierliches Abschluss-Turnier im 1:2 System.")

# ---------------------------------------------------------
# LÄUFER-SPEZIAL
# ---------------------------------------------------------
elif monat == "Läufer-Spezial: System-Drills":
    st.header("Läufer-Spezial: Intensiv-Drills für das 1:2 System")
    st.success("Tipp: Nutze diese Übungen, wenn das System im normalen Training wackelt oder die Laufwege unsauber werden.")
    
    with st.expander("⏱️ 1. Timing: Der Ampel-Start (15 Min)"):
        st.markdown("""
        **Fokus: Der Zuspieler darf erst laufen, wenn der Aufschlag erfolgt.**
        * **Organisation (1 Feld):** Trainer steht auf der Aufschlagseite mit Ballwagen. Zwei 3er-Teams stehen auf der Gegenseite. Der Rest sammelt Bälle.
        * **Ablauf:** Der Trainer tut so, als würde er aufschlagen. 
            * *Rote Ampel:* Trainer wirft an, fängt aber wieder auf (Fake). Wer jetzt schon losläuft, muss zurück.
            * *Grüne Ampel:* Trainer schlägt wirklich auf. Jetzt erst sprintet der Zuspieler von Pos I auf Pos III.
        * **Trainer-Fokus:** Konsequenter Blick des Zuspielers zum Trainer. Explosiver Start im exakt richtigen Moment.
        """)

    with st.expander("🔄 2. Wiederholung: Das Zuspiel-Karussell (20 Min)"):
        st.markdown("""
        **Fokus: Einlaufen, sauberes Stellen und schnelles Umschalten.**
        * **Organisation (1 Feld):** Trainer steht auf Pos VI mit Ballwagen. Ein Angreifer auf Pos IV. 3 Zuspieler in Reihe hinter Pos I.
        * **Ablauf (Dauerschleife):** 1. Zuspieler 1 sprintet auf Pos III.
            2. Trainer wirft unsauber an (simuliert Annahme).
            3. Zuspieler 1 pritscht zum Angreifer und sprintet sofort zurück ans Ende der Schlange.
            4. In dem Moment, wo Zuspieler 1 pritscht, sprintet Zuspieler 2 los.
        * **Trainer-Fokus:** Der Zuspieler muss vor dem Ballkontakt **stehen**! Wer im Laufen pritscht, wird korrigiert.
        """)

    with st.expander("🌪️ 3. Reaktion: Der Chaos-Läufer (20 Min)"):
        st.markdown("""
        **Fokus: Was tun, wenn die Annahme am Netz klebt oder zu weit hinten ist?**
        * **Organisation (Wellenprinzip):** 3er-Teams auf beiden Seiten. Trainer wirft abwechselnd auf Seite A und B ein.
        * **Ablauf:** Der Trainer wirft absichtlich extrem schlecht ein (z.B. fast ins Netz oder sehr kurz).
        * **Aufgabe Läufer:** * Ball erreichbar? Sprinten und hoch auf Pos IV pritschen/baggern.
            * Ball nicht erreichbar? Laut "HILFE!" rufen. Ein Annahmespieler übernimmt.
        * **Trainer-Fokus:** Mut zum Rufen! Kommunikation rettet den Ball.
        """)

    with st.expander("🏆 4. Spielform: Läufer-Bingo (20 Min)"):
        st.markdown("""
        **Fokus: System-Anwendung unter Turnier-Bedingungen.**
        * **Organisation:** 3v3 auf Zeit (z.B. 4 Minuten).
        * **Ablauf:** Normales Spiel. Es gibt ein "Bingo", wenn ein Punkt so erzielt wird: 
            1. Gegnerischer Ball abgewehrt.
            2. Läufer rechtzeitig auf Pos III.
            3. Pritsche über Kopf.
            4. Angriff führt zum direkten Punkt.
        * **Punkte-Regel:** Normaler Punkt = 1. Bingo-Punkt = 3!
        * **Trainer-Fokus:** Lobe System-Versuche, auch wenn der Angriff im Aus landet. Das System soll erzwungen werden.
        """)
