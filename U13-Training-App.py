import streamlit as st
import os

# Seiten-Konfiguration
st.set_page_config(page_title="U13 Trainingsplan", page_icon="🏐", layout="centered")

st.title("🏐 U13 Trainingsplan – TuB Bocholt")
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
        
        with st.expander("🏃‍♂️ 1. Warm-up: Linien-Fangen & Tic-Tac-Toe (10 Min)"):
            st.markdown("""
            **Detail-Ablauf Linien-Fangen (5 Min):**
            * **Organisation:** Bestimme 2 Fänger. Alle (inkl. Fänger) bewegen sich *ausschließlich* auf den Linien des 9x9m Feldes.
            * **Regel:** Wer neben die Linie tritt, ist gefangen. Strafe: 3 Strecksprünge neben dem Feld, danach sofort wieder mitmachen (kein Ausscheiden!).
            * **Trainer-Fokus:** Bei Begegnungen schnelle Ausfallschritte oder Sidesteps einfordern.

            **Detail-Ablauf Tic-Tac-Toe (5 Min):**
            * **Organisation:** Links und rechts neben dem Feld je ein 3x3 Gitter (Reifen/Tape). 4 Teams à 3 Spieler.
            * **Regel:** Auf Kommando sprintet der Erste, legt ein Leibchen, rennt zurück und schlägt ab. Liegen 3 Leibchen, darf umgelegt werden. Wer zuerst 3 in einer Reihe hat, gewinnt.
            * **Trainer-Fokus:** Maximale Antrittsschnelligkeit.
            """)
            st.image(load_local_image("aufwaermen.jpg"), caption="Warm-Up: Linien-Fangen & Tic-Tac-Toe")
            
        with st.expander("🎯 2. Technik: Insel-Challenge im Stationsbetrieb (30 Min)"):
            st.markdown("""
            **Zielgerichtetes Pritschen und Baggern auf 1 Feld**
            * **Organisation:** 4 Turnmatten ("Inseln") auf Seite A auslegen. Kinder in drei 4er-Gruppen teilen.
            * **Die Rotation:**
                * **Gruppe 1 (Seite B):** Werfen sich den Ball selbst an, spielen gezielt auf die Inseln.
                * **Gruppe 2 (Seite A):** Stehen zwischen den Matten, fangen Bälle, rufen "Treffer!".
                * **Gruppe 3 (Transport):** Rollen Bälle unter dem Netz zügig zu Gruppe 1 zurück.
            * **Ablauf:** Fliegender Wechsel alle 3 Minuten (1 -> 2 -> 3 -> 1).
            * **Trainer-Fokus:** Beinarbeit! Erst unter den Ball laufen, dann aus den Beinen heraus spielen. Beim Pritschen "Körbchen formen" und über der Stirn spielen. Arm-Bagger konsequent korrigieren.
            """)
            st.image(load_local_image("technik_inseln.jpg"), caption="Technik: Gezieltes Pritschen/Baggern auf Matten")
            
        with st.expander("🧠 3. Taktik: Der Einwerfer im Wellenprinzip (30 Min)"):
            st.markdown("""
            **Einführung in das Läufersystem (Laufwege)**
            * **Organisation:** Trainer steht auf einem Kasten in der Mitte am Netz (Ballwagen parat). Auf Seite A und B jeweils ein 3er-Team (Pos 4, 6, 2). Zuspieler auf 1. Rest wartet hinter der Grundlinie.
            * **Ablauf (Die Welle):**
                1. Trainer wirft leicht auf Feld A ein.
                2. Zuspieler sprintet ans Netz. Annahme fängt den Ball und wirft hohen Bogen zum Läufer.
                3. Läufer fängt über dem Kopf und wirft zum Angreifer.
                4. Sobald der Ball drüben ist, rennt das Team Bälle sammeln. Das *nächste* wartende 3er-Team sprintet sofort auf Feld A.
                5. Trainer wirft derweil schon auf Feld B ein.
            * **Trainer-Fokus:** Der Zuspieler darf erst loslaufen, wenn der Ball die Trainer-Hand verlässt (Positionsfehler vermeiden). Kommunikation einfordern ("Ich habe!").
            """)
            st.image(load_local_image("taktik_laeufer.jpg"), caption="Taktik: Das Läufersystem Laufweg-Erklärung")
            
        with st.expander("🏆 4. Abschlussspiel: Kaiserplatz (20 Min)"):
            st.markdown("""
            **Kaiserplatz mit System-Zwang**
            * **Organisation:** Seite A ist die "Kaiserseite". Seite B sind die Herausforderer (ein Team auf dem Feld, Rest wartet an der Grundlinie).
            * **Ablauf:** Trainer wirft Ball bei den Herausforderern ein. 
                * Punktet Seite B -> Wechsel auf die Kaiserseite. Altes Kaiser-Team stellt sich hinten an.
                * Punktet Seite A -> 1 Punkt für den Kaiser. Verlierer-Team B geht raus, nächstes rückt sofort nach.
            * **Sonderregel (U13):** Der Ball *muss* 3-mal gespielt werden (Annahme -> Läufer -> Angriff). Direkte Bälle rüber spielen bedeutet sofortigen Punktverlust.
            * **Trainer-Fokus:** Tempo extrem hoch halten. Sobald der Ball tot ist, direkt den nächsten einwerfen. Das zwingt zur schnellen Rotation.
            """)
            st.image(load_local_image("kaiserplatz.jpg"), caption="Abschlussspiel: Kaiserplatz Turnier-Setup")

    with tab2:
        st.subheader("Trainingseinheit 2")
        st.info("Wiederholung von TE 1. Tausche die Insel-Ziele gegen kleinere Markierungen aus, um die Präzision zu steigern.")

