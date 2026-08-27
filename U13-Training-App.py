import streamlit as st

# Seiten-Konfiguration
st.set_page_config(page_title="U13/U14 Trainingsplan", page_icon="🏐", layout="centered")

st.title("🏐 U13/U14 PRO Plan")
st.markdown("TuB Bocholt | 2x Training pro Woche (8 TE pro Monat)")

# Navigation - Monat
monat = st.selectbox(
    "Wähle den Trainingsmonat:", 
    [
        "Monat 1: Annahme-Präzision & System-Start", 
        "Monat 2: Grundtechnik Angriff & Aufschlag", 
        "Monat 3: Out-of-System & Match-Speed",
        "System-Spezial: 3v3 meets 4v4"
    ]
)

# ---------------------------------------------------------
# MONAT 1: Annahme & System (VOLLSTÄNDIG - 4 Wochen / 8 TE)
# ---------------------------------------------------------
if monat == "Monat 1: Annahme-Präzision & System-Start":
    st.header("Monat 1: Gezielte Annahme zum Steller")
    
    w1, w2, w3, w4 = st.tabs(["Woche 1", "Woche 2", "Woche 3", "Woche 4"])
    
    # ---------------- WOCHE 1 (Annahme Grundlagen) ----------------
    with w1:
        st.subheader("TE 1: Das sichere Spielbrett")
        with st.expander("🏃‍♂️ 1. Warm-up: Reaktions-Baggern (10 Min)"):
            st.markdown("**Gemeinsam:** Paarweise. Spieler A wirft den Ball leicht links oder rechts. Spieler B muss einen schnellen Sidestep machen, das Spielbrett formen und den Ball sauber zurückbaggern.")
        with st.expander("🎯 2. Technik: Ziel-Baggern zum Steller (30 Min)"):
            st.markdown("**Gemeinsam:** Ein Kasten oder Reifen wird auf Position II/III (Steller-Position) platziert. Trainer wirft Bälle von der Gegenseite an. Die Spieler müssen den Winkel ihrer Arme so anpassen, dass der Ball im hohen Bogen genau auf das Ziel (den Steller) fällt.")
        with st.expander("🧠 3. Taktik: Annahme-Riegel formieren (30 Min)"):
            st.markdown("**Split:** Seite A (U14 - 3er Annahmeriegel), Seite B (U13 - 2er Annahmeriegel). Trainer schlägt leichte Aufschläge ein. Fokus: Wer nimmt welchen Ball? Lautes Rufen ('Ich!') und sauberer Pass zum designierten Zuspieler, der den Ball nur fängt.")
        with st.expander("🏆 4. Abschlussspiel: Annahme-Bingo (20 Min)"):
            st.markdown("**Punkte-Regel:** 3v3 / 4v4. Ein Punkt zählt normal. Aber: Landet die Annahme perfekt beim Zuspieler (ohne dass dieser laufen muss), gibt es einen Zusatzpunkt!")

        st.divider()

        st.subheader("TE 2: Annahme unter Druck")
        with st.expander("🏃‍♂️ 1. Warm-up: Tiefe Abwehr (10 Min)"):
            st.markdown("**Gemeinsam:** Linienfangen auf dem ganzen Feld. Alle müssen sich in der tiefen Abwehrhaltung (Knie gebeugt, Arme bereit) bewegen.")
        with st.expander("🎯 2. Technik: Dankeball-Sprint & Annahme (30 Min)"):
            st.markdown("**Gemeinsam:** Spieler startet an der Grundlinie. Trainer ruft 'Go!' und wirft kurz hinter das Netz. Spieler sprintet, stoppt komplett ab (!) und baggert den Ball hoch zum wartenden Steller.")
        with st.expander("🧠 3. Taktik: Serve & Pass (30 Min)"):
            st.markdown("**Split:** U14 schlägt von oben auf (oder Trainer). U13 muss die harten Aufschläge kontrollieren. Fokus: Bei harten Bällen keine Arm-Bewegung beim Baggern, nur den Ball vom Spielbrett abprallen lassen!")
        with st.expander("🏆 4. Abschlussspiel: Handicap-Match (20 Min)"):
            st.markdown("**4v3:** U14 gegen U13. Wenn die Annahme der U13 zu unsauber wird, darf die U14 nur noch von unten aufschlagen, um den Fokus auf den sauberen Aufbau zurückzuholen.")

    # ---------------- WOCHE 2 (System-Start) ----------------
    with w2:
        st.subheader("TE 3: Zuspieler-Integration")
        with st.expander("🏃‍♂️ 1. Warm-up: Kognitives Chaos (10 Min)"):
            st.markdown("**Gemeinsam:** Paarweise am Netz. A pritscht Ball 1, B rollt Ball 2. Auf Pfiff: Sprint zur Grundlinie und zurück.")
        with st.expander("🎯 2. Technik: Annahme + Zuspiel (30 Min)"):
            st.markdown("**Gemeinsam (Wellenprinzip):** Annahme baggert zum Steller. Der Steller (muss aus der Bewegung abstoppen) pritscht den Ball hoch auf Position IV in einen Ballwagen/Korb.")
        with st.expander("🧠 3. Taktik: Mixed-System Laufwege (30 Min)"):
            st.markdown("**Split:** Seite A (U14 Rauten-System), Seite B (U13 Läufersystem). Trainer wirft Bälle ein. Der Steller muss einlaufen. Fokus auf das Timing: Steller läuft erst los, wenn der Ball den Trainer verlässt.")
        with st.expander("🏆 4. Abschlussspiel: Wash-Game (20 Min)"):
            st.markdown("**Punkte-Regel:** 2 Rallyes in Folge gewinnen = 1 Punkt. Fördert die Konzentration nach langen Ballwechseln.")

        st.divider()

        st.subheader("TE 4: System-Festigung")
        with st.expander("🏃‍♂️ 1. Warm-up: Aufschlag-Staffel (10 Min)"):
            st.markdown("**Gemeinsam:** Sprint zum Netz, Ball nehmen, Anwurf für Tennis-Aufschlag simulieren, fangen, Sprint zurück.")
        with st.expander("🎯 2. Technik: Zonen-Aufschlag vs. Annahme (30 Min)"):
            st.markdown("**Gemeinsam:** U14 übt gezielte Aufschläge auf Turnmatten. U13 steht in der Annahme und versucht, die Matten zu verteidigen und den Ball zum Steller abzufälschen.")
        with st.expander("🧠 3. Taktik: Rette das System (30 Min)"):
            st.markdown("**Split:** Trainer wirft absichtlich sehr schlechte Bälle (ans Netz, ins Aus) ein. Annahme ist unsauber. Ein anderer Spieler muss 'Hilfe' rufen und das Zuspiel übernehmen (Out-of-System).")
        with st.expander("🏆 4. Abschlussspiel: System-Kaiser (20 Min)"):
            st.markdown("**Sonderregel:** Herausforderer dürfen nur auf die Kaiser-Seite wechseln, wenn der letzte Ball über den Zuspieler (im System) gespielt wurde.")

    # ---------------- WOCHE 3 & 4 (Platzhalter für den Fokus Annahme/System) ----------------
    with w3:
        st.info("Woche 3: Fokus auf Aufschlag-Annahme Komplex und Transition (Umschalten von Abwehr auf Annahme).")
    with w4:
        st.success("Woche 4: Wettkampfhärte, Match-Simulation und TuB Bocholt Liga (Viel 3v3 und 4v4 spielen).")

