import streamlit as st

# Seiten-Konfiguration
st.set_page_config(page_title="U13/U14 PRO Trainingsplan", page_icon="🏐", layout="centered")

st.title("🏐 U13/U14 Trainingsplan – TuB Bocholt")
st.markdown("Fokus: Grundlagenausbildung, Binnendifferenzierung (Einsteiger & Fortgeschrittene) | 1 Feld")

# Dynamische Navigation & Teilnehmersteuerung
col1, col2 = st.columns(2)
with col1:
    monat = st.selectbox(
        "Wähle den Trainingsmonat:", 
        [
            "Monat 1: Annahme-Plattform, Beinarbeit & Basis-Aufschlag", 
            "Monat 2: Angriff, Aufschlag & Basics-Integration", 
            "Monat 3: Out-of-System & Match-Speed",
            "System-Spezial: 3v3 meets 4v4"
        ]
    )
with col2:
    spieler = st.radio(
        "Anzahl anwesender Spieler:",
        ["9-12 Spieler (Wellen-/Gruppenprinzip)", "6-8 Spieler (Intensiv)"]
    )

st.divider()

# =========================================================
# MONAT 1 & 3 (PLATZHALTER FÜR ÜBERSICHTLICHKEIT)
# =========================================================
if monat == "Monat 1: Annahme-Plattform, Beinarbeit & Basis-Aufschlag":
    st.info("Monat 1 ist im System hinterlegt. Wechsle zu Monat 2 für die neuen, binnendifferenzierten 15-Minuten-Einheiten.")
elif monat == "Monat 3: Out-of-System & Match-Speed":
    st.info("Monat 3 ist im System hinterlegt.")
elif monat == "System-Spezial: 3v3 meets 4v4":
    st.info("System-Spezial ist im System hinterlegt.")

