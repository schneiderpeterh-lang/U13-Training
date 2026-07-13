import streamlit as st
import os

# Seiten-Konfiguration
st.set_page_config(page_title="U13 Trainingsplan", page_icon="🏐", layout="centered")

st.title("🏐 U13 Trainingsplan – TuB Bocholt")
st.markdown("Basierend auf dem WVV-Schulsportportal (Fokus: 1 Feld, 3-gegen-3 im 1:2 System).")

# Navigation
monat = st.selectbox(
    "Wähle den Trainingsmonat:", 
    [
        "Monat 1: WVV Stationskarten & 1:2 System", 
        "Monat 2: WVV Powervolleyball & Analyse", 
        "Monat 3: WVV Spielabzeichen Bronze"
    ]
)

# Hilfsfunktion für lokale Bilder
def load_local_image(filename):
    if os.path.exists(filename):
        return filename
    else:
        return f"https://dummyimage.com/600x300/ccc/000&text=WVV+Bild+{filename}+fehlt"

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
            st.image(load_local_image("wvv_warmup.jpg"), caption="WVV Erwärmung: Ballkoordination")
            
        with st.expander("🎯 2. Technik: WVV Stationskarten für 3er-Gruppen (30 Min)"):
            st.markdown("""
            **Methodische Übungsreihe (Pritschen & Baggern)**
            * **Organisation:** 3er-Gruppen bilden (A: Anwerfer, B: Übender, C: Fänger). Alle Gruppen nutzen das Feld quer (über das Netz oder eine Zauberschnur).
            * **Ablauf (Pritschen):** Spieler A wirft beidhändig im hohen Bogen an. Spieler B pritscht den Ball hoch über das Netz. Spieler C fängt den Ball. Rotation nach 10 Wiederholungen (A->B, B->C, C->A).
            * **Ablauf (Baggern):** Gleicher Aufbau. Der Ball wird nun flacher angeworfen und gezielt als Bagger zu C gespielt.
            * **WVV-Tipp:** Rufe dir die offiziellen WVV-Technikvideos für das Leitbild (Körbchen formen / Spielbrett) auf dem Handy auf und zeige sie den Kindern direkt am Netz.
            """)
            st.image(load_local_image("wvv_stationen.jpg"), caption="WVV Stationskarten: 3er-Gruppen am Netz")
            
        with st.expander("🧠 3. Taktik: WVV 3-gegen-3 (1:2 System) Einführung (30 Min)"):
            st.markdown("""
            **Das 1:2 System (1 Zuspieler, 2 Annahme)**
            * **Organisation:** Trainer steht am Netz. Zwei 3er-Teams besetzen die beiden Netzhälften (Zuspieler in der Mitte am Netz auf Pos. III, Annahmespieler auf Pos. IV und II leicht nach hinten versetzt).
            * **Ablauf:** Trainer wirft den Ball im Wechsel auf Seite A und B ein. Die Annahme baggert zum Zuspieler. Der Zuspieler pritscht den Ball als Bogenpass zurück zu einem Angreifer, der den Ball fängt (noch kein Schlag).
            * **Trainer-Fokus:** Orientierung des Zuspielers (Rücken zur Seitenlinie, Blick ins Feld). Der Ball muss im hohen Bogen gespielt werden.
            """)
            st.image(load_local_image("wvv_1_2_system.jpg"), caption="WVV Taktik: 3v3 (1:2 System)")
            
        with st.expander("🏆 4. Abschlussspiel: WVV Kleinfeld-Turnier (20 Min)"):
            st.markdown("""
            **3-gegen-3 Spielform (Mit Fangen)**
            * **Organisation:** 1 Feld, 3-gegen-3 spielen. Wartende Teams stehen an der Grundlinie.
            * **Ablauf:** Normale Regeln, aber der 2. Ball (das Zuspiel) darf gefangen und geworfen werden, um das System zu festigen. Der 1. und 3. Ball müssen volley gespielt werden.
            * **Trainer-Fokus:** Konsequenter Fokus auf den Aufbau über die Position III. Direkte Bälle über das Netz führen zum Punktabzug.
            """)
            st.image(load_local_image("wvv_kleinfeld.jpg"), caption="WVV Abschlussspiel: System-Fokus")

    with tab2:
        st.subheader("Trainingseinheit 2")
        st.info("Wiederholung von TE 1. Lasst beim Abschlussspiel das Fangen weg und fordert das saubere Pritschen auf Position III ein.")