# ---------------------------------------------------------
# MONAT 2: Grundtechnik Angriff & Aufschlag (Schlagen)
# ---------------------------------------------------------
elif monat == "Monat 2: Grundtechnik Angriff & Aufschlag":
    st.header("Monat 2: Schlagen über das Netz")
    
    w1, w2, w3, w4 = st.tabs(["Woche 1", "Woche 2", "Woche 3", "Woche 4"])
    
    # ---------------- WOCHE 1 (Angriffsschlag Basics) ----------------
    with w1:
        st.subheader("TE 1: Der Armzug")
        with st.expander("🏃‍♂️ 1. Warm-up: Schulter-Aktivierung (10 Min)"):
            st.markdown("**Gemeinsam:** Paarweises Zuwerfen wie beim Baseball (einarmig). Fokus auf Aufdrehen der Schulterachse und den Peitschenschlag des Arms.")
        with st.expander("🎯 2. Technik: Wand-Schlagen (30 Min)"):
            st.markdown("**Gemeinsam (Trockenübung):** Spieler stehen vor einer Wand. Ball in der linken Hand (bei Rechtshändern) hochhalten. Der rechte Ellenbogen ist hoch (Bogen-Spannung). Ball schlagen, Handgelenk klappt ab, Ball tippt vor der Wand auf den Boden.")
        with st.expander("🧠 3. Taktik/Technik: Schlagen aus dem Stand (30 Min)"):
            st.markdown("**Gemeinsam am Netz:** Trainer steht mit Ballwagen auf Pos III und wirft perfekte Bälle auf Pos IV. Spieler stehen an der 3m-Linie, machen EINEN Schritt (Stemmschritt) und schlagen den Ball mit hartem Handgelenk-Einsatz über das Netz. (Netz für U13 ggf. etwas tiefer hängen).")
        with st.expander("🏆 4. Abschlussspiel: Angriffs-Bingo (20 Min)"):
            st.markdown("**Punkte-Regel:** 3v3/4v4. Ein Punkt zählt nur, wenn der Ball über das Netz 'geschlagen' (oder aggressiv von oben gepritscht) wurde. Bagger-Bälle über das Netz geben keinen Punkt.")

        st.divider()

        st.subheader("TE 2: Der Anlauf (3er-Rhythmus)")
        with st.expander("🏃‍♂️ 1. Warm-up: Rhythmus-Sprints (10 Min)"):
            st.markdown("**Gemeinsam:** Alle stehen an der Grundlinie. Trainer klatscht den Rhythmus: 'Links... Rechts-Links!'. Spieler machen den Anlauf trocken und springen explosiv hoch.")
        with st.expander("🎯 2. Technik: Anlauf und Fangen (30 Min)"):
            st.markdown("**Gemeinsam:** Trainer steht auf einem Kasten am Netz. Spieler starten an der 3m-Linie, machen den 3er-Rhythmus, springen ab und *fangen* den Ball des Trainers am höchsten Punkt mit ausgestreckten Armen (Beide Arme müssen beim Absprung schwungvoll mit nach oben gerissen werden!).")
        with st.expander("🧠 3. Taktik: Anlauf und Schlagen (30 Min)"):
            st.markdown("**Split (U13/U14):** Gleicher Aufbau wie eben. Trainer wirft den Ball. Die Spieler machen den kompletten Anlauf und schlagen den Ball über das Netz. U14 fokussiert sich auf Härte, U13 auf das korrekte Timing beim Absprung.")
        with st.expander("🏆 4. Abschlussspiel: Hit or Lob (20 Min)"):
            st.markdown("**Entscheidung:** Trainer hebt beim Angriff heimlich die Hand (Block) oder nicht. Hand oben = Sanfter Lob gefordert. Hand unten = Harter Schlag gefordert.")

    # ---------------- WOCHE 2 (Aufschlag von oben) ----------------
    with w2:
        st.subheader("TE 3: Aufschlag-Härte")
        with st.expander("🏃‍♂️ 1. Warm-up: Hechten & Block-Schatten (10 Min)"):
            st.markdown("**Gemeinsam:** Auf Pfiff: Blocksprung am Netz, landen, rückwärts ausweichen, auf den Bauch hechten, schnell aufstehen.")
        with st.expander("🎯 2. Technik: Tennis-Aufschlag (30 Min)"):
            st.markdown("**Gemeinsam:** Aufschlag von oben von der 3m-Linie über das Netz. Fokus: Der Anwurf muss vor dem Körper (Schlagarm) und hoch genug sein. Wer 3 am Stück schafft, geht einen Meter zurück. U14 arbeitet sich zur Grundlinie vor.")
        with st.expander("🧠 3. Taktik: Aufschlag vs. Riegel (30 Min)"):
            st.markdown("**Split:** Team A schlägt hart von oben auf. Team B muss die schwere Annahme kontrollieren und auf den Steller bringen. Nach 5 Bällen Wechsel.")
        with st.expander("🏆 4. Abschlussspiel: Aufschlag-Kaiser (20 Min)"):
            st.markdown("**Direkter As-Wechsel:** Kaiserplatz. Schafft ein Team ein direktes Aufschlag-Ass, rückt es sofort auf die Kaiser-Seite vor.")

        st.divider()

        st.subheader("TE 4: Komplex-Training (Annahme + Schlag)")
        with st.expander("🏃‍♂️ 1. Warm-up: Reaktions-Baggern (10 Min)"):
            st.markdown("**Gemeinsam:** Wie in Woche 1: Schnelle Sidesteps und stabiles Spielbrett formen.")
        with st.expander("🎯 2. Technik: Freeball-Kill (30 Min)"):
            st.markdown("**Gemeinsam:** Trainer schlägt einen leichten Dankeball ein. Annahme zum Steller -> Steller pritscht hoch -> Angreifer macht 3er-Rhythmus und schlägt. (Kein Fangen mehr, alles flüssig!).")
        with st.expander("🧠 3. Taktik: Angriffssicherung (30 Min)"):
            st.markdown("**Split:** 3v3 und 4v4. Ein Team greift an, das andere stellt einen starren Doppelblock (Kasten). Der Angreifer schlägt absichtlich in den Block, die eigene Mannschaft muss in tiefer Haltung den Abpraller (Sicherung) hochkratzen.")
        with st.expander("🏆 4. Abschlussspiel: Wash-Game (20 Min)"):
            st.markdown("**Turnier-Modus:** 2 Rallyes am Stück gewinnen. Voller Einsatz in Angriff und Abwehr gefordert.")

    # ---------------- WOCHE 3 & 4 (Platzhalter) ----------------
    with w3:
        st.info("Woche 3: Fokus auf Timing bei unsauberen Pässen und harte Abwehr (Schmetter-Abwehr).")
    with w4:
        st.success("Woche 4: Spielintelligenz. Lobs vs. harte Schläge unter Wettkampfbedingungen.")