# =========================================================
# MONAT 2: GRUNDTECHNIK ANGRIFF, AUFSCHLAG & BASICS
# =========================================================
elif monat == "Monat 2: Angriff, Aufschlag & Basics-Integration":
    st.header("Monat 2: Schlagen über das Netz & Integration aller Leistungsstufen")
    
    w1, w2, w3, w4 = st.tabs(["Woche 1", "Woche 2", "Woche 3", "Woche 4"])
    
    # ---------------- WOCHE 1 ----------------
    with w1:
        st.subheader("TE 1 (90 Min): Armzug, Bagger-Basics & Stemmschritt")
        
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Ballgewöhnung & Linien-Drill"):
            st.markdown("""
            **Ablauf:** Kurze Linien-Tappings. Danach schnelles Zuwerfen des Balls in Paaren im Seitgalopp quer durch die Halle.
            * **🎯 Basis-Level (Einsteiger):** Ball beidhändig fangen und aus der tiefen Hocke zurückwerfen (Beinarbeit fokussieren).
            * **🚀 PRO-Level:** Ball darf nicht gefangen werden, sondern muss direkt im sauberen Bagger oder Pritsch zurückgespielt werden.
            """)
            
        with st.expander("🎯 2. Technik I (15 Min): Das Spielbrett & Bagger-Kontakt"):
            st.markdown("""
            **Ablauf:** 2er-Paare. Spieler A wirft den Ball, Spieler B baggert zurück. 
            * **🎯 Basis-Level:** Der Ball wird absichtlich leicht und im hohen Bogen genau auf die Arme geworfen. Einsteiger stoppen ab, pressen die Schultern zusammen und lassen den Ball nur vom "klatschenden Spielbrett" abprallen, ohne Schwung zu holen.
            * **🚀 PRO-Level:** Spieler A wirft flache, harte Bälle leicht seitlich. Spieler B muss einen schnellen Sidestep machen und den Ball kontrollieren.
            """)
            
        with st.expander("🎯 3. Technik II (15 Min): Pritschen-Grundhaltung"):
            st.markdown("""
            **Ablauf:** Paarweise am Netz. Zuspiel-Bewegung üben.
            * **🎯 Basis-Level:** Ball über der Stirn fangen (Hand-Dreieck kontrollieren, rechtes Bein vorne). Aus den Knien heraus den Ball hoch an die Antenne stoßen.
            * **🚀 PRO-Level:** Ball direkt und ohne Halten sauber aus den Fingern pritschen.
            """)
            
        with st.expander("🧠 4. Taktik I (15 Min): Wandschlag & Armzug (ohne Netz)"):
            st.markdown("""
            **Ablauf:** Spieler stehen vor einer freien Wand und üben die Schlagbewegung (Peitscheneffekt).
            * **🎯 Basis-Level:** Ball mit gestrecktem Arm anwerfen, fangen und Stand korrigieren. Erst wenn der Anwurf exakt vor der Schlagschulter ist, mit offener Hand gegen die Wand schlagen, sodass er vorher auf dem Boden aufkommt.
            * **🚀 PRO-Level:** Fließende Bewegung mit extrem hartem Handgelenks-Einsatz.
            """)
            
        with st.expander("🧠 5. Taktik II (15 Min): Stemmschritt am Netz"):
            st.markdown("""
            **Ablauf:** Der Stemmschritt wird direkt am Netz angewendet. Trainer wirft Bälle hoch auf Pos IV.
            * **🎯 Basis-Level:** Spielen den Stemmschritt ohne Ball über ein flaches Hindernis auf dem Boden, um den Rhythmus ("Schritt... hopp-stopp!") zu verinnerlichen.
            * **🚀 PRO-Level:** Führen den Stemmschritt mit anfliegendem Ball aus, springen hoch und schlagen über das Netz.
            """)
            
        with st.expander("🏆 6. Abschlussspiel (15 Min): Angriffs-Bingo (Mix-Teams)"):
            st.markdown("""
            **Ablauf:** 3v3 oder 4v4. Die Teams werden bewusst gemischt (stark + schwach). 
            * **🎯 Basis-Level:** Dürfen den 2. Ball (Zuspiel) fangen und spielen. Ihr Angriff darf ein gezielter Stand-Schlag oder Bagger sein.
            * **🚀 PRO-Level:** Dürfen Bälle nicht fangen. Ihr eigener Angriff muss zwingend gesprungen und hart geschlagen werden.
            """)

        st.divider()

        st.subheader("TE 2 - Freitag (120 Min): Aufschlag-Basics & System-Integration")
        
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Baggertennis (1v1 / 2v2)"):
            st.markdown("""
            **Ablauf:** Kleinfelder markieren.
            * **🎯 Basis-Level:** Der Ball darf 1x auf dem Boden aufkommen. Gefördert wird die Bewegung zum Ball.
            * **🚀 PRO-Level:** Direkter Volley-Modus. Ball darf nicht aufkommen.
            """)
            
        with st.expander("⚡ 2. Athletik (15 Min): Fußarbeit & Rumpf"):
            st.markdown("""
            **Ablauf:** Schnelle Linien-Drills (Tappings, Scheren-Sprünge) und Planks (Unterarmstütz).
            * **Trainer-Details:** Einsteiger konzentrieren sich auf saubere Ausführung der Planks (gerader Rücken), Fortgeschrittene heben abwechselnd Arm und Bein.
            """)
            
        with st.expander("🎯 3. Technik I (15 Min): Aufschlag-Progression"):
            st.markdown("""
            **Ablauf:** Aufschlag-Training in Reihen. 
            * **🎯 Basis-Level:** Pendel-Aufschlag von unten ab der 4,50m- oder 6m-Linie. Ball liegt auf der flachen Hand, wird *nicht* hochgeworfen, sondern direkt mit dem Pendelarm sicher rübergeschlagen.
            * **🚀 PRO-Level:** Tennis-Aufschlag von oben von der Grundlinie mit flacher Flugkurve.
            """)
            
        with st.expander("🎯 4. Technik II (15 Min): Annahme der Aufschläge"):
            st.markdown("""
            **Ablauf:** Spieler auf der Gegenseite nehmen die Aufschläge aus Übung 3 an.
            * **🎯 Basis-Level:** Positionieren sich rechtzeitig, frieren ein und fangen den Ball in der tiefen Abwehrhaltung.
            * **🚀 PRO-Level:** Baggern den Aufschlag exakt in den Zielkreis auf Position III.
            """)
            
        with st.expander("🧠 5. Taktik I (15 Min): Der Systemaufbau (Pos I -> III -> IV)"):
            st.markdown("""
            **Ablauf:** Dankeball vom Trainer wird im 3er-Riegel angenommen, zugespielt und angegriffen.
            * **🎯 Basis-Level:** Der Zuspieler auf Pos III fängt die Annahme, richtet die Schulterachse zu Pos IV aus und wirft den Ball im hohen Bogen zum Angreifer.
            * **🚀 PRO-Level:** Der Zuspieler pritscht den Ball fließend (ggf. im Sprung) zu Pos IV.
            """)
            
        with st.expander("🧠 6. Taktik II (15 Min): Freeball-Kill"):
            st.markdown("""
            **Ablauf:** Ball wird über das Netz geworfen.
            * **🎯 Basis-Level:** Einsteiger fokussieren sich auf den lauten Ruf ("Ich!") und den ersten sauberen Bagger zur Mitte.
            * **🚀 PRO-Level:** Erfahrene Spieler fokussieren sich auf den sofortigen Stemmschritt-Anlauf, sobald der Ball ihren Zuspieler verlässt.
            """)
            
        with st.expander("🧠 7. Taktik III (15 Min): Blocksicherung (Am Boden)"):
            st.markdown("""
            **Ablauf:** Trainer schlägt hart gegen eine Matte am Netz (simulierter Block-Abpraller).
            * **🎯 Basis-Level:** Spieler werfen sich auf den Boden (Hechtbagger-Gleiten aus dem Kniestand) und fangen den Ball.
            * **🚀 PRO-Level:** Spieler stehen in tiefer Ready-Position, rutschen blitzschnell unter den Ball und kratzen ihn einarmig hoch.
            """)
            
        with st.expander("🏆 8. Abschlussspiel (15 Min): Handicap-Match"):
            st.markdown("""
            **Ablauf:** 3v3 oder 4v4. 
            * **🎯 Basis-Level:** Dürfen ihre Angaben von der 6m-Linie von unten machen.
            * **🚀 PRO-Level:** Dürfen nur ins hintere Felddrittel (Pos 1, 5, 6) angreifen. Wenn sie ins Netz aufschlagen, gibt es Minuspunkt.
            """)

    # ---------------- WOCHE 2 ----------------
    with w2:
        st.subheader("TE 3 (90 Min): Härte, Abwehr & Zuspiel")
        
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Ball-Handling-Staffel"):
            st.markdown("""
            **Ablauf:** Staffel mit Dribbeln und Richtungswechseln.
            * **🎯 Basis-Level:** Normaler Vorwärtslauf durch den Parcours.
            * **🚀 PRO-Level:** Müssen die Staffel rückwärts dribbelnd absolvieren.
            """)
            
        with st.expander("🎯 2. Technik I (15 Min): Schlaghärte gegen Matte"):
            st.markdown("""
            **Ablauf:** Spieler schlagen Bälle aus dem Stand mit maximaler Härte senkrecht auf eine Matte.
            * **🎯 Basis-Level:** Werfen den Ball mit beiden Händen auf die Matte (Bogenspannung üben).
            * **🚀 PRO-Level:** Harter, einarmiger Peitschenschlag mit aktivem Handgelenk.
            """)
            
        with st.expander("🎯 3. Technik II (15 Min): Zuspiel aus der Bewegung"):
            st.markdown("""
            **Ablauf:** Zuspieler pendelt zwischen Netz und Pos 3.
            * **🎯 Basis-Level:** Läuft ein, fängt den Ball über der Stirn, stabilisiert den Stand.
            * **🚀 PRO-Level:** Läuft ein und pritscht den Ball direkt aus der Bewegung ohne Fangen weiter.
            """)
            
        with st.expander("🧠 4. Taktik I (15 Min): Schmetter-Abwehr"):
            st.markdown("""
            **Ablauf:** Trainer schlägt gezielt von Kästen auf Abwehrspieler an.
            * **🎯 Basis-Level:** Arme ruhig hinhalten, Ball nur abprallen lassen. Kein Wegziehen, keine Angst vor dem Ball!
            * **🚀 PRO-Level:** Harte Schläge kontrolliert auf eine Zielhöhe von 3 Metern in die Feldmitte dämpfen.
            """)
            
        with st.expander("🧠 5. Taktik II (15 Min): System-Integration (Live)"):
            st.markdown("""
            **Ablauf:** Komplette Kette vom Aufschlag bis zum Angriff.
            * **Trainer-Details:** Jeder Spieler bekommt eine auf sein Niveau zugeschnittene Aufgabe (z. B. Einsteiger = sicherer erster Bagger, PRO = harter Abschluss).
            """)
            
        with st.expander("🏆 6. Abschlussspiel (15 Min): Wash-Game (2 Rallyes)"):
            st.markdown("""
            **Ablauf:** 2 gewonnene Ballwechsel in Folge geben 1 Punkt. 
            * Einsteiger-Fehler beim Aufschlag werden ignoriert (sie dürfen sofort wiederholen), um den Spielfluss für alle zu erhalten.
            """)

        st.divider()

        st.subheader("TE 4 - Freitag (120 Min): Aufschlagdruck & Block")
        
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Hechten & Block-Schatten"):
            st.markdown("""
            **Ablauf:** Blocksprung am Netz, landen, rückwärts ausweichen, Abwehrhecht.
            * **🎯 Basis-Level:** Hecht-Gleiten aus dem Kniestand (flach abrutschen).
            * **🚀 PRO-Level:** Hechtbagger aus dem vollen Lauf.
            """)
            
        with st.expander("⚡ 2. Athletik (15 Min): Sprung & Schulter"):
            st.markdown("""
            **Ablauf:** Medizinball-Würfe über das Netz und seitliche Block-Sprünge.
            """)
            
        with st.expander("🎯 3. Technik I (15 Min): Zonen-Aufschlag"):
            st.markdown("""
            **Ablauf:** Aufschläge auf Turnmatten.
            * **🎯 Basis-Level:** Von unten von der 6m-Linie. Ziel ist das sichere Treffen der großen Mattenfläche.
            * **🚀 PRO-Level:** Von oben von der Grundlinie. Matten werden halbiert (Ziel wird kleiner).
            """)
            
        with st.expander("🎯 4. Technik II (15 Min): Der 1er- und 2er-Block"):
            st.markdown("""
            **Ablauf:** Timing beim Absprung am Netz, Hände übergreifen.
            * **🎯 Basis-Level:** Fokus liegt auf dem zeitgleichen, beidbeinigen Absprung ohne Netzberührung.
            * **🚀 PRO-Level:** Hände aktiv über das Netz schieben und Handgelenke starr machen.
            """)
            
        with st.expander("🧠 5. Taktik I (15 Min): Lobs erlaufen"):
            st.markdown("""
            **Ablauf:** Trainer tippt Bälle kurz hinter den Block.
            * **🎯 Basis-Level:** Schneller Antritt, Ball vor dem Boden fangen.
            * **🚀 PRO-Level:** Ball aus dem tiefen Lauf heraus einarmig kratzen.
            """)
            
        with st.expander("🧠 6. Taktik II (15 Min): Out-of-System Notpass"):
            st.markdown("""
            **Ablauf:** Ball fliegt ins Aus. Spieler ruft 'Hilfe'.
            * **🎯 Basis-Level:** Notpass wird als hoher Bagger sicher über das Netz gespielt.
            * **🚀 PRO-Level:** Notpass wird hoch an die Antenne gelegt, Mitspieler greift aus dem Hinterfeld an.
            """)
            
        with st.expander("🧠 7. Taktik III (15 Min): Block-Abwehr Dreieck"):
            st.markdown("""
            **Ablauf:** U14 stellt Block, Abwehr positioniert sich V-förmig dahinter.
            * **Trainer-Details:** Einsteiger sichern die leichten Abpraller im Raum, Profis erlaufen die schnellen diagonalen Linien-Schläge.
            """)
            
        with st.expander("🏆 8. Abschlussspiel (15 Min): Block-König"):
            st.markdown("""
            **Ablauf:** 3v3 / 4v4. 
            * **Punkte-Regel:** Kill-Blocks oder gerettete Lobs zählen doppelt. Aufschläge für Einsteiger ab der 6m-Linie.
            """)
            
    with w3:
        st.info("Woche 3 vertieft die Angriffs-Technik am Netz und integriert die Fehlerkompensation.")
    with w4:
        st.info("Woche 4 bereitet auf den Match-Day vor (Max. 15-Minuten-Einheiten).")
