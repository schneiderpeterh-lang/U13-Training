import streamlit as st
import os

# Seiten-Konfiguration
st.set_page_config(page_title="U13/U14 Trainingsplan", page_icon="🏐", layout="centered")

st.title("🏐 U13/U14 PRO Plan")
st.markdown("TuB Bocholt | 2x Training pro Woche (8 TE pro Monat)")

# Navigation - Monat
monat = st.selectbox(
    "Wähle den Trainingsmonat:", 
    [
        "Monat 1: Tempo & Aufschlag von oben", 
        "Monat 2: Angriff & Sicherung", 
        "Monat 3: Out-of-System & Match-Speed",
        "System-Spezial: 3v3 meets 4v4"
    ]
)

# Hilfsfunktion für lokale Bilder (lädt lokales Bild oder einen dynamischen Platzhalter)
def load_local_image(filename, beschreibung):
    if os.path.exists(filename):
        return filename
    else:
        # Erzeugt ein graues Bild mit Text, falls das lokale Bild noch fehlt
        text = beschreibung.replace(" ", "+")
        return f"https://dummyimage.com/600x300/e0e0e0/000000&text={text}"

# ---------------------------------------------------------
# MONAT 1 (VOLLSTÄNDIG - 4 Wochen / 8 TE)
# ---------------------------------------------------------
if monat == "Monat 1: Tempo & Aufschlag von oben":
    st.header("Monat 1: Schnelles System & Aufschlagdruck")
    
    # Wochen-Navigation per Tabs
    w1, w2, w3, w4 = st.tabs(["Woche 1", "Woche 2", "Woche 3", "Woche 4"])
    
    # ---------------- WOCHE 1 ----------------
    with w1:
        st.subheader("TE 1: Basis Volley-Tempo")
        with st.expander("🏃‍♂️ 1. Warm-up: Kognitives Chaos (10 Min)"):
            st.markdown("**Gemeinsam:** Paarweise am Netz. A pritscht Ball 1, B rollt Ball 2. Auf Pfiff: Sprint zur Grundlinie und zurück.")
            st.image(load_local_image("m1_w1_e1.jpg", "Bild: Kognitives Chaos (Paare)"), caption="Visualisierung: Zwei-Ball-Koordination")
            
        with st.expander("🎯 2. Technik: Präzisions-Zuspiel aus der Bewegung (30 Min)"):
            st.markdown("**Gemeinsam:** Zuspieler startet auf Pos I oder V. Trainer schlägt Dankebälle ein. Zuspieler sprintet ein, **stoppt komplett ab**, dreht Schulterachse und pritscht.")
            st.image(load_local_image("m1_w1_e2.jpg", "Bild: Zuspieler stoppt ab"), caption="Visualisierung: Sauberer Stand vor dem Pritschen")
            
        with st.expander("🧠 3. Taktik: Mixed-System Wellenprinzip (30 Min)"):
            st.markdown("**Split:** Seite A (U14) baut 4v4 Rauten-System auf. Seite B (U13) baut 3v3 (1:2 Läufer) auf. Trainer schlägt abwechselnd ein.")
            st.image(load_local_image("m1_w1_e3.jpg", "Bild: 4v4 vs 3v3 Split"), caption="Visualisierung: Ein Feld, zwei Systeme")
            
        with st.expander("🏆 4. Abschlussspiel: 4v3 Handicap (20 Min)"):
            st.markdown("**Handicap:** U14 (zu 4.) vs. U13 (zu 3.). U14 darf nur schlagen, U13 darf clever loben.")
            st.image(load_local_image("m1_w1_e4.jpg", "Bild: 4 gegen 3 Spielform"), caption="Visualisierung: Überzahlspiel")

        st.divider()

        st.subheader("TE 2: Basis Tennis-Aufschlag")
        with st.expander("🏃‍♂️ 1. Warm-up: Aufschlag-Staffel (10 Min)"):
            st.markdown("**Gemeinsam:** Sprint zum Netz, Ball nehmen, Anwurf für Tennis-Aufschlag simulieren, fangen, Sprint zurück.")
            st.image(load_local_image("m1_w1_e5.jpg", "Bild: Aufschlag-Staffel"), caption="Visualisierung: Anwurf-Training in der Staffel")
            
        with st.expander("🎯 2. Technik: Aufschlag von oben (30 Min)"):
            st.markdown("**Gemeinsam:** Gegen die Wand werfen & schlagen. Danach Aufschlag von 3m-Linie übers Netz. U14 von hinten, U13 von 6m-Linie.")
            st.image(load_local_image("m1_w1_e6.jpg", "Bild: Tennis-Aufschlag Technik"), caption="Visualisierung: Treffpunkt und Handgelenk")
            
        with st.expander("🧠 3. Taktik: Serve & Pass (30 Min)"):
            st.markdown("**Split:** U14 schlägt von oben auf. U13 muss Annahme kontrollieren, Läufer anspielen und Ball rüberspielen. Wechsel nach 5x.")
            st.image(load_local_image("m1_w1_e7.jpg", "Bild: Serve and Pass Komplexe"), caption="Visualisierung: Aufschlag gegen Annahmeriegel")
            
        with st.expander("🏆 4. Abschlussspiel: Integration (20 Min)"):
            st.markdown("**Hochziehen:** Reines 4v4. U13 Spieler werden in U14-Teams integriert, um Laufwege auf großem Feld zu lernen.")
            st.image(load_local_image("m1_w1_e8.jpg", "Bild: 4v4 Mixed Teams"), caption="Visualisierung: U13 lernt die 4v4 Raute")

    # ---------------- WOCHE 2 ----------------
    with w2:
        st.subheader("TE 3: Zuspiel unter Druck")
        with st.expander("🏃‍♂️ 1. Warm-up: Linien-Fangen (10 Min)"):
            st.markdown("**Gemeinsam:** Klassisches Linienfangen auf dem ganzen Feld. Tiefe Haltung fordern!")
            st.image(load_local_image("m1_w2_e1.jpg", "Bild: Linienfangen im Feld"), caption="Visualisierung: Beinarbeit")
        with st.expander("🎯 2. Technik: Dankeball-Sprint (30 Min)"):
            st.markdown("**Gemeinsam:** Zuspieler startet auf Grundlinie. Trainer wirft hohen Ball ans Netz. Sprint -> sauber abstoppen -> Pass auf IV.")
            st.image(load_local_image("m1_w2_e2.jpg", "Bild: Sprint zum Netz"), caption="Visualisierung: Antritt des Zuspielers")
        with st.expander("🧠 3. Taktik: System-Drill mit Abwehr (30 Min)"):
            st.markdown("**Split:** Wie Woche 1, aber Trainer schlägt hart (keine Dankebälle mehr). Annahme muss tief bleiben.")
            st.image(load_local_image("m1_w2_e3.jpg", "Bild: Harter Trainerspezifischer Angriff"), caption="Visualisierung: Tiefe Abwehrhaltung")
        with st.expander("🏆 4. Abschlussspiel: Wash-Game (20 Min)"):
            st.markdown("**Punkte-Regel:** 2 Rallyes in Folge gewinnen = 1 Punkt. Fördert Konzentration.")
            st.image(load_local_image("m1_w2_e4.jpg", "Bild: Wash-Game Turnier"), caption="Visualisierung: 3v3/4v4 Matchpraxis")

        st.divider()

        st.subheader("TE 4: Ziel-Aufschlag")
        with st.expander("🏃‍♂️ 1. Warm-up: Reaktions-Sprints (10 Min)"):
            st.markdown("**Gemeinsam:** Spieler liegen am Netz. Auf Pfiff: Aufstehen, rückwärts bis 3m-Linie, vorwärts ans Netz hechten.")
            st.image(load_local_image("m1_w2_e5.jpg", "Bild: Boden-Sprints"), caption="Visualisierung: Schnelles Aufstehen")
        with st.expander("🎯 2. Technik: Zonen-Aufschlag (30 Min)"):
            st.markdown("**Gemeinsam:** Turnmatten in die Ecken legen. Aufschläge von oben auf die Matten zielen.")
            st.image(load_local_image("m1_w2_e6.jpg", "Bild: Matten als Ziele in Ecken"), caption="Visualisierung: Zonen-Aufschlag")
        with st.expander("🧠 3. Taktik: Aufschlag-Rezeption (30 Min)"):
            st.markdown("**Split:** U14 schlägt gezielt in die Ecken auf, U13 muss die Lücken schließen und aufbauen.")
            st.image(load_local_image("m1_w2_e7.jpg", "Bild: Annahme verschieben"), caption="Visualisierung: Lücken schließen")
        with st.expander("🏆 4. Abschlussspiel: Aufschlag-König (20 Min)"):
            st.markdown("**Sonderregel:** Direktes Aufschlag-Ass = direkter Seitenwechsel auf die 'Kaiser-Seite'.")
            st.image(load_local_image("m1_w2_e8.jpg", "Bild: Kaiserplatz mit Aufschlag"), caption="Visualisierung: Belohnung für Aufschläge")

    # ---------------- WOCHE 3 ----------------
    with w3:
        st.subheader("TE 5: Transition-Offense")
        with st.expander("🏃‍♂️ 1. Warm-up: Ball-Klau (10 Min)"):
            st.markdown("**Gemeinsam:** Alle dribbeln Ball im 3m-Raum und versuchen, anderen Bälle wegzuschlagen.")
            st.image(load_local_image("m1_w3_e1.jpg", "Bild: Dribbling und Ballklau"), caption="Visualisierung: Periphere Sicht")
        with st.expander("🎯 2. Technik: Abwehr-Zuspiel (30 Min)"):
            st.markdown("**Gemeinsam:** Trainer schlägt auf Zuspieler. Dieser wehrt ab. Annahme muss aushelfen und hoch zuspielen.")
            st.image(load_local_image("m1_w3_e2.jpg", "Bild: Not-Zuspiel durch Annahme"), caption="Visualisierung: Libero/Annahme stellt")
        with st.expander("🧠 3. Taktik: Butterfly-Drill (30 Min)"):
            st.markdown("**Split:** Team A schlägt auf Team B auf. B greift an, A wehrt ab und baut Gegenangriff (Transition) auf.")
            st.image(load_local_image("m1_w3_e3.jpg", "Bild: Butterfly Drill Flow"), caption="Visualisierung: Endlos-Rotation")
        with st.expander("🏆 4. Abschlussspiel: Dauer-Feuer (20 Min)"):
            st.markdown("**Trainer-Druck:** Sobald Ball tot ist, wirft Trainer sofort nächsten ein. Keine Pause.")
            st.image(load_local_image("m1_w3_e4.jpg", "Bild: Trainer wirft Bälle ein"), caption="Visualisierung: Hohe Belastung")

        st.divider()

        st.subheader("TE 6: Aufschlag unter Ermüdung")
        with st.expander("🏃‍♂️ 1. Warm-up: Block-Schatten (10 Min)"):
            st.markdown("**Gemeinsam:** Paare am Netz. Leader macht Sidesteps/Blocksprünge, Schatten folgt.")
            st.image(load_local_image("m1_w3_e5.jpg", "Bild: Spiegelbild am Netz"), caption="Visualisierung: Beinarbeit am Netz")
        with st.expander("🎯 2. Technik: Sprint & Serve (30 Min)"):
            st.markdown("**Gemeinsam:** Blocksprung am Netz, Sprint rückwärts, Ball fangen, sofort von oben aufschlagen.")
            st.image(load_local_image("m1_w3_e6.jpg", "Bild: Sprint zum Aufschlag"), caption="Visualisierung: Puls hochtreiben")
        with st.expander("🧠 3. Taktik: Rette das System (30 Min)"):
            st.markdown("**Split:** Trainer wirft extrem schlechte Bälle. Teams müssen retten und trotzdem angreifen.")
            st.image(load_local_image("m1_w3_e7.jpg", "Bild: Hechtbagger ins Feld"), caption="Visualisierung: Out-of-System retten")
        with st.expander("🏆 4. Abschlussspiel: Joker-Turnier (20 Min)"):
            st.markdown("**Level Up:** Jedes Team hat 2 Joker-Karten. Einsatz verdoppelt Punkte der nächsten Rallye.")
            st.image(load_local_image("m1_w3_e8.jpg", "Bild: Turnier mit Taktik"), caption="Visualisierung: Spielsteuerung")

    # ---------------- WOCHE 4 ----------------
    with w4:
        st.subheader("TE 7: Match-Simulation")
        with st.expander("🏃‍♂️ 1. Warm-up: Pre-Game Routine (15 Min)"):
            st.markdown("**Gemeinsam:** Offizielles Einspielen wie am Spieltag. Einschlagen am Netz mit Block durch Trainer.")
            st.image(load_local_image("m1_w4_e1.jpg", "Bild: Offizielles Einschlagen"), caption="Visualisierung: Pre-Game Routine")
        with st.expander("🎯 2. Technik & Taktik: Systemprüfung (25 Min)"):
            st.markdown("**Mixed-Wellenprinzip:** Harte Aufschläge (U14/Trainer). Welle 1 = 3 Sek für perfekten Aufbau. Welle 2 = 4 Sek.")
            st.image(load_local_image("m1_w4_e2.jpg", "Bild: Aufschlag gegen Annahmeriegel"), caption="Visualisierung: Prüfung unter Druck")
        with st.expander("🏆 3. Abschlussspiel: TuB Bocholt Liga Hinrunde (50 Min)"):
            st.markdown("**Turnier:** Wettkampf. Wenn möglich, Feld teilen. Sonst 4v4 (U13 integriert). Du bist Schiri.")
            st.image(load_local_image("m1_w4_e3.jpg", "Bild: Liga Turnier Spielszene"), caption="Visualisierung: Echter Wettkampf")

        st.divider()

        st.subheader("TE 8: Finaltag")
        with st.expander("🏃‍♂️ 1. Warm-up: Kopfball-Volleyball (10 Min)"):
            st.markdown("**Gemeinsam:** 2v2 über tiefes Netz. Ball darf nur per Kopf/Fuß gespielt werden. Lockert Stimmung!")
            st.image(load_local_image("m1_w4_e4.jpg", "Bild: Kopfball Spiel"), caption="Visualisierung: Spaßiges Aufwärmen")
        with st.expander("🧠 2. Taktik: Der Not-Aufschlag (20 Min)"):
            st.markdown("**Drucksituation:** '14:14 im 3. Satz'. Jeder muss 3 fehlerfreie, leichte Aufschläge übers Netz bringen.")
            st.image(load_local_image("m1_w4_e5.jpg", "Bild: Konzentrierter Aufschlag"), caption="Visualisierung: Nervenstärke")
        with st.expander("🏆 3. Abschlussspiel: TuB Bocholt Liga Rückrunde (60 Min)"):
            st.markdown("**Turnier:** Fortsetzung TE 7. Sieger darf Warm-Up am Dienstag leiten.")
            st.image(load_local_image("m1_w4_e6.jpg", "Bild: Jubelndes Team"), caption="Visualisierung: Liga Finale")

# ... (Monat 2, 3 und Spezial-Tab bleiben wie im vorherigen Code, du kannst diese Logik analog fortsetzen!)