# ---------------------------------------------------------
# MONAT 2
# ---------------------------------------------------------
elif monat == "Monat 2: Systemfestigung":
    st.header("Monat 2: Präzision unter Druck")
    st.success("Tipp: Behalte die Rotations-Prinzipien (Wellenprinzip) aus Monat 1 bei den neuen Übungen bei!")
    
    tab1, tab2 = st.tabs(["TE 1 (Fokus Präzision)", "TE 2 (Fokus Umschaltspiel)"])
    
    with tab1:
        st.subheader("Trainingseinheit 1")
        with st.expander("🏃‍♂️ 1. Warm-up & Athletik (10 Min)"):
            st.markdown("**Spiegelbild am Netz (Ganzes Feld nutzen)**\nAlle Spielerpaare verteilen sich entlang der kompletten Netzkante. Leader macht Sidesteps, Schatten folgt. Nach 60 Sekunden Wechsel. Alle sind gleichzeitig aktiv.")
            
        with st.expander("🎯 2. Technik (30 Min)"):
            st.markdown("**Bagger-Tennis im Endlos-Modus**\n3-gegen-3 auf 1 Feld. Die wartenden Spieler stehen auf Pos 1 hinter dem Feld. Sobald ein Team den Ball rüberspielt, wechselt der Spieler, der den Ball zuletzt berührt hat, sofort vom Feld und ein Neuer sprintet rein.")
            
        with st.expander("🧠 3. Taktik (30 Min)"):
            st.markdown("**System-Drill im Wellenprinzip**\nZwei 3er-Teams auf der Annahmeseite (Team A auf dem Feld, Team B dahinter). Trainer schlägt 3 Bälle (Freeballs) scharf ein. Team A spielt Läufersystem. Nach 3 Bällen sofortiger Wechsel mit Team B.")
            
        with st.expander("🏆 4. Abschlussspiel (20 Min)"):
            st.markdown("**Zusatzpunkt-Wash-Spiel**\nUm einen 'großen' Punkt zu erzielen, muss ein Team 2 Ballwechsel am Stück (Wash) gewinnen. Verliert es den ersten, rückt sofort das nächste Team rein. Zusatzpunkt für sauberes Läufersystem bleibt bestehen.")

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
            st.markdown("**Ball-Klau**\nBegrenze das Feld auf die beiden 3-Meter-Räume. Alle dribbeln ihren Ball und schlagen die Bälle der anderen weg. Wer seinen verliert, macht 3 Strecksprünge am Netz.")
            
        with st.expander("🎯 2. Technik (30 Min)"):
            st.markdown("**Schere-Stein-Papier-Sprint (Beide Hälften)**\nTrainer auf den 3-Meter-Linien als 'Bosse'. Spieler müssen offene Räume anspielen. Nach jedem Ball Sprint zur Seitenlinie, SSP gegen den Wartenden spielen.")
            
        with st.expander("🧠 3. Taktik (30 Min)"):
            st.markdown("**Chaos-Aufbau (Butterfly-System)**\nTeam A schlägt auf Team B auf. Team B baut im System auf und greift an. Team A wehrt ab und baut selbst im System auf (Endlos-Rallye). Fällt der Ball, rücken wartende Teams nach.")
            
        with st.expander("🏆 4. Abschlussspiel (20 Min)"):
            st.markdown("**TuB Bocholt Bundesliga-Blitzturnier**\nSpiele auf exakt 4 Minuten Zeit. Gewinner bleibt stehen, Verlierer geht raus. Extrem kurze Standzeiten. Joker-Karten-Regel gilt!")

    with tab2:
        st.subheader("Trainingseinheit 2")
        st.info("Reiner Turniermodus. Der Trainer greift nur noch bei groben Systemfehlern ein und agiert ansonsten als Schiedsrichter.")
