import streamlit as st

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
        with st.expander("🎯 2. Technik: Zuspiel im Sprung (30 Min)"):
            st.markdown("**Gemeinsam:** Trainer schlägt Dankebälle ein. Zuspieler *muss* springen und im Sprung pritschen. (U14 schlägt auf U13 ein).")
        with st.expander("🧠 3. Taktik: Mixed-System Wellenprinzip (30 Min)"):
            st.markdown("**Split:** Seite A (U14) baut 4v4 Rauten-System auf. Seite B (U13) baut 3v3 (1:2 Läufer) auf. Trainer schlägt abwechselnd ein.")
        with st.expander("🏆 4. Abschlussspiel: 4v3 Handicap (20 Min)"):
            st.markdown("**Handicap:** U14 (zu 4.) vs. U13 (zu 3.). U14 darf nur schlagen, U13 darf clever loben.")

        st.divider()

        st.subheader("TE 2: Basis Tennis-Aufschlag")
        with st.expander("🏃‍♂️ 1. Warm-up: Aufschlag-Staffel (10 Min)"):
            st.markdown("**Gemeinsam:** Sprint zum Netz, Ball nehmen, Anwurf für Tennis-Aufschlag simulieren, fangen, Sprint zurück.")
        with st.expander("🎯 2. Technik: Aufschlag von oben (30 Min)"):
            st.markdown("**Gemeinsam:** Gegen die Wand werfen & schlagen. Danach Aufschlag von 3m-Linie übers Netz. U14 von hinten, U13 von 6m-Linie.")
        with st.expander("🧠 3. Taktik: Serve & Pass (30 Min)"):
            st.markdown("**Split:** U14 schlägt von oben auf. U13 muss Annahme kontrollieren, Läufer anspielen und Ball rüberspielen. Wechsel nach 5x.")
        with st.expander("🏆 4. Abschlussspiel: Integration (20 Min)"):
            st.markdown("**Hochziehen:** Reines 4v4. U13 Spieler werden in U14-Teams integriert, um Laufwege auf großem Feld zu lernen.")

    # ---------------- WOCHE 2 ----------------
    with w2:
        st.info("Fokus Woche 2: Härte im Zuspiel und Aufschlag-Zielgenauigkeit.")
        st.subheader("TE 3: Zuspiel unter Druck")
        with st.expander("🏃‍♂️ 1. Warm-up: Linien-Fangen (10 Min)"):
            st.markdown("**Gemeinsam:** Klassisches Linienfangen auf dem ganzen Feld. Tiefe Haltung fordern!")
        with st.expander("🎯 2. Technik: Dankeball-Sprint (30 Min)"):
            st.markdown("**Gemeinsam:** Zuspieler startet auf Grundlinie. Trainer wirft hohen Ball ans Netz. Sprint -> Sprung -> Pass auf IV.")
        with st.expander("🧠 3. Taktik: System-Drill mit Abwehr (30 Min)"):
            st.markdown("**Split:** Wie Woche 1, aber Trainer schlägt hart (keine Dankebälle mehr). Annahme muss tief bleiben.")
        with st.expander("🏆 4. Abschlussspiel: Wash-Game (20 Min)"):
            st.markdown("**Punkte-Regel:** 2 Rallyes in Folge gewinnen = 1 Punkt. Fördert die Konzentration nach langen Ballwechseln.")

        st.divider()

        st.subheader("TE 4: Ziel-Aufschlag")
        with st.expander("🏃‍♂️ 1. Warm-up: Reaktions-Sprints (10 Min)"):
            st.markdown("**Gemeinsam:** Spieler liegen auf dem Bauch am Netz. Auf Pfiff: Aufstehen, rückwärts bis 3m-Linie, vorwärts ans Netz hechten.")
        with st.expander("🎯 2. Technik: Zonen-Aufschlag (30 Min)"):
            st.markdown("**Gemeinsam:** Turnmatten in die Ecken des gegnerischen Feldes legen. Aufschläge von oben auf die Matten zielen (Punkte sammeln).")
        with st.expander("🧠 3. Taktik: Aufschlag-Rezeption (30 Min)"):
            st.markdown("**Split:** U14 schlägt gezielt in die Ecken auf, U13 muss die Lücken schließen und aufbauen.")
        with st.expander("🏆 4. Abschlussspiel: Aufschlag-König (20 Min)"):
            st.markdown("**Sonderregel:** Direktes Aufschlag-Ass führt zum direkten Seitenwechsel auf die 'Kaiser-Seite'.")

    # ---------------- WOCHE 3 ----------------
    with w3:
        st.info("Fokus Woche 3: Umschaltspiel (Transition) und Ermüdung.")
        st.subheader("TE 5: Transition-Offense")
        with st.expander("🏃‍♂️ 1. Warm-up: Ball-Klau (10 Min)"):
            st.markdown("**Gemeinsam:** Alle dribbeln einen Ball im 3m-Raum und versuchen, anderen die Bälle wegzuschlagen.")
        with st.expander("🎯 2. Technik: Abwehr-Zuspiel (30 Min)"):
            st.markdown("**Gemeinsam:** Trainer schlägt auf Zuspieler. Dieser wehrt ab. Ein Annahmespieler muss aushelfen und hoch zuspielen.")
        with st.expander("🧠 3. Taktik: Butterfly-Drill (30 Min)"):
            st.markdown("**Split:** Team A schlägt auf Team B auf. B greift an, A wehrt ab und baut Gegenangriff (Transition) auf.")
        with st.expander("🏆 4. Abschlussspiel: Dauer-Feuer (20 Min)"):
            st.markdown("**Trainer-Druck:** Sobald der Ball tot ist, wirft der Trainer in Sekundenschnelle den nächsten Ball ein. Keine Verschnaufpause.")

        st.divider()

        st.subheader("TE 6: Aufschlag unter Ermüdung")
        with st.expander("🏃‍♂️ 1. Warm-up: Block-Schatten (10 Min)"):
            st.markdown("**Gemeinsam:** Paare am Netz. Leader macht Sidesteps/Blocksprünge, Schatten folgt.")
        with st.expander("🎯 2. Technik: Sprint & Serve (30 Min)"):
            st.markdown("**Gemeinsam:** Spieler macht am Netz einen Blocksprung, sprintet rückwärts zur Grundlinie, bekommt Ball zugeworfen und muss sofort mit hohem Puls von oben aufschlagen.")
        with st.expander("🧠 3. Taktik: Rette das System (30 Min)"):
            st.markdown("**Split:** Trainer wirft absichtlich sehr schlechte Bälle (Netz, Aus, Hinterfeld) ein. Die Teams müssen den Ball retten und trotzdem über einen Angriff (!) abschließen.")
        with st.expander("🏆 4. Abschlussspiel: Joker-Turnier (20 Min)"):
            st.markdown("**Level Up:** Jedes Team hat 2 Joker-Karten. Einsatz verdoppelt die Punkte der nächsten Rallye.")

    # ---------------- WOCHE 4 ----------------
    with w4:
        st.success("Fokus Woche 4: Wettkampfhärte, Mini-Turniere und Coaching untereinander.")
        st.subheader("TE 7: Match-Simulation")
        with st.expander("🏃‍♂️ 1. Warm-up: Pre-Game Routine (15 Min)"):
            st.markdown("**Gemeinsam:** Offizielles Einspielen wie beim Spieltag. Einschlagen am Netz mit Block durch den Trainer.")
        with st.expander("🎯 2. Technik & Taktik: Systemprüfung (25 Min)"):
            st.markdown("**Mixed-Wellenprinzip:** Harte Aufschläge (U14/Trainer). Welle 1 hat 3 Sekunden für den perfekten Aufbau, Welle 2 hat 4 Sekunden. Fehler = Liegestütze für alle.")
        with st.expander("🏆 3. Abschlussspiel: TuB Bocholt Liga Hinrunde (50 Min)"):
            st.markdown("**Turnier:** Reines Wettkampfspiel. Wenn möglich, Feld längs teilen. Sonst 4v4, wobei U13 in die U14 integriert wird. Du bist Schiri, Spieler coachen sich selbst.")

        st.divider()

        st.subheader("TE 8: Finaltag")
        with st.expander("🏃‍♂️ 1. Warm-up: Kopfball-Volleyball (10 Min)"):
            st.markdown("**Gemeinsam:** Kurzes 2v2 über tiefes Netz. Ball darf nur per Kopf oder Fuß gespielt werden. Lockert die Stimmung für den Finaltag!")
        with st.expander("🧠 2. Taktik: Der Not-Aufschlag (20 Min)"):
            st.markdown("**Drucksituation:** 'Es steht 14:14 im 3. Satz'. Jeder Spieler muss 3 absolut fehlerfreie, leichte Aufschläge nacheinander übers Netz bringen. Bei Fehler: Vorne anfangen.")
        with st.expander("🏆 3. Abschlussspiel: TuB Bocholt Liga Rückrunde (60 Min)"):
            st.markdown("**Turnier:** Fortsetzung von TE 7. Das Sieger-Team bekommt am Ende ein kleines Belohnungsgetränk oder darf das Warm-Up am Dienstag leiten.")

