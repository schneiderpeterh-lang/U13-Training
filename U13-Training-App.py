import streamlit as st

# Seiten-Konfiguration
st.set_page_config(page_title="U13/U14 Trainingsplan", page_icon="🏐", layout="centered")

st.title("🏐 U13/U14 PRO Plan")
st.markdown("TuB Bocholt | Max. 15 Min pro Übung (Hohe Taktung)")

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
# MONAT 1: Annahme & System (15-Minuten-Raster)
# ---------------------------------------------------------
if monat == "Monat 1: Annahme-Präzision & System-Start":
    st.header("Monat 1: Gezielte Annahme zum Steller")
    
    w1, w2, w3, w4 = st.tabs(["Woche 1", "Woche 2", "Woche 3", "Woche 4"])
    
    # ---------------- WOCHE 1 ----------------
    with w1:
        st.subheader("TE 1 (90 Min): Das sichere Spielbrett")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Reaktions-Baggern"):
            st.markdown("""
            **Ablauf:** Paarweise. Spieler A wirft leicht seitlich. Spieler B macht schnellen Sidestep, formt das Spielbrett und baggert präzise zurück.
            **Trainer-Details:** Achte strikt darauf, dass die Beinarbeit *vor* der Armarbeit passiert!
            """)
        with st.expander("🎯 2. Technik I (15 Min): Ziel-Baggern aus dem Stand"):
            st.markdown("""
            **Ablauf:** Kasten auf Pos II/III. Trainer wirft Bälle zentral an. Ball im hohen Bogen auf das Ziel baggern.
            **Trainer-Details:** Stell dich genau hinter den Kasten. Die Schulterachse der Spieler muss zu dir zeigen.
            """)
        with st.expander("🎯 3. Technik II (15 Min): Ziel-Baggern aus Bewegung"):
            st.markdown("""
            **Ablauf:** Wie zuvor, aber der Trainer wirft die Bälle nun in die Lücken (kurz, lang, seitlich). Spieler muss den Ball erlaufen, abstoppen und zum Kasten spielen.
            **Trainer-Details:** Der Bremsweg ist entscheidend. Wer beim Baggern noch läuft, spielt unpräzise.
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Annahme-Riegel formieren"):
            st.markdown("""
            **Ablauf:** U14 (3er Riegel), U13 (2er Riegel). Trainer wirft leichte Bälle ein. Fokus: Lautes Rufen ('Ich!').
            **Trainer-Details:** Wer zuerst 'Ich' ruft, hat Vorfahrt. Zögern abpfeifen.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Pass zum Steller"):
            st.markdown("""
            **Ablauf:** Aufbauend auf Übung 4. Der Ball wird nun nach dem 'Ich'-Ruf gezielt zum einlaufenden Steller gebaggert (dieser fängt den Ball über Kopf).
            **Trainer-Details:** Der Steller muss lernen, den Ball lautstark einzufordern ('Zu mir!').
            """)
        with st.expander("🏆 6. Abschlussspiel (20 Min): Annahme-Bingo"):
            st.markdown("""
            **Ablauf:** 3v3/4v4. Zusatzpunkt, wenn die Annahme perfekt beim Zuspieler landet.
            **Trainer-Details:** Werte streng: Musste der Zuspieler mehr als einen Schritt machen, gibt es keinen Zusatzpunkt.
            """)

        st.divider()

        st.subheader("TE 2 - Freitag (120 Min): Annahme unter Druck")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Tiefe Abwehr & Linien-Chaos"):
            st.markdown("""
            **Ablauf:** Linienfangen mit tiefem Abwehr-Stopp auf Pfiff.
            **Trainer-Details:** Fordere die 'Ready-Position': Knie gebeugt, Gewicht auf dem Vorfuß.
            """)
        with st.expander("🎯 2. Technik I (15 Min): Dankeball-Sprint"):
            st.markdown("""
            **Ablauf:** Spieler an der Grundlinie. Trainer ruft 'Go!', wirft Ball ans Netz. Sprint, abstoppen, baggern.
            **Trainer-Details:** Härte im Antritt fordern!
            """)
        with st.expander("🎯 3. Technik II (15 Min): Harte Bälle absorbieren"):
            st.markdown("""
            **Ablauf:** Trainer schlägt hart von einem Kasten auf die Spieler. Arme nur hinhalten, Ball abprallen lassen.
            **Trainer-Details:** Keine Schwungbewegung! Der Bagger agiert nur als Wand.
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Serve & Pass (Leicht)"):
            st.markdown("""
            **Ablauf:** U14 schlägt von unten auf U13 auf (und umgekehrt). Fokus auf den ruhigen Annahme-Aufbau zum Steller.
            **Trainer-Details:** Laufwege überprüfen.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Serve & Pass (Schwer)"):
            st.markdown("""
            **Ablauf:** Harte Aufschläge von oben. Der Riegel muss dem Druck standhalten.
            **Trainer-Details:** Steh hinter der Annahme. Verschieben sie den Riegel richtig?
            """)
        with st.expander("⚡ 6. Athletik I (15 Min): Rumpf- & Sprungkraft"):
            st.markdown("""
            **Ablauf:** 3 Runden Zirkel (Plank, Ausfallschritte, Blocksprünge).
            **Trainer-Details:** Achte bei der Plank auf einen geraden Rücken.
            """)
        with st.expander("⚡ 7. Athletik II (10 Min): Puls-Aufschlag"):
            st.markdown("""
            **Ablauf:** Direkt nach dem Zirkel 5 Aufschläge mit hohem Puls ins Feld bringen.
            **Trainer-Details:** Kontrolliere, ob der Anwurf trotz Ermüdung sauber bleibt.
            """)
        with st.expander("🏆 8. Abschlussspiel (20 Min): Handicap-Match"):
            st.markdown("""
            **Ablauf:** 4v3. Wenn Annahme der U13 wackelt, schlägt U14 von unten auf.
            **Trainer-Details:** Steuere das Spielniveau, um lange Rallyes zu generieren.
            """)

    # ---------------- WOCHE 2 ----------------
    with w2:
        st.subheader("TE 3 (90 Min): Zuspieler-Integration")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Kognitives Chaos"):
            st.markdown("""
            **Ablauf:** A pritscht Ball 1, B rollt Ball 2. Auf Pfiff: Sprint.
            **Trainer-Details:** Fehler sind hier erwünscht, um das Gehirn zu fordern.
            """)
        with st.expander("🎯 2. Technik I (15 Min): Zuspieler Beinarbeit"):
            st.markdown("""
            **Ablauf:** Zuspieler pendelt zwischen Netz und Pos 3. Trainer wirft Bälle, Zuspieler fängt sie in perfekter Pritsch-Position.
            **Trainer-Details:** Rechter Fuß muss leicht vorne sein!
            """)
        with st.expander("🎯 3. Technik II (15 Min): Annahme + Zuspiel"):
            st.markdown("""
            **Ablauf:** Annahme baggert zum Steller. Steller pritscht den Ball hoch in einen Korb.
            **Trainer-Details:** Zuspieler muss vor dem Pass absolut still stehen.
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Laufweg-Drill (Trocken)"):
            st.markdown("""
            **Ablauf:** U14/U13 in Grundaufstellung. Trainer wirft Bälle hoch. Zuspieler läuft ein, fängt den Ball, alle gehen zurück.
            **Trainer-Details:** Strenge Regelauslegung: Wer vor dem Einwurf losläuft, macht einen Positionsfehler.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Laufweg-Drill (Live)"):
            st.markdown("""
            **Ablauf:** Wie Übung 4, aber nun wird komplett (Annahme, Zuspiel, Dankeball rüber) durchgespielt.
            **Trainer-Details:** Der Steller muss den kürzesten Weg ans Netz finden.
            """)
        with st.expander("🏆 6. Abschlussspiel (20 Min): Wash-Game"):
            st.markdown("""
            **Ablauf:** 2 Rallyes in Folge gewinnen = 1 Punkt.
            **Trainer-Details:** Zweiter Ball fliegt sofort rein. Hält die Konzentration oben.
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

    # ---------------- WOCHE 3 ----------------
    with w3:
        st.subheader("TE 5 (90 Min): Annahme-Konstanz")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Reaktions-Sprints"):
            st.markdown("""
            **Ablauf:** Bauchlage am Netz. Auf Pfiff: Aufstehen, Rückwärtslauf bis 3m-Linie, Vorwärtssprint.
            **Trainer-Details:** Beim Rückwärtslaufen über die Schulter schauen lassen (Raum-Blick schulen).
            """)
        with st.expander("🎯 2. Technik I (15 Min): Annahme aus der Bewegung (Trocken)"):
            st.markdown("""
            **Ablauf:** Trainer wirft den Ball in weiten Bögen seitlich. Spieler muss mit Sidesteps hinter den Ball kommen und ihn fangen.
            **Trainer-Details:** Keine gekreuzten Beine beim Laufen! Nur Sidesteps.
            """)
        with st.expander("🎯 3. Technik II (15 Min): Annahme aus der Bewegung (Live)"):
            st.markdown("""
            **Ablauf:** Gleicher Aufbau wie Technik I, nun aber geschlagene Bälle. Nach dem Sidestep muss der Ball zum Ziel gebaggert werden.
            **Trainer-Details:** Verlange, dass das Spielbrett erst im letzten Moment geschlossen wird, wenn der Stand sicher ist.
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Aufschlag-Druck (Räume erkennen)"):
            st.markdown("""
            **Ablauf:** Aufschläger versuchen gezielt in die "Naht" (die Lücke zwischen zwei Annahmespielern) zu servieren.
            **Trainer-Details:** Fordere die Aufschläger heraus, kluge Entscheidungen zu treffen, statt nur hart draufzuhauen.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Annahme-Riegel verschieben"):
            st.markdown("""
            **Ablauf:** Die Annahme reagiert auf die taktischen Aufschläge aus Taktik I. Wer nimmt den Ball in der Schnittstelle?
            **Trainer-Details:** Klare Ansage fordern: Der Spieler, der den Ball seitlich vor sich hat, nimmt ihn. Der andere macht Platz.
            """)
        with st.expander("🏆 6. Abschlussspiel (20 Min): Druck-Turnier"):
            st.markdown("""
            **Ablauf:** 3v3 / 4v4. Ein direkter Annahmefehler (Ass für den Gegner) gibt 2 Punkte.
            **Trainer-Details:** Das erhöht den psychologischen Druck auf die Annahme. Erinnere sie an die Grundtechnik (tief bleiben).
            """)

        st.divider()

        st.subheader("TE 6 - Freitag (120 Min): Transition Defensive -> Annahme")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): 1v1 Volley-Tennis"):
            st.markdown("""
            **Ablauf:** 1v1 in schmalen Feldern. Ball darf 1x tippen, alle Körperteile erlaubt. Auf-/Abstieg.
            **Trainer-Details:** Halte das Tempo extrem hoch. Kurze Standzeiten, schnelle Wechsel.
            """)
        with st.expander("🎯 2. Technik I (15 Min): Not-Annahme am Boden (Trocken)"):
            st.markdown("""
            **Ablauf:** Hechtbagger üben (Sprawl). Aus dem Stand auf Brust/Bauch abgleiten, Arme ausstrecken. 
            **Trainer-Details:** Gleiten, nicht fallen! Knie dürfen nicht zuerst aufschlagen (Verletzungsgefahr).
            """)
        with st.expander("🎯 3. Technik II (15 Min): Not-Annahme am Boden (Live)"):
            st.markdown("""
            **Ablauf:** Trainer wirft Bälle knapp vor die Spieler. Diese müssen abtauchen und den Ball hoch ins Zentrum spielen.
            **Trainer-Details:** Der Ball muss nur hoch in die Luft, nicht zwingend perfekt zum Netz (Not-Situation!).
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Abwehr-Positionierung"):
            st.markdown("""
            **Ablauf:** Trockenübung auf dem Feld. Trainer hebt den Arm (simuliert Angriff), alle Spieler rücken auf ihre Abwehr-Positionen.
            **Trainer-Details:** Niemand darf im 'Schatten' eines eigenen Mitspielers stehen. Alle müssen den Ball sehen können.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Umschaltspiel nach Abwehr"):
            st.markdown("""
            **Ablauf:** Aus der Feldabwehr (Ball ist gerettet) sofort wieder in die Annahme-Struktur für den Aufbau formieren.
            **Trainer-Details:** Nach der Abwehr nicht stehenbleiben! Das Kommando lautet: 'Ball ist oben, Transition!'
            """)
        with st.expander("⚡ 6. Athletik I (15 Min): Rumpfstabilität"):
            st.markdown("""
            **Ablauf:** Unterarmstütz (Plank) mit Variationen (Bein heben) und Thera-Band Schulter-Rotation.
            **Trainer-Details:** Starke Körpermitte ist entscheidend für stabile Annahmen in der Bewegung.
            """)
        with st.expander("⚡ 7. Athletik II (10 Min): Schulter-Mobilität"):
            st.markdown("""
            **Ablauf:** Ausgiebiges Auslockern und leichtes dynamisches Dehnen der Schlag-Schulter.
            **Trainer-Details:** Dient der Verletzungsprävention vor dem Wochenende.
            """)
        with st.expander("🏆 8. Abschlussspiel (20 Min): Transition-Match"):
            st.markdown("""
            **Ablauf:** Schneller Ballwechsel-Rhythmus. Trainer wirft sofort nach Rallye-Ende neuen Ball ein.
            **Trainer-Details:** Wer nicht schnell genug von Abwehr auf Annahme umschaltet, wird vom nächsten Ball überrumpelt.
            """)

    # ---------------- WOCHE 4 ----------------
    with w4:
        st.subheader("TE 7 (90 Min): Match-Day Vorbereitung")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Pre-Game Einspielen"):
            st.markdown("""
            **Ablauf:** Paarweises Warmspielen. Simulation eines echten Spieltages (100% Fokus).
            **Trainer-Details:** Korrigiere Schlampigkeit sofort. Jede Berührung muss spielnah sein (tiefer Stand).
            """)
        with st.expander("🎯 2. Technik I (15 Min): Annahme-Präzisions-Test"):
            st.markdown("""
            **Ablauf:** Jeder Spieler nimmt 10 harte Trainer-Aufschläge an. Wie viele landen im Zielkreis?
            **Trainer-Details:** Baut künstlichen Wettkampf-Stress auf. Notiere die Werte.
            """)
        with st.expander("🎯 3. Technik II (15 Min): Der sichere Not-Aufschlag"):
            st.markdown("""
            **Ablauf:** 10 Aufschläge (Float oder von unten), die absolut sicher in die Feldmitte müssen.
            **Trainer-Details:** 'Das ist euer 14:14-Sicherheitsball.' Zeige, wie man Risiko rausnimmt (ruhiger Anwurf).
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Abstimmung U13/U14 (Schnittstellen)"):
            st.markdown("""
            **Ablauf:** Gemischte Teams spielen. Festlegen: Wer nimmt den kurzen Ball? Wer nimmt Bälle in der Mitte?
            **Trainer-Details:** Lass die U14-Spieler die Führung übernehmen und die Räume für die U13 ansagen.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Systemprüfung unter Zeitdruck"):
            st.markdown("""
            **Ablauf:** Trainer schlägt ein. Die Teams müssen den kompletten Aufbau in max. 4 Sekunden (U13) bzw. 3 Sekunden (U14) schaffen.
            **Trainer-Details:** Zähle laut mit. Fehler oder zu langsam = Liegestütze (Druck!).
            """)
        with st.expander("🏆 6. Abschlussspiel (20 Min): TuB Bocholt Liga (Hinrunde)"):
            st.markdown("""
            **Ablauf:** Spiel auf Zeit (z.B. 4 Min pro Match). Start des großen Monats-Turniers.
            **Trainer-Details:** Halte dich zurück. Lass sie spielen, führe eine korrekte Punktetabelle für Freitag.
            """)

        st.divider()

        st.subheader("TE 8 - Freitag (120 Min): Der große Monatstest")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Turnier-Warm-up"):
            st.markdown("""
            **Ablauf:** Dynamisches Dehnen, Einschlagen am Netz mit Zuspiel aus der Annahme.
            **Trainer-Details:** Achte auf die Körperspannung. Keine Faxen am Netz, volle Spieltags-Mentalität.
            """)
        with st.expander("🎯 2. Technik I (15 Min): Aufschlag-Duelle"):
            st.markdown("""
            **Ablauf:** Spieler treten direkt gegeneinander an. Wer platziert seinen Aufschlag besser in die vorgegebene Zone?
            **Trainer-Details:** Fördert den Wettkampfgeist. Fordere harte, flache Flugkurven.
            """)
        with st.expander("🎯 3. Technik II (15 Min): Annahme-Feinschliff"):
            st.markdown("""
            **Ablauf:** Die Verlierer aus Übung 2 schlagen auf, die Gewinner stehen im Annahme-Riegel und müssen perfekt abwehren.
            **Trainer-Details:** Korrigiere hier nur noch minimale Details. Lobe laute Kommunikation.
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Spielaufbau unter Wettkampfstress"):
            st.markdown("""
            **Ablauf:** Spielstände simulieren ('Es steht 23:23'). Annahme MUSS sitzen, um Sideout zu schaffen.
            **Trainer-Details:** Beobachte die Körpersprache. Wer versteckt sich? Fordere von Schlüsselspielern Verantwortung.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Timeout-Coaching"):
            st.markdown("""
            **Ablauf:** Teams simulieren Mini-Matches. Sie nehmen selbst Timeouts und suchen taktische Lösungen.
            **Trainer-Details:** Misch dich nicht ein. Lerne, wie deine Spieler miteinander kommunizieren und Probleme lösen.
            """)
        with st.expander("⚡ 6. Athletik I (15 Min): Explosive Sprungserie"):
            st.markdown("""
            **Ablauf:** 3x5 Hocksprünge auf Kommando, kurze Sprints zur 3m-Linie.
            **Trainer-Details:** ZNS (Zentrales Nervensystem) aktivieren vor dem Finale.
            """)
        with st.expander("⚡ 7. Athletik II (10 Min): Ausgiebiges Partner-Dehnen"):
            st.markdown("""
            **Ablauf:** Kurzes Runterfahren und Dehnen (Fokus Schultern & Beine).
            **Trainer-Details:** Puls kontrolliert senken, bevor es in das heiße Turnier geht.
            """)
        with st.expander("🏆 8. Abschlussspiel (20 Min): Monats-Finale"):
            st.markdown("""
            **Ablauf:** 2 Gewinnsätze bis 15 Punkte. Volle Anwendung aller Regeln (TuB Bocholt Liga Finale).
            **Trainer-Details:** Sei der strenge Schiedsrichter. Pfeif Netzfehler und Übertreten gnadenlos ab. Zelebriere den Sieger!
            """)

# [Monat 2, 3 und Spezial-Tab bleiben wie bisher, bis sie umgewandelt werden]
elif monat == "Monat 2: Grundtechnik Angriff & Aufschlag":
    st.info("Die Struktur für Monat 2 wartet auf das 15-Minuten-Update.")
elif monat == "Monat 3: Out-of-System & Match-Speed":
    st.info("Die Struktur für Monat 3 wartet auf das 15-Minuten-Update.")
elif monat == "System-Spezial: 3v3 meets 4v4":
    st.info("System-Spezial wartet auf das 15-Minuten-Update.")