# ---------------------------------------------------------
# MONAT 2
# ---------------------------------------------------------
elif monat == "Monat 2: WVV Powervolleyball & Analyse":
    st.header("Monat 2: Powervolleyball & Spielerbeobachtung")
    st.success("Tipp: Die WVV-Beobachtungsbögen halten auch die wartenden Spieler auf dem Feld konzentriert!")
    
    tab1, tab2 = st.tabs(["TE 1 (Fokus Taktik)", "TE 2 (Fokus Angriff)"])
    
    with tab1:
        st.subheader("Trainingseinheit 1")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min)"):
            st.markdown("**WVV Aufwärm-Spiele**\nPaarweises Zuwerfen über das Netz. Zusatzaufgabe: Nach dem Wurf sofort den Boden berühren (Tiefe Abwehrhaltung) und wieder fangbereit stehen.")
            
        with st.expander("🎯 2. Technik (30 Min)"):
            st.markdown("**WVV Stationskarten: Der Dankeball**\n3er Gruppen. Spieler A wirft einen hohen 'Freeball' über das Netz. Spieler B muss den Ball im Bagger sauber auf Position III spielen. Spieler C (Zuspieler) fängt ihn. Fliegender Wechsel.")
            
        with st.expander("🧠 3. Taktik: WVV Spielerbeobachtung im 1:2 System (30 Min)"):
            st.markdown("**Die Beobachtungs-Aufgabe**\nEin 3er-Team spielt auf dem Feld, ein 3er-Team beobachtet von außen (Nutze den WVV Beobachtungsbogen). Trainer wirft Bälle im 'Powervolleyball'-Stil (zügig nacheinander) ein. Beobachter machen Striche bei: *'Zuspieler bewegt sich schnell zur Pos III'* und *'Zuspieler spielt den Ball im hohen Bogen'*.")
            
        with st.expander("🏆 4. Abschlussspiel (20 Min)"):
            st.markdown("**Powervolleyball-Turnier**\n3v3 Teams. Keine Aufschläge! Der Trainer feuert die Bälle extrem schnell als 'Dankebälle' nacheinander ein. Welches Team hält sein 1:2 System trotz der Geschwindigkeit aufrecht?")

    with tab2:
        st.subheader("Trainingseinheit 2")
        st.info("Fokus auf den Zuspieler. Beobachtungsaufgabe für die Wartenden: *'Steht der Zuspieler rechtzeitig still, bevor er den Ball pritscht?'*")

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
            
        with st.expander("🎯 2. Technik: Spielabzeichen Bronze (Pritschen & Baggern) (30 Min)"):
            st.markdown("**Stationstraining für die Prüfung**\n*Station 1 (Pritschen):* 10 saubere Pässe (Ziel-Pritschen) über 3 Meter in einen Reifen auf dem Boden.\n*Station 2 (Baggern):* 5 angeworfene Bälle (durch Trainer) im Bagger kontrolliert in einen markierten 3x3-Meter Raum spielen.")
            
        with st.expander("🧠 3. Taktik: WVV 1:2 System (Aufschlag-Annahme) (30 Min)"):
            st.markdown("**Der Ernstfall**\nDas Powervolleyball (Einwerfen) wird durch Aufschläge von unten ersetzt. Team A schlägt auf, Team B baut im 1:2 System auf. Das Abzeichen erfordert saubere Annahme unter realen Bedingungen.")
            
        with st.expander("🏆 4. Abschlussspiel (20 Min)"):
            st.markdown("**Turniermodus**\n3v3 nach offiziellen WVV Schulsportregeln (Kleinfeld). Gewinnerteam bekommt extra Zeit, um die Stationen für das Abzeichen weiter zu üben.")

    with tab2:
        st.subheader("Trainingseinheit 2")
        st.info("Abnahme des WVV-Spielabzeichens (Bronze) an den Stationen für alle Kinder. Danach feierliches Abschluss-Turnier im 1:2 System.")
