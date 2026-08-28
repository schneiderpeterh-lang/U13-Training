import streamlit as st

# Seiten-Konfiguration
st.set_page_config(page_title="U13/U14 Trainingsplan - DVV RTK", page_icon="🏐", layout="centered")

st.title("🏐 U13/U14 PRO Plan (DVV RTK Edition)")
st.markdown("TuB Bocholt | Max. 15 Min pro Übung (Hohe Taktung)\n**Fokus DVV Starting Six:** Anlauf-Rhythmus, Schlagbewegung, Highball-Set, Bagger & Athletik")

# Navigation - Monat
monat = st.selectbox(
    "Wähle den Trainingsmonat:", 
    [
        "Monat 1: Annahme-Präzision (RTK: Bagger & Athletik)", 
        "Monat 2: Angriff (RTK: Anlauf-Rhythmus & Schlagbewegung)", 
        "Monat 3: Out-of-System (RTK: Highball-Set & Abwehr-Bagger)",
        "System-Spezial: 3v3 meets 4v4"
    ]
)

# ---------------------------------------------------------
# MONAT 1: Annahme & System (Bagger & Athletik)
# ---------------------------------------------------------
if monat == "Monat 1: Annahme-Präzision (RTK: Bagger & Athletik)":
    st.header("Monat 1: Gezielte Annahme zum Steller")
    st.info("DVV RTK Fokus: Technik-Leitbild Bagger (ruhiges Spielbrett, Beinarbeit) und volleyballspezifische Athletik.")
    
    w1, w2, w3, w4 = st.tabs(["Woche 1", "Woche 2", "Woche 3", "Woche 4"])
    
    # ---------------- WOCHE 1 ----------------
    with w1:
        st.subheader("TE 1 (90 Min): Das sichere Spielbrett")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): RTK Reaktions-Baggern"):
            st.markdown("""
            **Ablauf:** Paarweise. Spieler A wirft leicht seitlich. Spieler B macht schnellen Sidestep, formt das Spielbrett und baggert zurück.
            **Trainer-Details (DVV Bagger):** Die Bewegung muss aus den Beinen kommen. Die Arme bleiben als ruhiges Spielbrett gestreckt. Keine Schwungbewegung aus den Schultern!
            """)
        with st.expander("🎯 2. Technik I (15 Min): Ziel-Baggern aus dem Stand"):
            st.markdown("""
            **Ablauf:** Kasten auf Pos II/III. Trainer wirft Bälle zentral an. Ball im hohen Bogen auf das Ziel baggern.
            **Trainer-Details:** Beine schulterbreit, Knie vor den Fußspitzen. Achte auf den korrekten Armwinkel.
            """)
        with st.expander("🎯 3. Technik II (15 Min): Bagger aus der Bewegung"):
            st.markdown("""
            **Ablauf:** Bälle in Lücken werfen. Spieler erläuft den Ball, stoppt ab und spielt zum Kasten.
            **Trainer-Details:** Der Bremsweg ist entscheidend. Stemmschritt setzen, Spielbrett erst im letzten Moment formen.
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Annahme-Riegel formieren"):
            st.markdown("""
            **Ablauf:** U14 (3er Riegel), U13 (2er Riegel). Trainer wirft leichte Bälle ein.
            **Trainer-Details:** Wer nimmt welchen Ball? Klare Kommunikation ('Ich!') ist ein RTK-Schwerpunkt im Aufbau.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Pass zum Steller"):
            st.markdown("""
            **Ablauf:** Gezielter Bagger zum einlaufenden Steller (dieser fängt den Ball über Kopf).
            **Trainer-Details:** Der Bagger muss hoch sein (Zeit kaufen). Zuspieler fordert den Ball lautstark.
            """)
        with st.expander("🏆 6. Abschlussspiel (20 Min): Annahme-Bingo"):
            st.markdown("""
            **Ablauf:** 3v3/4v4. Zusatzpunkt, wenn die Annahme perfekt beim Zuspieler landet.
            **Trainer-Details:** Werte streng: Musste der Zuspieler mehr als einen Schritt machen, gibt es keinen Zusatzpunkt.
            """)

        st.divider()

        st.subheader("TE 2 - Freitag (120 Min): RTK Athletik & Bagger unter Druck")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Tiefe Abwehr & Linien-Chaos"):
            st.markdown("""
            **Ablauf:** Linienfangen mit tiefem Abwehr-Stopp auf Pfiff.
            **Trainer-Details:** Ready-Position: Knie gebeugt, Gewicht auf dem Vorfuß. Keine aufrechte Haltung!
            """)
        with st.expander("🎯 2. Technik I (15 Min): Dankeball-Sprint"):
            st.markdown("""
            **Ablauf:** Sprint ans Netz, komplett abstoppen, baggern.
            **Trainer-Details:** Härte im Antritt fordern (Athletik) und extreme Ruhe im Bagger-Kontakt.
            """)
        with st.expander("🎯 3. Technik II (15 Min): Harte Bälle absorbieren"):
            st.markdown("""
            **Ablauf:** Trainer schlägt hart auf die Spieler. Arme hinhalten, Ball abprallen lassen.
            **Trainer-Details (DVV Bagger):** Körper absorbiert den Druck. Arme nicht nach oben reißen!
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Serve & Pass (Leicht)"):
            st.markdown("""
            **Ablauf:** Aufschläge von unten. Fokus auf den ruhigen Annahme-Aufbau.
            **Trainer-Details:** Überprüfe die Positionierung der Annahmespieler zueinander.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Serve & Pass (Schwer)"):
            st.markdown("""
            **Ablauf:** Harte Aufschläge von oben.
            **Trainer-Details:** Steh hinter der Annahme. Passen sie den Winkel des Spielbretts an?
            """)
        with st.expander("⚡ 6. Athletik I (15 Min): DVV Rumpf- & Bein-Power"):
            st.markdown("""
            **Ablauf:** 3 Runden Zirkel (Plank, tiefe Ausfallschritte, seitliche Sprünge).
            **Trainer-Details (RTK Athletik):** Ein starker Rumpf ist die Basis für das 'sichere Spielbrett' beim Baggern.
            """)
        with st.expander("⚡ 7. Athletik II (10 Min): Puls-Aufschlag"):
            st.markdown("""
            **Ablauf:** Direkt nach dem Zirkel 5 Aufschläge mit hohem Puls.
            **Trainer-Details:** Athletische Ausdauer: Konzentration trotz Laktat hochhalten.
            """)
        with st.expander("🏆 8. Abschlussspiel (20 Min): Handicap-Match"):
            st.markdown("""
            **Ablauf:** 4v3. Wenn Annahme der U13 wackelt, schlägt U14 von unten auf.
            **Trainer-Details:** Fokus auf langen Ballwechseln und sauberen Bagger-Aktionen.
            """)

    # ---------------- WOCHE 2 ----------------
    with w2:
        st.subheader("TE 3 (90 Min): Zuspieler-Integration & Bagger-Winkel")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Kognitives Chaos"):
            st.markdown("""
            **Ablauf:** A pritscht Ball 1, B rollt Ball 2. Auf Pfiff: Sprint zur Grundlinie und zurück.
            **Trainer-Details:** Fehler sind hier erwünscht. Fördert die schnelle kognitive Umschaltung.
            """)
        with st.expander("🎯 2. Technik I (15 Min): Bagger-Winkel anpassen"):
            st.markdown("""
            **Ablauf:** Spieler steht auf Pos 5, wirft sich den Ball selbst an und baggert diagonal auf Pos 2.
            **Trainer-Details (RTK Bagger):** Die innere Schulter muss tiefer sein, damit das Spielbrett zum Ziel (Pos 2/3) zeigt.
            """)
        with st.expander("🎯 3. Technik II (15 Min): Annahme + Zuspiel Kopplung"):
            st.markdown("""
            **Ablauf:** Annahme baggert zum Steller. Steller pritscht hoch in einen Korb.
            **Trainer-Details:** Der Bagger muss hoch genug sein, damit der Steller in Ruhe unter den Ball treten kann.
            """)
        with st.expander("🧠 4. Taktik I (15 Min): System-Laufwege (Trocken)"):
            st.markdown("""
            **Ablauf:** U14/U13 in Grundaufstellung. Trainer wirft Bälle hoch. Zuspieler läuft ein, fängt Ball, alle rotieren.
            **Trainer-Details:** Positionsfehler streng abpfeifen. Erst laufen, wenn der Ball den Trainer verlässt.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): System-Laufwege (Live)"):
            st.markdown("""
            **Ablauf:** Wie Übung 4, aber komplett durchgespielt (Annahme, Zuspiel, Dankeball rüber).
            **Trainer-Details:** Laufweg des Stellers auf direktem Weg zum Netz einfordern.
            """)
        with st.expander("🏆 6. Abschlussspiel (20 Min): Wash-Game (2 Rallyes)"):
            st.markdown("""
            **Ablauf:** 2 Rallyes in Folge gewinnen = 1 Punkt.
            **Trainer-Details:** Zweiter Ball fliegt sofort rein. Hält die Konzentration oben.
            """)

        st.divider()

        st.subheader("TE 4 - Freitag (120 Min): RTK Athletik & System unter Druck")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Ball-Handling Staffel"):
            st.markdown("""
            **Ablauf:** Staffel mit Ball prellen, Anwurf-Simulation am Netz und Richtungswechseln.
            **Trainer-Details:** Ball muss vor der Schlag-Schulter angeworfen werden (Vorbereitung für Aufschlag).
            """)
        with st.expander("🎯 2. Technik I (15 Min): Zonen-Aufschlag"):
            st.markdown("""
            **Ablauf:** Aufschläge gezielt auf Turnmatten in den Ecken.
            **Trainer-Details:** Handgelenk muss fest sein, um Druck und Genauigkeit zu erzeugen.
            """)
        with st.expander("🎯 3. Technik II (15 Min): Annahme-Verschiebung"):
            st.markdown("""
            **Ablauf:** Aufschläger wechselt permanent die Position (Mitte, Seite). Annahmeriegel muss rotieren.
            **Trainer-Details:** Den Kreuzwinkel abdecken! Das äußere Bein blockiert den Ball Richtung Aus.
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Out-of-System (Trocken)"):
            st.markdown("""
            **Ablauf:** Trainer wirft Ball absichtlich ins Aus. Spieler rufen 'Hilfe' und fangen den Ball.
            **Trainer-Details:** Es geht rein um die auditive Kommunikation. Wer übernimmt das Zuspiel?
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Out-of-System (Live)"):
            st.markdown("""
            **Ablauf:** Notzuspiel aus dem Chaos zum Angreifer (Highball-Vorbereitung).
            **Trainer-Details:** Der Notpass muss hoch und weit weg vom Netz sein, um dem Angreifer Zeit zu geben.
            """)
        with st.expander("⚡ 6. Athletik I (15 Min): DVV Fußarbeit (Leiter)"):
            st.markdown("""
            **Ablauf:** Koordinationsleiter für schnelle Fußarbeit und Agilität.
            **Trainer-Details (RTK Athletik):** Fersen bleiben in der Luft (Vorfuß-Lauf). Kurze, knackige Kontakte.
            """)
        with st.expander("⚡ 7. Athletik II (10 Min): Core-Rotation"):
            st.markdown("""
            **Ablauf:** Medizinball-Würfe (seitlich).
            **Trainer-Details:** Imitiert die Rumpf-Rotation, die für Angriff und stabilen Bagger aus der Drehung nötig ist.
            """)
        with st.expander("🏆 8. Abschlussspiel (20 Min): System-Kaiser"):
            st.markdown("""
            **Ablauf:** Herausforderer rücken nur bei 3er-System-Aufbau auf die Kaiserseite.
            **Trainer-Details:** Lobe auch den Versuch, wenn der finale Ball im Aus landet!
            """)

    # ---------------- WOCHE 3 ----------------
    with w3:
        st.subheader("TE 5 (90 Min): Annahme-Konstanz & Körperkontrolle")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Reaktions-Sprints"):
            st.markdown("""
            **Ablauf:** Bauchlage am Netz. Auf Pfiff: Aufstehen, Rückwärtslauf bis 3m-Linie, Vorwärtssprint.
            **Trainer-Details:** Beim Rückwärtslaufen über die Schulter schauen lassen (Raum-Blick schulen).
            """)
        with st.expander("🎯 2. Technik I (15 Min): Bagger aus tiefer Bewegung"):
            st.markdown("""
            **Ablauf:** Trainer wirft weite Bälle. Spieler macht Sidesteps, stoppt extrem tief ab und fängt den Ball.
            **Trainer-Details (DVV Bagger):** Keine gekreuzten Beine! Nur saubere Sidesteps und extrem tiefer Körperschwerpunkt.
            """)
        with st.expander("🎯 3. Technik II (15 Min): Bagger aus Bewegung (Live)"):
            st.markdown("""
            **Ablauf:** Wie Übung 2, nun aber geschlagene Bälle sauber zum Ziel baggern.
            **Trainer-Details:** Das Spielbrett erst im letzten Moment schließen, wenn der Stand sicher ist.
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Aufschlag-Druck (Räume)"):
            st.markdown("""
            **Ablauf:** Aufschläger zielen in die "Naht" (Lücke zwischen zwei Annahmespielern).
            **Trainer-Details:** Zwingt die Annahme, Verantwortlichkeiten blitzschnell zu klären.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Annahme-Riegel Schnittstellen"):
            st.markdown("""
            **Ablauf:** Die Annahme reagiert auf die taktischen Aufschläge. Wer nimmt den Ball in der Schnittstelle?
            **Trainer-Details:** Klare DVV-Regel: Der Spieler, der den Ball seitlich *vor* sich hat, nimmt ihn.
            """)
        with st.expander("🏆 6. Abschlussspiel (20 Min): Druck-Turnier"):
            st.markdown("""
            **Ablauf:** 3v3 / 4v4. Ein direkter Annahmefehler (Ass für Gegner) gibt 2 Punkte.
            **Trainer-Details:** Erhöht den psychologischen Druck auf das 'ruhige Spielbrett'.
            """)

        st.divider()

        st.subheader("TE 6 - Freitag (120 Min): Transition & RTK Boden-Abwehr")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): 1v1 Volley-Tennis"):
            st.markdown("""
            **Ablauf:** 1v1 in schmalen Feldern. Ball darf 1x tippen, alle Körperteile erlaubt.
            **Trainer-Details:** Halte das Tempo hoch. Kurze Standzeiten, schnelle Wechsel.
            """)
        with st.expander("🎯 2. Technik I (15 Min): DVV Not-Annahme (Sprawl)"):
            st.markdown("""
            **Ablauf:** Hechtbagger üben. Aus dem Stand auf Brust/Bauch abgleiten, Arme ausstrecken. 
            **Trainer-Details (RTK):** Gleiten, nicht fallen! Knie dürfen nicht zuerst aufschlagen.
            """)
        with st.expander("🎯 3. Technik II (15 Min): Not-Annahme (Live)"):
            st.markdown("""
            **Ablauf:** Trainer wirft Bälle knapp vor die Spieler. Abtauchen und hoch ins Zentrum spielen.
            **Trainer-Details:** Der Ball muss nur hoch in die Luft, nicht zwingend perfekt zum Netz (Not-Situation).
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Abwehr-Positionierung"):
            st.markdown("""
            **Ablauf:** Trockenübung. Trainer hebt Arm (Angriffssimulation), alle rücken auf Abwehr-Positionen.
            **Trainer-Details:** Niemand darf im 'Schatten' eines eigenen Mitspielers stehen (Sichtlinien-Check).
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Umschaltspiel (Transition)"):
            st.markdown("""
            **Ablauf:** Aus der Feldabwehr (Ball ist gerettet) sofort wieder in die Annahme-Struktur formieren.
            **Trainer-Details:** Nach der Abwehr nicht stehenbleiben! Kommando: 'Ball ist oben, Transition!'
            """)
        with st.expander("⚡ 6. Athletik I (15 Min): Rumpfstabilität (Planks)"):
            st.markdown("""
            **Ablauf:** Unterarmstütz mit Variationen (Bein heben) und Thera-Band Schulter-Rotation.
            **Trainer-Details:** Starke Körpermitte ist essenziell für stabile Annahmen in der Bewegung.
            """)
        with st.expander("⚡ 7. Athletik II (10 Min): Schulter-Mobilität"):
            st.markdown("""
            **Ablauf:** Ausgiebiges Auslockern und dynamisches Dehnen der Schlag-Schulter.
            **Trainer-Details:** Verletzungsprävention vor dem Wochenende.
            """)
        with st.expander("🏆 8. Abschlussspiel (20 Min): Transition-Match"):
            st.markdown("""
            **Ablauf:** Schneller Rhythmus. Trainer wirft sofort nach Rallye-Ende neuen Ball ein.
            **Trainer-Details:** Wer nicht schnell genug von Abwehr auf Annahme umschaltet, wird bestraft.
            """)

    # ---------------- WOCHE 4 ----------------
    with w4:
        st.subheader("TE 7 (90 Min): Match-Day Vorbereitung & DVV Checks")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Pre-Game Einspielen"):
            st.markdown("""
            **Ablauf:** Paarweises Warmspielen. Simulation eines echten Spieltages.
            **Trainer-Details:** Korrigiere Schlampigkeit sofort. Jede Berührung muss spielnah (tief) sein.
            """)
        with st.expander("🎯 2. Technik I (15 Min): Annahme-Präzisions-Test"):
            st.markdown("""
            **Ablauf:** Jeder nimmt 10 harte Trainer-Aufschläge an. Wie viele landen im Zielkreis?
            **Trainer-Details:** Baut künstlichen Wettkampf-Stress auf. Notiere die Werte.
            """)
        with st.expander("🎯 3. Technik II (15 Min): Der sichere Not-Aufschlag"):
            st.markdown("""
            **Ablauf:** 10 Aufschläge (Float/von unten), die absolut sicher in die Feldmitte müssen.
            **Trainer-Details:** 'Das ist euer 14:14-Ball.' Zeige, wie man Risiko rausnimmt (ruhiger Anwurf).
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Abstimmung Schnittstellen"):
            st.markdown("""
            **Ablauf:** Gemischte Teams spielen. Festlegen: Wer nimmt den kurzen Ball? Wer nimmt Mitte?
            **Trainer-Details:** Lass die U14 die Führung übernehmen und Räume für die U13 ansagen.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Systemprüfung unter Zeitdruck"):
            st.markdown("""
            **Ablauf:** Trainer schlägt ein. Kompletter Aufbau in max. 4 Sek (U13) bzw. 3 Sek (U14).
            **Trainer-Details:** Zähle laut mit. Fehler oder zu langsam = Liegestütze.
            """)
        with st.expander("🏆 6. Abschlussspiel (20 Min): TuB Bocholt Liga (Hinrunde)"):
            st.markdown("""
            **Ablauf:** Spiel auf Zeit. Start des großen Monats-Turniers.
            **Trainer-Details:** Halte dich zurück. Führe eine korrekte Punktetabelle.
            """)

        st.divider()

        st.subheader("TE 8 - Freitag (120 Min): Monatstest & Turnierhärte")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Turnier-Warm-up"):
            st.markdown("""
            **Ablauf:** Dynamisches Dehnen, Einschlagen am Netz mit Zuspiel aus der Annahme.
            **Trainer-Details:** Keine Faxen am Netz, volle Spieltags-Mentalität einfordern.
            """)
        with st.expander("🎯 2. Technik I (15 Min): Aufschlag-Duelle"):
            st.markdown("""
            **Ablauf:** Spieler treten direkt gegeneinander an. Wer platziert besser in die Zone?
            **Trainer-Details:** Fördert den Wettkampfgeist. Flache Flugkurven fordern.
            """)
        with st.expander("🎯 3. Technik II (15 Min): Annahme-Feinschliff"):
            st.markdown("""
            **Ablauf:** Verlierer aus Übung 2 schlagen auf, Gewinner stehen im Annahme-Riegel.
            **Trainer-Details:** Korrigiere hier nur noch minimale Details am Bagger-Winkel.
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Spielaufbau unter Stress"):
            st.markdown("""
            **Ablauf:** Spielstände simulieren ('Es steht 23:23'). Annahme MUSS sitzen für Sideout.
            **Trainer-Details:** Beobachte die Körpersprache. Fordere von Schlüsselspielern Verantwortung.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Timeout-Coaching"):
            st.markdown("""
            **Ablauf:** Mini-Matches. Teams nehmen selbst Timeouts und suchen taktische Lösungen.
            **Trainer-Details:** Misch dich nicht ein. Lerne, wie deine Spieler Probleme lösen.
            """)
        with st.expander("⚡ 6. Athletik I (15 Min): Explosive Sprungserie"):
            st.markdown("""
            **Ablauf:** 3x5 Hocksprünge auf Kommando, kurze Sprints zur 3m-Linie.
            **Trainer-Details (RTK):** ZNS (Zentrales Nervensystem) aktivieren vor dem Finale.
            """)
        with st.expander("⚡ 7. Athletik II (10 Min): Ausgiebiges Partner-Dehnen"):
            st.markdown("""
            **Ablauf:** Kurzes Runterfahren und Dehnen (Fokus Schultern & Beine).
            **Trainer-Details:** Puls kontrolliert senken, Verletzungsrisiko mindern.
            """)
        with st.expander("🏆 8. Abschlussspiel (20 Min): Monats-Finale"):
            st.markdown("""
            **Ablauf:** 2 Gewinnsätze bis 15 Punkte. Volle Anwendung aller Regeln.
            **Trainer-Details:** Sei der strenge Schiri. Pfeif Netzfehler gnadenlos ab. Zelebriere den Sieger!
            """)

# ---------------------------------------------------------
# MONAT 2: Angriff (Anlauf-Rhythmus & Schlagbewegung)
# ---------------------------------------------------------
elif monat == "Monat 2: Angriff (RTK: Anlauf-Rhythmus & Schlagbewegung)":
    st.header("Monat 2: Der perfekte Angriffsschlag")
    st.info("DVV RTK Fokus: Explosiver 3er-Anlauf (Links-Rechts-Links) und saubere Schlagbewegung (Peitscheneffekt).")
    
    w1, w2, w3, w4 = st.tabs(["Woche 1", "Woche 2", "Woche 3", "Woche 4"])
    
    # ---------------- WOCHE 1 ----------------
    with w1:
        st.subheader("TE 1 (90 Min): Die RTK Schlagbewegung (Armzug)")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Schulter-Rotation & Athletik"):
            st.markdown("""
            **Ablauf:** Einarmiges Baseball-Werfen paarweise. 
            **Trainer-Details (RTK Schlagbewegung):** Die Bewegung startet in der Hüfte, zieht über die Schulter und endet im Handgelenk (Peitschenschlag).
            """)
        with st.expander("🎯 2. Technik I (15 Min): Trockenübung Wand-Schlagen"):
            st.markdown("""
            **Ablauf:** Spieler vor Wand. Rechter Ellenbogen hoch, Handgelenk klappt aktiv ab.
            **Trainer-Details (DVV Essentials):** Bogenspannung aufbauen. Der Führungsarm (links) zeigt zum Ball, der Schlagarm ist weit hinten geöffnet.
            """)
        with st.expander("🎯 3. Technik II (15 Min): Schlag aus dem Stand (Netz)"):
            st.markdown("""
            **Ablauf:** Trainer wirft auf Pos IV. Stemmschritt aus dem Stand, Schlagen.
            **Trainer-Details:** Treffpunkt ist am höchsten Punkt, leicht *vor* dem Körper (auf 1 Uhr). Aktives Abklappen des Handgelenks für Topspin.
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Ziel-Schlagen (Line/Diagonal)"):
            st.markdown("""
            **Ablauf:** Aus dem Stand gezielt auf Matten (Longline und Diagonal) schlagen.
            **Trainer-Details:** Die Schulterachse bestimmt die Richtung. Keine verdrehten Armbewegungen.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Block-Sicht (Hit or Lob)"):
            st.markdown("""
            **Ablauf:** Trainer signalisiert Block (Hand hoch/runter). Spieler entscheidet: Schlag oder Lob.
            **Trainer-Details:** Die Schlagbewegung muss beim Lob bis zum Schluss identisch aussehen (Täuschung).
            """)
        with st.expander("🏆 6. Abschlussspiel (20 Min): Angriffs-Bingo"):
            st.markdown("""
            **Ablauf:** 3v3/4v4. Punkte zählen nur bei geschlagenem Ball oder aggressivem Angriff.
            **Trainer-Details:** Ermutige hartes Schlagen. Fehler (Netz/Aus) bei gutem Armzug positiv verstärken!
            """)

        st.divider()

        st.subheader("TE 2 - Freitag (120 Min): RTK Anlauf-Rhythmus & Sprungkraft")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Rhythmus-Schulung (Trocken)"):
            st.markdown("""
            **Ablauf:** Klatschen des Anlaufs: 'Links... Rechts-Links!' (für Rechtshänder).
            **Trainer-Details (RTK Anlauf):** Erster Schritt (Orientierung) ist langsam, die letzten zwei (Stemmschritt) sind extrem schnell und explosiv.
            """)
        with st.expander("🎯 2. Technik I (15 Min): Anlauf mit Ball-Fangen"):
            st.markdown("""
            **Ablauf:** Trainer wirft Ball hoch. Spieler läuft mit 3er-Rhythmus an, springt und fängt den Ball am höchsten Punkt.
            **Trainer-Details:** Beide Arme MÜSSEN beim letzten Schritt weit nach hinten schwingen (Doppelarmschwung) und den Körper nach oben reißen.
            """)
        with st.expander("🎯 3. Technik II (15 Min): Kopplung Anlauf + Schlag"):
            st.markdown("""
            **Ablauf:** Kompletter Angriff aus dem Anlauf (Zuspieler wirft oder pritscht).
            **Trainer-Details (DVV Essentials):** Den Ball in der Luft nicht unterlaufen! Der Spieler muss den Ball *vor* sich halten.
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Angriff aus der Transition"):
            st.markdown("""
            **Ablauf:** Spieler startet am Netz (Block), zieht sich rückwärts zur 3m-Linie zurück, startet dann den Anlauf.
            **Trainer-Details:** Die schnelle Rückwärtsbewegung (Athletik) ist entscheidend, um genug Platz für den Anlauf-Rhythmus zu haben.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Freeball-Kill"):
            st.markdown("""
            **Ablauf:** Trainer schlägt Dankeball ein. Annahme -> Zuspiel -> voller Anlauf & Schlagangriff.
            **Trainer-Details:** Das System muss fließen, damit der Angreifer seinen Rhythmus findet.
            """)
        with st.expander("⚡ 6. Athletik I (15 Min): DVV Sprungkraft-Zirkel"):
            st.markdown("""
            **Ablauf:** Box-Jumps, Hürdensprünge, tiefe Kniebeugen.
            **Trainer-Details (RTK Athletik):** Maximale Explosivität in den Beinen trainieren, um die Sprunghöhe für den Angriff zu maximieren.
            """)
        with st.expander("⚡ 7. Athletik II (10 Min): Core-Spannung"):
            st.markdown("""
            **Ablauf:** Medizinball-Slams auf den Boden (aktiviert den Rumpf für die Schlagbewegung).
            **Trainer-Details:** Die Kraft für den Schlag kommt massiv aus der Bauchmuskulatur (Klappmesser-Effekt).
            """)
        with st.expander("🏆 8. Abschlussspiel (20 Min): Angriffs-Turnier"):
            st.markdown("""
            **Ablauf:** 3v3/4v4. Erfolgreiche Angriffsschläge aus vollem Anlauf zählen 2 Punkte.
            **Trainer-Details:** Zuspieler müssen die Bälle hoch genug stellen (Highball), damit der Rhythmus passt.
            """)

    # ---------------- WOCHE 2 ----------------
    with w2:
        st.subheader("TE 3 (90 Min): Härte & Blocküberwindung")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Hechten & Block-Schatten"):
            st.markdown("""
            **Ablauf:** Blocksprung am Netz, landen, rückwärts ausweichen, Abwehrhecht.
            **Trainer-Details:** Landung beim Blocksprung immer beidbeinig zur Verletzungsprävention.
            """)
        with st.expander("🎯 2. Technik I (15 Min): Schlaghärte gegen die Matte"):
            st.markdown("""
            **Ablauf:** Spieler schlagen Bälle aus dem Stand mit maximaler Härte senkrecht auf eine Matte vor ihnen.
            **Trainer-Details (RTK Schlag):** Peitscheneffekt! Der Armzug muss explosionsartig durchgezogen werden.
            """)
        with st.expander("🎯 3. Technik II (15 Min): Anlauf-Timing anpassen"):
            st.markdown("""
            **Ablauf:** Trainer wirft variable Pässe (flach, hoch, zu nah). Angreifer muss Rhythmus anpassen.
            **Trainer-Details:** Der langsame erste Orientierungsschritt rettet den Angriff bei unsauberen Pässen.
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Schlagen gegen den Doppelblock"):
            st.markdown("""
            **Ablauf:** U14 stellt festen Doppelblock (Kasten). Angreifer muss die Hände des Blocks gezielt anschlagen (Block-Out).
            **Trainer-Details:** Den Ball hoch und lang an die äußere Hand des Blockers schlagen.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Sicherung des Angreifers"):
            st.markdown("""
            **Ablauf:** Wie Übung 4, aber die Mannschaft formiert sich extrem tief um den Angreifer, um Abpraller zu retten.
            **Trainer-Details:** Niemand guckt zu! Alle rücken ran (Sicherung).
            """)
        with st.expander("🏆 6. Abschlussspiel (20 Min): Hit or Tip Match"):
            st.markdown("""
            **Ablauf:** Punkte nur durch harten Schlag (2 Pkt) oder perfekten Lob (1 Pkt).
            **Trainer-Details:** Fördert variables Angriffsspiel.
            """)

        st.divider()

        st.subheader("TE 4 - Freitag (120 Min): Aufschlag als Angriff & RTK Power")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Sprints & Reaktions-Baggern"):
            st.markdown("""
            **Ablauf:** Schnelle Sidesteps, Spielbrett stabilisieren, kurze Sprints.
            **Trainer-Details:** Hohe Frequenz in den Füßen.
            """)
        with st.expander("🎯 2. Technik I (15 Min): Tennis-Aufschlag (Technik)"):
            st.markdown("""
            **Ablauf:** Anwurf vor dem Körper, Schlag aus der Bogenspannung (wie beim Angriff).
            **Trainer-Details:** Der Aufschlag ist der erste Angriff! Bogenspannung muss sichtbar sein.
            """)
        with st.expander("🎯 3. Technik II (15 Min): Zonen-Aufschlag unter Druck"):
            st.markdown("""
            **Ablauf:** Aufschläge ab 3m/6m-Linie. Bei 3 Treffern ins Ziel nach hinten rücken.
            **Trainer-Details:** Flache Flugkurve direkt über das Netz forcieren.
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Aufschlag vs. Riegel"):
            st.markdown("""
            **Ablauf:** Team A serviert hart, Team B baut auf.
            **Trainer-Details:** Den Aufschlägern klare taktische Vorgaben geben (z.B. "Kurz auf die Linie").
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Freeball-Kill (Komplex)"):
            st.markdown("""
            **Ablauf:** Annahme -> Zuspiel -> voller Schlagangriff aus dem Rhythmus.
            **Trainer-Details:** Fokus auf Flüssigkeit. Der Angreifer darf nicht stehen bleiben.
            """)
        with st.expander("⚡ 6. Athletik I (15 Min): DVV Schulter-Power"):
            st.markdown("""
            **Ablauf:** Einarmige Medizinballwürfe über das Netz + Kräftigung oberer Rücken.
            **Trainer-Details:** Schnellkraft in der Schulter = Härte im Angriff.
            """)
        with st.expander("⚡ 7. Athletik II (10 Min): Bein-Plyometrie"):
            st.markdown("""
            **Ablauf:** Kurze, reaktive Sprünge (z.B. von niedrigem Kasten droppen und sofort hochspringen).
            **Trainer-Details:** Bodenkontaktzeit minimieren für explosiven Absprung.
            """)
        with st.expander("🏆 8. Abschlussspiel (20 Min): Wash-Game Extrem"):
            st.markdown("""
            **Ablauf:** 2 Rallyes am Stück gewinnen. Block- und Sicherungsaktionen geben Zusatzpunkte.
            **Trainer-Details:** Belohne schmutzige Punkte und gerettete Bälle.
            """)

    # ---------------- WOCHE 3 ----------------
    with w3:
        st.subheader("TE 5 (90 Min): Kognition & Abwehr")
        with st.expander("🎾 1. Warm-up (10 Min): 1v1 Kreatives Tennis Game"):
            st.markdown("""
            **Ablauf:** Feld in Schläuche teilen. 1v1, 1x Aufkommen erlaubt.
            **Trainer-Details:** Schult periphere Sicht (Wo steht der Gegner?).
            """)
        with st.expander("🎯 2. Technik I (15 Min): Schmetter-Abwehr (Technik)"):
            st.markdown("""
            **Ablauf:** Spieler tief, Trainer schlägt gezielt hart an. Arme ruhig halten.
            **Trainer-Details:** Nicht schwingen! Körper absorbiert die Härte (DVV Bagger-Leitbild).
            """)
        with st.expander("🎯 3. Technik II (15 Min): Schmetter-Abwehr (Bewegung)"):
            st.markdown("""
            **Ablauf:** Trainer schlägt leicht seitlich. Spieler macht Sidestep und wehrt ab.
            **Trainer-Details:** Winkel des Spielbretts anpassen (innere Schulter tief).
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Abwehr -> Transition"):
            st.markdown("""
            **Ablauf:** Harter Angriff -> Abwehr ins Zentrum -> Notzuspiel -> Gegenangriff.
            **Trainer-Details:** Sofortiges Umschalten von Defensive in den Anlauf-Rhythmus.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Block und V-Abwehr"):
            st.markdown("""
            **Ablauf:** 1er/2er Block steht, Abwehr positioniert sich V-förmig dahinter.
            **Trainer-Details:** Abwehrspieler dürfen nicht im 'Schatten' des Blocks stehen.
            """)
        with st.expander("🏆 6. Abschlussspiel (20 Min): Abwehr-König"):
            st.markdown("""
            **Ablauf:** Spektakuläre Abwehr mit erfolgreichem Gegenangriff gibt 2 Punkte.
            **Trainer-Details:** Lobe den Mut, sich auf den Boden zu werfen.
            """)

        st.divider()

        st.subheader("TE 6 - Freitag (120 Min): Block-Timing & DVV Feldverteidigung")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Block-Sidesteps & Sprünge"):
            st.markdown("""
            **Ablauf:** Paarweise am Netz. Schnelle Sidesteps, hochspringen und abklatschen.
            **Trainer-Details:** Landung kontrollieren, Knie federn lassen.
            """)
        with st.expander("🎯 2. Technik I (15 Min): Der 1er- und 2er-Block"):
            st.markdown("""
            **Ablauf:** Timing beim Absprung. Hände fest über das Netz schieben.
            **Trainer-Details:** Blocker springt minimal nach dem Angreifer. Handgelenke starr!
            """)
        with st.expander("🎯 3. Technik II (15 Min): Lobs erlaufen"):
            st.markdown("""
            **Ablauf:** Trainer tippt Bälle kurz hinter den Block. Abwehr muss tief reinstarten.
            **Trainer-Details:** Start aus der tiefen Haltung (Ready-Position) ist zwingend.
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Block-Abwehr-Dreieck"):
            st.markdown("""
            **Ablauf:** U14 stellt Block, U13 sichert die Ecken und Linien.
            **Trainer-Details:** Jeder muss genau wissen, welchen Raum der Block offen lässt.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Transition nach Block-Touch"):
            st.markdown("""
            **Ablauf:** Ball touchiert den Block, verlangsamt sich. Abwehr spielt hoch, Angreifer formiert sich neu.
            **Trainer-Details:** Kommunikation ('Touch!') einfordern.
            """)
        with st.expander("⚡ 6. Athletik I (15 Min): DVV Sprungausdauer"):
            st.markdown("""
            **Ablauf:** Serien aus Blocksprüngen mit lateralen Sidesteps entlang des Netzes.
            **Trainer-Details (RTK):** Belastet die Waden stark. Auf saubere Technik auch bei Ermüdung achten.
            """)
        with st.expander("⚡ 7. Athletik II (10 Min): Rumpf für Blockstabilität"):
            st.markdown("""
            **Ablauf:** Core-Halteübungen (Plank mit Gewichtsverlagerung).
            **Trainer-Details:** Ein stabiler Rumpf verhindert das 'Wegfliegen' beim Blocken.
            """)
        with st.expander("🏆 8. Abschlussspiel (20 Min): Block & Defense Match"):
            st.markdown("""
            **Ablauf:** 3v3/4v4. Kill-Blocks zählen doppelt.
            **Trainer-Details:** Fordere die U13 auf, den 1er-Block mutig einzusetzen.
            """)

    # ---------------- WOCHE 4 ----------------
    with w4:
        st.subheader("TE 7 (90 Min): Entscheidungsfindung & Match-Simulation")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): 1v1 Auf-/Absteiger"):
            st.markdown("""
            **Ablauf:** Schnelles Warm-up mit vollem Körpereinsatz im 1-gegen-1 (Tennis).
            **Trainer-Details:** Puls hochtreiben, Spaßfaktor vor der Taktik.
            """)
        with st.expander("🎯 2. Technik I (15 Min): Hit or Lob Präzision"):
            st.markdown("""
            **Ablauf:** Angreifer entscheidet in der Luft: Harter Schlag oder gezielter Tip über Block.
            **Trainer-Details:** Anlauf muss für beide Optionen identisch aussehen (Täuschung!).
            """)
        with st.expander("🎯 3. Technik II (15 Min): Angriff aus schlechten Pässen"):
            st.markdown("""
            **Ablauf:** Trainer wirft unpräzise Bälle (zu nah, zu weit). Angreifer muss das Beste draus machen.
            **Trainer-Details:** Nicht in den Block dreschen! Cleverness schlägt Härte bei schlechten Pässen.
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Systemprüfung unter Druck"):
            st.markdown("""
            **Ablauf:** Trainer serviert variabel. Teams müssen Annahme, Zuspiel und Angriff fehlerfrei durchbringen.
            **Trainer-Details:** Erhöhe die Aufschlag-Härte stufenweise.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Fehlerkompensation"):
            st.markdown("""
            **Ablauf:** Wenn Annahme wackelt, muss Notzuspiel und Sicherung perfekt greifen.
            **Trainer-Details:** Das Team muss lernen, sich selbst aus dem Sumpf zu ziehen.
            """)
        with st.expander("🏆 6. Abschlussspiel (20 Min): TuB Bocholt Liga"):
            st.markdown("""
            **Ablauf:** Reiner Wettkampf 3v3/4v4.
            **Trainer-Details:** Mache die Halle heiß für das Final-Wochenende!
            """)

        st.divider()

        st.subheader("TE 8 - Freitag (120 Min): Das große Angriffs-Finale")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Pre-Game Routine & Einschlagen"):
            st.markdown("""
            **Ablauf:** Offizieller Spieltags-Ablauf: Paare einspielen, Angriffsschläge am Netz.
            **Trainer-Details:** Lass die Kapitäne das Einspielen komplett selbst leiten.
            """)
        with st.expander("🎯 2. Technik I (15 Min): Nervenstarker Aufschlag"):
            st.markdown("""
            **Ablauf:** '14:14'. 5 harte Aufschläge fehlerfrei ins Zielfeld platzieren.
            **Trainer-Details:** Baue künstlichen Druck auf (Pfeife, Nebengeräusche).
            """)
        with st.expander("🎯 3. Technik II (15 Min): Direkte Angriffs-Duelle"):
            st.markdown("""
            **Ablauf:** Angreifer gegen Blockspieler. Wer gewinnt das 1v1 am Netz?
            **Trainer-Details:** Lobe aggressive Schläge und saubere Block-Penetration.
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Match-Taktik & Coaching"):
            st.markdown("""
            **Ablauf:** Teams analysieren gegnerische Lücken und passen Angriffsziele an.
            **Trainer-Details:** Frage im Kreis: 'Wo steht die U13 schwach?' Fördert das Spielverständnis.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Timeout-Simulation"):
            st.markdown("""
            **Ablauf:** Teams nehmen selbst Timeouts und suchen taktische Lösungen.
            **Trainer-Details:** Misch dich nicht ein, hör nur zu.
            """)
        with st.expander("⚡ 6. Athletik I (15 Min): Final-Drill & Explosivität"):
            st.markdown("""
            **Ablauf:** Kurze Schnelligkeits-Parcours.
            **Trainer-Details:** ZNS wecken für das finale Match.
            """)
        with st.expander("⚡ 7. Athletik II (10 Min): Mobilisation & Cool-down"):
            st.markdown("""
            **Ablauf:** Ausgiebiges gemeinsames Dehnen (Mental Runterfahren).
            **Trainer-Details:** Fokus auf Schultern und Beine.
            """)
        with st.expander("🏆 8. Abschlussspiel (20 Min): TuB Bocholt Meisterschaft"):
            st.markdown("""
            **Ablauf:** 2 Gewinnsätze bis 15 Punkte. Profi-Schiedsrichterregeln.
            **Trainer-Details:** Zelebriere dieses Spiel! Pfeife sauber und ehre das Gewinner-Team.
            """)

# ---------------------------------------------------------
# MONAT 3: Out-of-System (Highball-Set & Bagger-Abwehr)
# ---------------------------------------------------------
elif monat == "Monat 3: Out-of-System (RTK: Highball-Set & Abwehr-Bagger)":
    st.header("Monat 3: Lösungen unter Stress")
    st.info("DVV RTK Fokus: Das Highball-Set (hoher Notpass) und der Abwehr-Bagger unter extremen Bedingungen.")
    
    w1, w2, w3, w4 = st.tabs(["Woche 1", "Woche 2", "Woche 3", "Woche 4"])
    
    # ---------------- WOCHE 1 ----------------
    with w1:
        st.subheader("TE 1 (90 Min): Chaos-Management & Highball")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Blickkontrolle & Athletik"):
            st.markdown("""
            **Ablauf:** Paarweises Baggern. A hält Finger hoch, B ruft Zahl.
            **Trainer-Details:** RTK fordert periphere Sicht. Der Spieler darf nicht nur den Ball anstarren, sondern muss das Feld scannen.
            """)
        with st.expander("🎯 2. Technik I (15 Min): Das Highball-Set (Trocken)"):
            st.markdown("""
            **Ablauf:** Trainer wirft Bälle tief ins Hinterfeld. Steller/Annahme spielt einen extrem hohen Pass (Highball) ans Netz (Pos IV).
            **Trainer-Details (RTK Highball):** Der Ball muss 2-3 Meter über der Antenne sein. Die Kraft kommt aus den Beinen! Schulterachse MUSS zum Ziel zeigen.
            """)
        with st.expander("🎯 3. Technik II (15 Min): Highball-Angriff"):
            st.markdown("""
            **Ablauf:** Angreifer muss den hohen Notpass erlaufen und sicher übers Netz bringen (kein Netzfehler!).
            **Trainer-Details:** Der Angreifer muss seinen Anlauf-Rhythmus an den Highball anpassen (später loslaufen!).
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Out-of-System Verteidigung"):
            st.markdown("""
            **Ablauf:** Trainer greift hart an. Abwehr-Bagger ins Zentrum, 2. Spieler macht das Highball-Set.
            **Trainer-Details (RTK Bagger):** In der Abwehr muss der Bagger nicht perfekt ans Netz, sondern hoch in die Mitte des Feldes gespielt werden.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Scramble Offense"):
            st.markdown("""
            **Ablauf:** Ball wird unkontrolliert eingeworfen. Team muss retten (Bagger) und über Highball angreifen.
            **Trainer-Details:** Kommunikation! Wer rettet den Ball? Wer spielt den Highball? Wer greift an?
            """)
        with st.expander("🏆 6. Abschlussspiel (20 Min): Profi-Kaiserplatz"):
            st.markdown("""
            **Ablauf:** Vollgas Turnier. Ball wird hart aufgeschlagen.
            **Trainer-Details:** Konsequentes Abpfeifen von Unsauberkeiten, um Wettkampfhärte zu erzeugen.
            """)

        st.divider()

        st.subheader("TE 2 - Freitag (120 Min): RTK Abwehr-Bagger & Sprint-Athletik")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Reaktions-Chaos"):
            st.markdown("""
            **Ablauf:** 2 Bälle gleichzeitig im 3er-Team jonglieren.
            **Trainer-Details:** Trainiert den Kopf unter Stress.
            """)
        with st.expander("🎯 2. Technik I (15 Min): Der seitliche Abwehr-Bagger"):
            st.markdown("""
            **Ablauf:** Bälle werden weit rechts/links geworfen. Spieler erläuft Ball mit langem Ausfallschritt und baggert am Körper vorbei.
            **Trainer-Details (RTK Bagger):** Den Ball außerhalb der Körperachse nehmen. Das Spielbrett wird seitlich gekippt, die Schulter zieht hoch.
            """)
        with st.expander("🎯 3. Technik II (15 Min): Not-Annahme am Boden (Sprawl)"):
            st.markdown("""
            **Ablauf:** Hechtbagger. Spieler gleitet auf der Brust ab und spielt den Ball hoch.
            **Trainer-Details:** RTK-Athletik: Körperkontrolle beim Fallen. Knie schützen!
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Transition mit Highball"):
            st.markdown("""
            **Ablauf:** Endlos-Butterfly. Abwehr -> Highball-Set -> Angriff.
            **Trainer-Details:** Das Umschalten (Transition) muss rasend schnell gehen.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Dauerfeuer-Abwehr"):
            st.markdown("""
            **Ablauf:** Trainer schießt 5 Bälle schnell hintereinander ab.
            **Trainer-Details:** Bagger-Plattform stabil halten, auch bei extremem Druck und Müdigkeit.
            """)
        with st.expander("⚡ 6. Athletik I (15 Min): DVV Sprint-Ausdauer"):
            st.markdown("""
            **Ablauf:** Linien-Pendel-Sprints. 
            **Trainer-Details (RTK Athletik):** Erschöpfungsresistenz trainieren. Ein Volleyballspiel wird oft im 3. Satz durch bessere Athletik gewonnen.
            """)
        with st.expander("⚡ 7. Athletik II (10 Min): Beinarbeit & Block"):
            st.markdown("""
            **Ablauf:** Schnelle laterale Sidesteps (Block-Vorbereitung).
            **Trainer-Details:** Tiefer Schwerpunkt beim seitlichen Verschieben.
            """)
        with st.expander("🏆 8. Abschlussspiel (20 Min): Out-of-System Bonus"):
            st.markdown("""
            **Ablauf:** Ein Punkt, der nach einer Rettungstat (Highball aus dem Hinterfeld) erzielt wird, zählt doppelt.
            **Trainer-Details:** Belohne den Mut, aus einer schlechten Situation das Beste (Highball-Angriff) zu machen.
            """)

    # ---------------- WOCHE 2 ----------------
    with w2:
        st.subheader("TE 3 (90 Min): Not-Pässe & Scramble Offense")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Ball-Klau im 3m-Raum"):
            st.markdown("""
            **Ablauf:** Dribbeln und anderen den Ball wegschlagen.
            **Trainer-Details:** Fördert Übersicht, Ballkontrolle und flinke Fußarbeit auf engem Raum.
            """)
        with st.expander("🎯 2. Technik I (15 Min): Den schlechten Pass erlaufen"):
            st.markdown("""
            **Ablauf:** Trainer wirft Bälle extrem streuend. Zuspieler/Mitspieler muss sprinten, abstoppen und den Not-Pass spielen.
            **Trainer-Details:** Wer im Vollsprint pritscht/baggert, produziert Doppelfehler. Abstoppen ist Pflicht!
            """)
        with st.expander("🎯 3. Technik II (15 Min): Angriff aus dem Hinterfeld"):
            st.markdown("""
            **Ablauf:** Wenn der Pass nicht ans Netz kommt: Angreifer drückt den Ball von der 3m-Linie lang ins gegnerische Feld.
            **Trainer-Details:** Die 'Push'-Technik zeigen: Ball tief greifen und im Bogen gezielt in die Ecken drücken (kein harter Schlag).
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Rettungsaktion -> Angriff"):
            st.markdown("""
            **Ablauf:** Annahme klebt im Netz/Aus. Spieler kratzt ihn hoch, der 3. Ball MUSS als bewusster Lob/Schlag rüber.
            **Trainer-Details:** Auch aus einem kaputten System heraus muss ein taktischer Ball gespielt werden.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Sicherung bei schlechten Pässen"):
            st.markdown("""
            **Ablauf:** Pass ist unpräzise. Die gesamte Mannschaft muss sofort Richtung Angreifer rücken, um abzusichern.
            **Trainer-Details:** Zwinge die Mitspieler, sich schützend tief um den Angreifer zu postieren (Block-Abpraller retten).
            """)
        with st.expander("🏆 6. Abschlussspiel (20 Min): Kein Dankeball"):
            st.markdown("""
            **Ablauf:** Wer einen Ball 'einfach so' per Bagger oder Dankeball rüberspielt, kassiert einen Minuspunkt.
            **Trainer-Details:** Hält die Disziplin extrem hoch. Ein Angreifer (auch gepusht/gedrückt) ist Pflicht.
            """)

        st.divider()

        st.subheader("TE 4 - Freitag (120 Min): RTK Fehlerkompensation & Rumpf")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Koordinations-Sprints"):
            st.markdown("""
            **Ablauf:** Sprints aus dem Sitzen, Liegen und Kniestand auf Kommando.
            **Trainer-Details:** Fordert maximale Explosivkraft aus ungewohnten Abwehr-Positionen.
            """)
        with st.expander("🎯 2. Technik I (15 Min): Tip/Lob aus der Not"):
            st.markdown("""
            **Ablauf:** Pass kommt zu nah ans Netz (Block wartet). Angreifer federt Ball sanft am Block vorbei.
            **Trainer-Details:** Bei nahen Pässen führt ein Vollschlag oft zum Block-Abpraller ins eigene Gesicht.
            """)
        with st.expander("🎯 3. Technik II (15 Min): Highball aus dem Bagger"):
            st.markdown("""
            **Ablauf:** Aus der tiefen Abwehrhaltung (auf Knien/nach Hechtbagger) den Ball hoch als Zuspiel baggern.
            **Trainer-Details:** Die Kraft muss hier massiv aus dem Rumpf und den Schultern kommen, da die Beine nicht helfen können.
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Butterfly unter Druck"):
            st.markdown("""
            **Ablauf:** Endlos-System. Team A wehrt ab und greift an. Fällt der Ball, rückt das wartende Team nach.
            **Trainer-Details:** Rotieren die Spieler schnell genug rein und raus, ohne sich im Weg zu stehen?
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Dauerfeuer-Rallye"):
            st.markdown("""
            **Ablauf:** Trainer schießt 5 Bälle pro Team in 10 Sekunden ein.
            **Trainer-Details:** Bringe sie an die Grenze. Sofortiges Reagieren, Abwehren und Umschalten.
            """)
        with st.expander("⚡ 6. Athletik I (15 Min): RTK Rumpf für Luftkontrolle"):
            st.markdown("""
            **Ablauf:** Bauchmuskel-Zirkel und Rückenstrecker (Supermans).
            **Trainer-Details:** Verhindert das Einknicken in der Luft (Bogenspannung halten) und schützt vor Rückenschmerzen.
            """)
        with st.expander("⚡ 7. Athletik II (10 Min): Explosive Richtungswechsel"):
            st.markdown("""
            **Ablauf:** T-Drill oder Hütchenlauf mit schnellen Richtungswechseln.
            **Trainer-Details:** Gelenke auf Stabilität unter Belastung schulen.
            """)
        with st.expander("🏆 8. Abschlussspiel (20 Min): Wash-Game Extrem"):
            st.markdown("""
            **Ablauf:** 3 Rallyes am Stück gewinnen für einen großen Punkt.
            **Trainer-Details:** Erfordert brutale Konstanz. Ermutige die Teams, zwischen den Rallyes durchzuatmen.
            """)

    # ---------------- WOCHE 3 ----------------
    with w3:
        st.subheader("TE 5 (90 Min): High-Speed Transition")
        with st.expander("🎾 1. Warm-up (10 Min): Volley-Tennis (Chaos)"):
            st.markdown("""
            **Ablauf:** 1v1 Chaos-Tennis. 1x Aufkommen erlaubt, alle Körperteile dürfen benutzt werden.
            **Trainer-Details:** Perfektes Mentaltraining nach der Schule. Reaktionsfähigkeit wird hochgefahren.
            """)
        with st.expander("🎯 2. Technik I (15 Min): Abwehr -> Sofort-Angriff"):
            st.markdown("""
            **Ablauf:** Spieler wehrt harten Ball ab, macht sofort (!) den 3er-Rhythmus und greift an.
            **Trainer-Details:** Aus der Hocke sofort aufrichten, nach hinten weg vom Netz lösen, um Anlauf nehmen zu können.
            """)
        with st.expander("🎯 3. Technik II (15 Min): Highball-Präzision"):
            st.markdown("""
            **Ablauf:** Aus der tiefen Abwehr heraus gezielt auf eine Matte (Pos IV) spielen.
            **Trainer-Details:** (RTK) Ballhöhe muss konstant 2-3 Meter über Antenne betragen.
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Aufschlagdruck vs. Transition"):
            st.markdown("""
            **Ablauf:** U14 feuert Aufschläge auf U13. U13 muss annehmen, aufbauen und sofort auf Abwehr umschalten.
            **Trainer-Details:** Eine Endlos-Schleife der Härte. Annahme-Technik darf nicht schlampig werden.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Rallye aufrechterhalten"):
            st.markdown("""
            **Ablauf:** Fokus: Ball unter allen Umständen im Spiel halten (Lobs, Sicherung, Hechtbagger).
            **Trainer-Details:** Belohne nur Ballwechsel, die über 4 Netzüberquerungen dauern.
            """)
        with st.expander("🏆 6. Abschlussspiel (20 Min): Speed-Turnier"):
            st.markdown("""
            **Ablauf:** Ball tot = Trainer wirft in Sekunde 1 den nächsten Ball ein.
            **Trainer-Details:** Wer jubelt oder sich ärgert, hat schon den nächsten Ball im Gesicht. Extrem hohe Dichte!
            """)

        st.divider()

        st.subheader("TE 6 - Freitag (120 Min): RTK Wettkampfhärte & Beine")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): 1v1 Auf-/Absteiger"):
            st.markdown("""
            **Ablauf:** Volley-Tennis im Turniermodus (Minifelder).
            **Trainer-Details:** Schnelle Auf-/Abstiege halten den Wettkampfgedanken frisch.
            """)
        with st.expander("🎯 2. Technik I (15 Min): Das Highball-Set unter Ermüdung"):
            st.markdown("""
            **Ablauf:** Spieler sprintet von Seitenlinie zu Seitenlinie und muss dann den Highball setzen.
            **Trainer-Details:** Wenn die Beine brennen, rettet die saubere RTK-Technik (Schulterachse) den Pass.
            """)
        with st.expander("🎯 3. Technik II (15 Min): Abwehr von Notschlägen"):
            st.markdown("""
            **Ablauf:** Trainer spielt Bälle aus extrem unvorteilhaften Winkeln. Abwehr muss sich anpassen.
            **Trainer-Details:** Die unberechenbaren Bälle simulieren das 'Scramble'-Spiel des Gegners.
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Out-of-System (6v6 Simulation)"):
            st.markdown("""
            **Ablauf:** 3v3 oder 4v4. Trainer greift hart ein, das System ist sofort gesprengt.
            **Trainer-Details:** Wie schnell findet die Mannschaft zurück in ihre Struktur?
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Fehlerketten durchbrechen"):
            st.markdown("""
            **Ablauf:** Nach einem eigenen Fehler serviert der Gegner sofort nochmal (Drucksituation).
            **Trainer-Details:** Lerne, nach einem Fehler durchzuatmen und den 'Reset-Knopf' im Kopf zu drücken.
            """)
        with st.expander("⚡ 6. Athletik I (15 Min): RTK Schnelle Füße"):
            st.markdown("""
            **Ablauf:** Skippings, High-Knees und kurze Antritt-Sprints am Netz.
            **Trainer-Details:** Letzter athletischer Reiz für die Beine vor dem Abschluss-Turnier.
            """)
        with st.expander("⚡ 7. Athletik II (10 Min): Sprungkraft-Endurance"):
            st.markdown("""
            **Ablauf:** Kontinuierliche Blocksprünge für 60 Sekunden (am Netz entlang).
            **Trainer-Details:** Simulieren die Belastung im 3. Satz.
            """)
        with st.expander("🏆 8. Abschlussspiel (20 Min): Transition-König"):
            st.markdown("""
            **Ablauf:** Punkt zählt erst, wenn der Ball mindestens 3x (pro Seite) über das Netz ging.
            **Trainer-Details:** Verhindert dumme Fehler im Aufschlag und erzwingt lange Rallyes.
            """)

    # ---------------- WOCHE 4 ----------------
    with w4:
        st.subheader("TE 7 (90 Min): Match-Day Vorbereitung (DVV RTK Checks)")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Pre-Game Routine"):
            st.markdown("""
            **Ablauf:** Komplettes offizielles Einschlagen (Paarweise -> Netz -> Aufschlag).
            **Trainer-Details:** Fokus liegt auf der Routine. Lass die Kinder den Ablauf selbstständig leiten.
            """)
        with st.expander("🎯 2. Technik I (15 Min): Der sichere Not-Aufschlag"):
            st.markdown("""
            **Ablauf:** Wenn die Luft raus ist: Sicherer Aufschlag, der zu 100% ins Feld muss.
            **Trainer-Details:** Zeige, wie man das Risiko komplett rausnimmt (ruhiger Anwurf, große Fläche anvisieren).
            """)
        with st.expander("🎯 3. Technik II (15 Min): RTK Highball-Check"):
            st.markdown("""
            **Ablauf:** Ein finaler Test: Jeder Spieler muss aus dem Hinterfeld einen perfekten Highball ans Netz liefern.
            **Trainer-Details:** Prüfe die RTK-Vorgaben: Höhe (2-3m über Antenne) und Schulterachse.
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Abstimmung U13/U14 Mix"):
            st.markdown("""
            **Ablauf:** Gemischte Teams (3v3 oder 4v4). Wer deckt welche Räume? Absprachen treffen.
            **Trainer-Details:** Lass die Teams ihre eigene Taktik besprechen. Schult das Spielverständnis.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Letzte Systemprüfung"):
            st.markdown("""
            **Ablauf:** Kurze 5-Punkte-Matches unter Wettkampfbedingungen.
            **Trainer-Details:** Greife nur bei gravierenden Stellungsfehlern ein.
            """)
        with st.expander("🏆 6. Abschlussspiel (20 Min): Liga Hinrunde"):
            st.markdown("""
            **Ablauf:** Start des großen Monats-Turniers. Jeder gegen Jeden.
            **Trainer-Details:** Führe eine echte Tabelle (Whiteboard). Motiviert für Freitag!
            """)

        st.divider()

        st.subheader("TE 8 - Freitag (120 Min): Das große DVV RTK Saison-Finale")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Turnier-Warm-up"):
            st.markdown("""
            **Ablauf:** Fokus und Konzentration. Dynamisches Einspielen.
            **Trainer-Details:** Achte auf Körperspannung. Keine lockeren Faxen am Netz.
            """)
        with st.expander("🎯 2. Technik I (15 Min): Feinschliff & Duelle (Angriff)"):
            st.markdown("""
            **Ablauf:** Angreifer gegen Blockspieler. Direkte 1v1 Duelle zur Schärfung.
            **Trainer-Details:** Gib den Spielern Selbstvertrauen in ihre Waffen. Lobe gute Aktionen laut!
            """)
        with st.expander("🎯 3. Technik II (15 Min): Feinschliff & Duelle (Aufschlag)"):
            st.markdown("""
            **Ablauf:** Aufschläger gegen Annahmeriegel. 
            **Trainer-Details:** Fokus auf die RTK-Aufschlagbewegung und das Bagger-Spielbrett.
            """)
        with st.expander("🧠 4. Taktik I (15 Min): Timeout-Coaching"):
            st.markdown("""
            **Ablauf:** Teams simulieren Spielstände. Sie nehmen selbst Timeouts und suchen taktische Lösungen.
            **Trainer-Details:** Misch dich nicht ins Timeout ein. Hör zu, wie sie kommunizieren.
            """)
        with st.expander("🧠 5. Taktik II (15 Min): Mental-Stärke Check"):
            st.markdown("""
            **Ablauf:** 'Es steht 24:24'. Wer fordert den Ball? Wer macht den Punkt?
            **Trainer-Details:** Beobachte die Schlüsselspieler in Drucksituationen.
            """)
        with st.expander("⚡ 6. Athletik I (15 Min): RTK Explosivität"):
            st.markdown("""
            **Ablauf:** Letzte kurze Sprintserie.
            **Trainer-Details:** Muskulatur aktivieren, Spannung aufbauen.
            """)
        with st.expander("⚡ 7. Athletik II (10 Min): Cool-down & Mentaler Fokus"):
            st.markdown("""
            **Ablauf:** 10 Minuten ausgiebiges gemeinsames Dehnen.
            **Trainer-Details:** Lass die Spieler das Dehnen abwechselnd anleiten. Kopf runterfahren.
            """)
        with st.expander("🏆 8. Abschlussspiel (20 Min): Liga Finale (Meisterschaft)"):
            st.markdown("""
            **Ablauf:** Die Rückrunde. 2 Gewinnsätze, volle Regeln, absolute Wettkampfbedingungen.
            **Trainer-Details:** Kröne den Monats-Sieger! Du agierst als Schiedsrichter und zelebrierst das Spiel.
            """)

# ---------------------------------------------------------
# SYSTEM-SPEZIAL
# ---------------------------------------------------------
elif monat == "System-Spezial: 3v3 meets 4v4":
    st.header("System-Spezial: Transition & Kognition")
    st.info("DVV RTK Fokus: Das 'Spiel lesen' und Schnittstellen-Koordination zwischen Altersklassen.")
    
    with st.expander("⏱️ 1. Der Transition-Läufer (U13 & U14) (15 Min)"):
        st.markdown("""
        **Aus der Abwehr ins Zuspiel:** Trainer greift auf Zuspieler an. Dieser wehrt ab, Mitspieler übernimmt Highball-Set.
        **Trainer-Details:** Zwingt den Zuspieler, erst Abwehrspieler (Bagger) zu sein, anstatt wegzulaufen.
        """)
    with st.expander("👀 2. Das Scanner-Zuspiel (20 Min)"):
        st.markdown("""
        **Block lesen:** Trainer hebt linke/rechte Hand. Zuspieler pritscht dorthin, wo die Hand *unten* ist.
        **Trainer-Details (RTK Kognition):** Blick weg vom Ball, rein ins Feld.
        """)
    with st.expander("🏆 3. Spielform: Der Libero-Joker (20 Min)"):
        st.markdown("""
        **3v3 mit Abwehr-Chef:** Ein U14-Spieler sichert hinten als Libero ab (Fokus: Abwehr-Bagger).
        **Trainer-Details:** Die U14 übernimmt Verantwortung in der RTK Abwehr-Technik.
        """)