# ---------------------------------------------------------
# MONAT 3 & SYSTEM-SPEZIAL (Wie gehabt)
# ---------------------------------------------------------
elif monat == "Monat 3: Out-of-System & Match-Speed":
    st.header("Monat 3: Lösungen unter Stress")
    st.info("Hier: 4 Tabs für 4 Wochen mit jeweils TE 1 und TE 2. Fokus auf Chaos-Management, Transition und Freeball-Kill.")

elif monat == "System-Spezial: 3v3 meets 4v4":
    st.header("System-Spezial: Transition & Kognition")
    st.success("Tipp: Nutze diese Übungen immer dann, wenn du merkst, dass die Teams im regulären Training die Übersicht verlieren.")
    
    with st.expander("⏱️ 1. Der Transition-Läufer (U13 & U14) (15 Min)"):
        st.markdown("**Aus der Abwehr ins Zuspiel:** Trainer schlägt auf Zuspieler. Dieser wehrt ab, Mitspieler übernimmt das Not-Zuspiel.")
    with st.expander("👀 2. Das Scanner-Zuspiel (20 Min)"):
        st.markdown("**Block lesen:** Trainer am Netz hebt linke oder rechte Hand. Zuspieler pritscht dorthin, wo die Hand *unten* ist.")
    with st.expander("🏆 3. Spielform: Der Libero-Joker (20 Min)"):
        st.markdown("**3v3 mit Abwehr-Chef:** U13 spielt 3v3. Ein U14 Spieler steht hinten als Libero und darf eingreifen, wenn Bälle drohen ins Aus zu fallen.")