# ---------------------------------------------------------
# MONAT 2 & 3 (PLATZHALTER FÜR 4 WOCHEN STRUKTUR)
# ---------------------------------------------------------
elif monat == "Monat 2: Angriff & Sicherung":
    st.header("Monat 2: Harter Angriff und Angriffs-Sicherung")
    w1, w2, w3, w4 = st.tabs(["Woche 1", "Woche 2", "Woche 3", "Woche 4"])
    
    with w1:
        st.info("Hier werden später die 8 TEs für Monat 2 eingefügt (z.B. Schlaghärte, Lob-Technik). Struktur ist identisch zu Monat 1.")
        # Platzhalter für die gleichen expander-Blöcke

elif monat == "Monat 3: Out-of-System & Match-Speed":
    st.header("Monat 3: Lösungen unter Stress")
    st.info("Auch hier: 4 Tabs für 4 Wochen mit jeweils TE 1 und TE 2. Fokus auf Chaos-Management und Freeball-Kill.")

elif monat == "System-Spezial: 3v3 meets 4v4":
    st.header("System-Spezial: Transition & Kognition")
    st.success("Tipp: Nutze diese Übungen immer dann, wenn du merkst, dass die Teams im regulären Training die Übersicht verlieren.")
    
    with st.expander("⏱️ 1. Der Transition-Läufer (U13 & U14) (15 Min)"):
        st.markdown("**Aus der Abwehr ins Zuspiel:** Trainer schlägt auf Zuspieler. Dieser wehrt ab, Mitspieler übernimmt das Not-Zuspiel.")
    with st.expander("👀 2. Das Scanner-Zuspiel (20 Min)"):
        st.markdown("**Block lesen:** Trainer am Netz hebt linke oder rechte Hand. Zuspieler pritscht dorthin, wo die Hand *unten* ist.")
    with st.expander("🏆 3. Spielform: Der Libero-Joker (20 Min)"):
        st.markdown("**3v3 mit Abwehr-Chef:** U13 spielt 3v3. Ein U14 Spieler steht hinten als Libero und darf eingreifen, wenn Bälle drohen ins Aus zu fallen.")
