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
        st.subheader("TE 3 - Mittwoch (90 Min): Games Approach – Fokus Spielpraxis")
        st.markdown("**Organisation:** U13 & U14 gemischt auf einem Feld. Fokus auf Positionen I bis IV.")

        with st.expander("🎾 1. Warm-up (15 Min): 1v1 Kreatives Volley-Tennis"):
            st.markdown("""
            **Organisation:** Das Spielfeld in schmale "Schläuche" unterteilen.
            **Ablauf:** 
            * Die Spieler spielen 1-gegen-1. 
            * Der Ball darf pro Spielzug exakt ein Mal auf dem eigenen Feld aufkommen. 
            * Es sind alle Ballberührungen (auch Fuß oder Kopf) erlaubt.
            **Ziel:** Garantiert maximale Ballkontakte für jeden Einzelnen vom ersten Moment an und schult die periphere Sicht.
            """)

        with st.expander("👑 2. Spielnaher Drill (20 Min): Kaiserplatz im Wellenprinzip"):
            st.markdown("""
            **Organisation:** 3v3 (Pos I, III, IV) oder 4v4 (Pos I, II, III, IV). Eine Seite ist die "Kaiserseite", auf der anderen warten die Herausforderer.
            **Ablauf:** 
            * Der Trainer wirft den Ball in extrem hoher Frequenz bei den Herausforderern ein. 
            * Punkten sie, wechseln sie jubelnd unter dem Netz durch auf die Kaiserseite. 
            * Punktet die Kaiserseite, rückt sofort das nächste Herausforderer-Team nach.
            **Ziel:** Das Wellenprinzip verhindert Warteschlangen und zwingt die Kinder durch den schnellen Einwurf zu pausenloser Aufmerksamkeit.
            """)

        with st.expander("🎯 3. System-Spielform (25 Min): Zusatzpunkt-Spiel (Läufer-Bingo)"):
            st.markdown("""
            **Organisation:** Normales 3v3 / 4v4 Match auf Zeit (z. B. 4 Minuten pro Runde).
            **Ablauf:** 
            * Es wird frei gegeneinander gespielt. Einen normalen Punkt gibt es für einen Fehler des Gegners. 
            * Einen **Zusatzpunkt** (bzw. "Bingo") gibt es, wenn der Punkt durch einen sauberen 3er-Aufbau über den Zuspieler auf Position III erzielt wird.
            **Ziel:** Die Spieler werden taktisch belohnt, das erlernte System in der echten Spielpraxis anzuwenden, anstatt den Ball unkontrolliert "rüberzuretten".
            """)

        with st.expander("🦸‍♂️️ 4. Abschluss-Event (30 Min): Das Superkraft-Turnier"):
            st.markdown("""
            **Organisation:** U13- und U14-Spieler werden bunt durchgemischt; gespielt wird ein Jeder-gegen-Jeden-Kurzturnier.
            **Ablauf:** 
            * Jedes Team erhält laminierte "Superkraft-Karten", die einmal pro Match durch lautes Rufen vor dem Aufschlag aktiviert werden können. 
            * Beispiele: "Gummi-Wand" (Team darf den Ball viermal berühren) oder "Bodenhaftung" (Gegner darf in diesem Ballwechsel nicht abspringen).
            **Ziel:** Purer Spielspaß am Ende der Einheit. Die Gamification nimmt den Stress aus der Wettkampfsituation und stärkt den Teamgeist.
            """)

        st.divider()

        st.subheader("TE 4 - Freitag (120 Min): System-Festigung")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Aufschlag-Staffel"):
            st.markdown("""
            **Ablauf:** Staffel mit Ball prellen und Anwurf-Simulation am Netz.
            **Trainer-Details:** Ball muss vor der Schlag-Schulter angeworfen werden.
            """)
        with st.expander("🎯 2. Technik I (15 Min): Zonen-Aufschlag"):
            st.markdown("""
            **Ablauf:** U14 schlägt gezielt auf Turnmatten in den Ecken.
            **Trainer-Details:** Handgelenk muss abklappen für den nötigen Druck.
            """)
        with st.expander("🎯 3. Technik II (15 Min): Annahme-Verschiebung"):
            st.markdown("""
            **Ablauf:** Aufschläger wechselt permanent die Position (Mitte, Seite). Annahmeriegel muss rotieren.
            **Trainer-Details:** Den Kreuzwinkel abdecken!
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Rette das System (Trocken)"):
            st.markdown("""
            **Ablauf:** Trainer wirft Ball absichtlich ins Aus. Spieler rufen 'Hilfe' und fangen den Ball.
            **Trainer-Details:** Es geht rein um die auditive Kommunikation (wer ruft?).
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Rette das System (Live)"):
            st.markdown("""
            **Ablauf:** Notzuspiel aus dem Chaos (Out-of-System) zum Angreifer.
            **Trainer-Details:** Der Notpass muss hoch an die Antenne gespielt werden, damit der Angreifer Zeit hat.
            """)
        with st.expander("⚡ 6. Athletik I (15 Min): Quickness & Leiter"):
            st.markdown("""
            **Ablauf:** Koordinationsleiter für schnelle Fußarbeit.
            **Trainer-Details:** Fersen bleiben in der Luft (Vorfuß-Lauf).
            """)
        with st.expander("⚡ 7. Athletik II (10 Min): Core-Rotation"):
            st.markdown("""
            **Ablauf:** Medizinball-Würfe (seitlich).
            **Trainer-Details:** Imitiert die Rumpf-Rotation beim Schlag.
            """)
        with st.expander("🏆 8. Abschlussspiel (20 Min): System-Kaiser"):
            st.markdown("""
            **Ablauf:** Herausforderer rücken nur bei 3er-System-Aufbau auf die Kaiserseite.
            **Trainer-Details:** Lobe auch den Versuch, wenn der finale Ball im Aus landet!
            """)
            
    with w3:
        st.info("Woche 3 vertieft die Angriffs-Technik am Netz und integriert die Fehlerkompensation.")
    with w4:
        st.info("Woche 4 bereitet auf den Match-Day vor (Max. 15-Minuten-Einheiten).")
