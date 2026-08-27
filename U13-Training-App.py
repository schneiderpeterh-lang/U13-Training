import streamlit as st

# Seiten-Konfiguration
st.set_page_config(page_title="U13/U14 Trainingsplan", page_icon="🏐", layout="centered")

st.title("🏐 U13/U14 PRO Plan")
st.markdown("TuB Bocholt | 2x pro Woche (TE 1: 90 Min, TE 2 Freitag: 120 Min)")

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
# MONAT 1: Annahme & System
# ---------------------------------------------------------
if monat == "Monat 1: Annahme-Präzision & System-Start":
    st.header("Monat 1: Gezielte Annahme zum Steller")
    
    w1, w2, w3, w4 = st.tabs(["Woche 1", "Woche 2", "Woche 3", "Woche 4"])
    
    # [Der Code für Monat 1 bleibt exakt wie im vorherigen Schritt]
    with w1:
        st.subheader("TE 1 (90 Min): Das sichere Spielbrett")
        with st.expander("🏃‍♂️ 1. Warm-up: Reaktions-Baggern (10 Min)"):
            st.markdown("**Gemeinsam:** Paarweise. Spieler A wirft leicht seitlich. Spieler B macht schnellen Sidestep, formt das Spielbrett und baggert präzise zurück.")
        with st.expander("🎯 2. Technik: Ziel-Baggern zum Steller (30 Min)"):
            st.markdown("**Gemeinsam:** Kasten auf Pos II/III. Trainer wirft Bälle an. Armwinkel so ausrichten, dass der Ball im hohen Bogen genau auf das Steller-Ziel fällt.")
        with st.expander("🧠 3. Taktik: Annahme-Riegel formieren (30 Min)"):
            st.markdown("**Split:** Seite A (U14 - 3er Riegel), Seite B (U13 - 2er Riegel). Trainer schlägt leichte Bälle ein. Fokus: Lautes Rufen ('Ich!') und Pass zum Steller (dieser fängt).")
        with st.expander("🏆 4. Abschlussspiel: Annahme-Bingo (20 Min)"):
            st.markdown("**Punkte-Regel:** 3v3/4v4. Zusatzpunkt, wenn die Annahme perfekt beim Zuspieler landet (ohne dass dieser laufen muss).")

        st.divider()
        st.subheader("TE 2 - Freitag (120 Min): Annahme unter Druck & Athletik")
        with st.expander("🏃‍♂️ 1. Warm-up: Tiefe Abwehr & Linien-Chaos (15 Min)"):
            st.markdown("**Gemeinsam:** Linienfangen kombiniert mit Sidesteps und tiefem Abwehr-Stopp auf Pfiff. Tiefe Haltung permanent einfordern.")
        with st.expander("🎯 2. Technik: Dankeball-Sprint & Annahme (35 Min)"):
            st.markdown("**Gemeinsam:** Spieler startet Grundlinie. Trainer ruft 'Go!' und wirft kurz hinters Netz. Spieler sprintet, stoppt komplett ab und baggert hoch zum Steller.")
        with st.expander("🧠 3. Taktik: Serve & Pass Komplex (35 Min)"):
            st.markdown("**Split:** U14 schlägt von oben auf. U13 kontrolliert harte Aufschläge. Fokus: Keine Arm-Bewegung beim Baggern harter Bälle, nur vom Spielbrett abprallen lassen!")
        with st.expander("⚡ 4. Athletik & Aufschlag-Präzision (15 Min)"):
            st.markdown("**Freitags-Special:** 3 Runden Rumpf- & Sprungkraft (Plank, Ausfallschritte, Blocksprünge). Danach sofort 5 Ziel-Aufschläge mit erhöhtem Puls.")
        with st.expander("🏆 5. Abschlussspiel: Handicap-Match (20 Min)"):
            st.markdown("**4v3:** U14 gegen U13. Wenn die Annahme der U13 wackelt, schlägt U14 nur von unten auf, um den sauberen Aufbau zu erzwingen.")

    with w2:
        st.subheader("TE 3 (90 Min): Zuspieler-Integration")
        with st.expander("🏃‍♂️ 1. Warm-up: Kognitives Chaos (10 Min)"):
            st.markdown("**Gemeinsam:** Paarweise am Netz. A pritscht Ball 1, B rollt Ball 2. Auf Pfiff: Sprint zur Grundlinie und zurück.")
        with st.expander("🎯 2. Technik: Annahme + Zuspiel (30 Min)"):
            st.markdown("**Gemeinsam:** Annahme baggert zum Steller. Der Steller pritscht den Ball hoch auf Pos IV in Ballwagen/Korb. Steller muss vor dem Pass stehen!")
        with st.expander("🧠 3. Taktik: Mixed-System Laufwege (30 Min)"):
            st.markdown("**Split:** Seite A (U14 Raute), Seite B (U13 Läufer). Trainer wirft ein. Steller läuft erst los, wenn der Ball den Trainer verlässt.")
        with st.expander("🏆 4. Abschlussspiel: Wash-Game (20 Min)"):
            st.markdown("**Punkte-Regel:** 2 Rallyes in Folge gewinnen = 1 Punkt. Fördert die Konzentration.")

        st.divider()
        st.subheader("TE 4 - Freitag (120 Min): System-Festigung & Dauerbelastung")
        with st.expander("🏃‍♂️ 1. Warm-up: Aufschlag-Staffel & Koordination (15 Min)"):
            st.markdown("**Gemeinsam:** Staffel mit Ball prellen, Anwurf-Simulation am Netz und schnellen Richtungswechseln.")
        with st.expander("🎯 2. Technik: Zonen-Aufschlag vs. Annahme (35 Min)"):
            st.markdown("**Gemeinsam:** U14 schlägt gezielt auf Turnmatten in den Ecken. U13 steht in Annahme und versucht die Matten zu verteidigen.")
        with st.expander("🧠 3. Taktik: Rette das System (Out-of-System) (35 Min)"):
            st.markdown("**Split:** Trainer wirft unpräzise Bälle (Netz, Aus). Annahme ist unsauber. Ein anderer Spieler muss laut 'Hilfe' rufen und das Zuspiel übernehmen.")
        with st.expander("⚡ 4. Athletik: Beinarbeit & Quickness (15 Min)"):
            st.markdown("**Freitags-Special:** Koordinationsleiter/Linien-Drills für schnelle Fußarbeit + Medizinball-/Ball-Würfe aus den Beinen.")
        with st.expander("🏆 5. Abschlussspiel: System-Kaiser (20 Min)"):
            st.markdown("**Sonderregel:** Herausforderer rücken nur auf Kaiser-Seite vor, wenn der Ball im 3er-System aufgebaut wurde.")

    with w3:
        st.subheader("TE 5 (90 Min): Annahme-Konstanz")
        with st.expander("🏃‍♂️ 1. Warm-up: Reaktions-Sprints (10 Min)"):
            st.markdown("**Gemeinsam:** Bauchlage am Netz. Auf Pfiff: Aufstehen, Rückwärtslauf bis 3m-Linie, Vorwärtssprint.")
        with st.expander("🎯 2. Technik: Annahme aus der Bewegung (30 Min)"):
            st.markdown("**Gemeinsam:** Spieler laufen seitlich in den Ballweg ein und stabilisieren das Spielbrett im Moment des Kontakts.")
        with st.expander("🧠 3. Taktik: Aufschlag-Druck vs. Annahme-Riegel (30 Min)"):
            st.markdown("**Split:** Annahmeriegel muss sich aktiv verschieben, wenn der Aufschläger seine Position an der Grundlinie verändert.")
        with st.expander("🏆 4. Abschlussspiel: Druck-Turnier (20 Min)"):
            st.markdown("**Punkte-Regel:** Annahmefehler (direktes As) gibt 2 Punkte für das aufschlagende Team.")

        st.divider()
        st.subheader("TE 6 - Freitag (120 Min): Transition Defensive -> Annahme")
        with st.expander("🏃‍♂️ 1. Warm-up: 1v1 Volley-Tennis (15 Min)"):
            st.markdown("**Gemeinsam:** 1v1 in kleinen Feldern. Ball darf 1x tippen. Alle Körperteile erlaubt.")
        with st.expander("🎯 2. Technik: Not-Annahme am Boden (35 Min)"):
            st.markdown("**Gemeinsam:** Hechtbagger und einarmige Rettungsaktionen mit kontrolliertem hohen Ballbogen ins Zentrum.")
        with st.expander("🧠 3. Taktik: Umschaltspiel nach Abwehr (35 Min)"):
            st.markdown("**Split:** Aus der Feldabwehr heraus sofort wieder in die Annahme-Struktur für den zweiten Ball formieren.")
        with st.expander("⚡ 4. Athletik: Rumpfstabilität & Schultern (15 Min)"):
            st.markdown("**Freitags-Special:** Kräftigung Rotatorenmanschette mit Thera-Bändern/Bällen + Unterarmstütz-Variationen.")
        with st.expander("🏆 5. Abschlussspiel: Transition-Match (20 Min)"):
            st.markdown("**Modus:** 3v3/4v4. Schneller Ballwechsel-Rhythmus mit Trainer-Einwurf sofort nach Rallye-Ende.")

    with w4:
        st.subheader("TE 7 (90 Min): Match-Simulation")
        with st.expander("🏃‍♂️ 1. Warm-up: Pre-Game Einspielen (10 Min)"):
            st.markdown("**Gemeinsam:** Paarweises Warmspielen mit Fokus auf präzisen ersten Ballkontakt.")
        with st.expander("🎯 2. Technik: Annahme-Präzisions-Test (30 Min)"):
            st.markdown("**Gemeinsam:** Jeder Spieler muss 10 Aufschläge annehmen; gezählt wird, wie viele perfekt im Zielkreis landen.")
        with st.expander("🧠 3. Taktik: Abstimmung U13/U14 (30 Min)"):
            st.markdown("**Split:** Gemischte Teams spielen mit festen Schnittstellen-Absprachen (wer nimmt Bälle in der Mitte?).")
        with st.expander("🏆 4. Abschlussspiel: TuB Bocholt Liga (20 Min)"):
            st.markdown("**Turnier:** Spiel auf Zeit (4 Min pro Match). Kaiserplatz-System.")

        st.divider()
        st.subheader("TE 8 - Freitag (120 Min): Der große Monatstest")
        with st.expander("🏃‍♂️ 1. Warm-up: Turnier-Warm-up (15 Min)"):
            st.markdown("**Gemeinsam:** Dynamisches Dehnen, Einschlagen am Netz mit Zuspiel aus der Annahme.")
        with st.expander("🎯 2. Technik: Aufschlag & Annahme Feinschliff (35 Min)"):
            st.markdown("**Gemeinsam:** Duelle: Aufschläger gegen 2er/3er Annahmeriegel. Punkte für Ass vs. perfekte Annahme.")
        with st.expander("🧠 3. Taktik: Spielaufbau unter Wettkampfstress (35 Min)"):
            st.markdown("**Split:** Spielstände simulieren ('23:23'). Annahme MUSS sitzen, um Sideout zu schaffen.")
        with st.expander("⚡ 4. Athletik & Auslockern (15 Min)"):
            st.markdown("**Freitags-Special:** Kurze explosive Sprungserie (3x5 Hocksprünge) + Partner-Dehnen.")
        with st.expander("🏆 5. Abschlussspiel: Monats-Finale (20 Min)"):
            st.markdown("**Wettkampf:** 2 Gewinnsätze bis 15 Punkte. Volle Anwendung aller Regeln.")

# ---------------------------------------------------------
# MONAT 2: Grundtechnik Angriff & Aufschlag
# ---------------------------------------------------------
elif monat == "Monat 2: Grundtechnik Angriff & Aufschlag":
    st.header("Monat 2: Schlagen über das Netz")
    
    w1, w2, w3, w4 = st.tabs(["Woche 1", "Woche 2", "Woche 3", "Woche 4"])
    
    # [Der Code für Monat 2 bleibt exakt wie im vorherigen Schritt]
    with w1:
        st.subheader("TE 1 (90 Min): Der Armzug")
        with st.expander("🏃‍♂️ 1. Warm-up: Schulter-Aktivierung (10 Min)"):
            st.markdown("**Gemeinsam:** Einarmiges Baseball-Werfen paarweise. Fokus auf Aufdrehen der Schulterachse.")
        with st.expander("🎯 2. Technik: Wand-Schlagen (30 Min)"):
            st.markdown("**Gemeinsam:** Vor der Wand: Hoher Ellenbogen, Handgelenk klappt aktiv ab, Ball tippt vor Wand auf den Boden.")
        with st.expander("🧠 3. Taktik/Technik: Schlagen aus dem Stand (30 Min)"):
            st.markdown("**Gemeinsam:** Trainer wirft auf Pos IV. Spieler machen Stemmschritt aus dem Stand und schlagen mit Handgelenkseinsatz übers Netz.")
        with st.expander("🏆 4. Abschlussspiel: Angriffs-Bingo (20 Min)"):
            st.markdown("**Punkte-Regel:** 3v3/4v4. Punkte zählen nur bei geschlagenem Ball oder aggressivem Angriff.")

        st.divider()
        st.subheader("TE 2 - Freitag (120 Min): Der 3er-Anlauf & Sprungkraft")
        with st.expander("🏃‍♂️ 1. Warm-up: Rhythmus-Schulung (15 Min)"):
            st.markdown("**Gemeinsam:** Anlauf-Rhythmus trocken ('Links... Rechts-Links!'). Steigerung mit explosivem Armschwung nach oben.")
        with st.expander("🎯 2. Technik: Anlauf, Absprung & Schlag (35 Min)"):
            st.markdown("**Gemeinsam:** Zuspieler wirft Bogenbälle. Angreifer läuft aus 3m-Distanz an, springt beidbeinig ab und schlagen.")
        with st.expander("🧠 3. Taktik: Hit or Lob (35 Min)"):
            st.markdown("**Split:** Trainer signalisiert Block. Hand oben = gezielter Lob in die Lücke. Hand unten = voller Schlagangriff.")
        with st.expander("⚡ 4. Athletik: Sprungkraft & Rumpf (15 Min)"):
            st.markdown("**Freitags-Special:** Box-Jumps (auf Weichboden/Kasten) + Core-Stabi für die Bogen-Spannung in der Luft.")
        with st.expander("🏆 5. Abschlussspiel: Angriffs-Turnier (20 Min)"):
            st.markdown("**Modus:** 3v3/4v4. Erfolgreiche Angriffsschläge aus vollem Anlauf zählen 2 Punkte.")

    with w2:
        st.subheader("TE 3 (90 Min): Aufschlag-Härte")
        with st.expander("🏃‍♂️ 1. Warm-up: Hechten & Block-Schatten (10 Min)"):
            st.markdown("**Gemeinsam:** Blocksprung am Netz, landen, rückwärts ausweichen, Abwehrhecht auf den Boden, schnell hoch.")
        with st.expander("🎯 2. Technik: Tennis-Aufschlag (30 Min)"):
            st.markdown("**Gemeinsam:** Aufschlag von oben ab 3m-Linie. Anwurf vor dem Körper. Bei 3 Treffern 1 Meter nach hinten gehen.")
        with st.expander("🧠 3. Taktik: Aufschlag vs. Riegel (30 Min)"):
            st.markdown("**Split:** Team A schlägt hart von oben auf. Team B kontrolliert die Annahme auf den Steller.")
        with st.expander("🏆 4. Abschlussspiel: Aufschlag-Kaiser (20 Min)"):
            st.markdown("**Direkter As-Wechsel:** Kaiserplatz. Direktes Aufschlag-Ass bringt sofortigen Wechsel auf die Kaiserseite.")

        st.divider()
        st.subheader("TE 4 - Freitag (120 Min): Komplex-Training & Sicherung")
        with st.expander("🏃‍♂️ 1. Warm-up: Reaktions-Baggern & Sprints (15 Min)"):
            st.markdown("**Gemeinsam:** Schnelle Sidesteps, Spielbrett stabilisieren, gefolgt von kurzen Sprints ans Netz.")
        with st.expander("🎯 2. Technik: Freeball-Kill im Ablauf (35 Min)"):
            st.markdown("**Gemeinsam:** Trainer schlägt Dankeball ein. Komplette Kette: Annahme -> Zuspiel -> voller Schlagangriff.")
        with st.expander("🧠 3. Taktik: Die Angriffssicherung (35 Min)"):
            st.markdown("**Split:** Angreifer schlägt in Doppelblock. 2-3 Mitspieler sichern tief ab und kratzen Abpraller hoch.")
        with st.expander("⚡ 4. Athletik: Schulter-Power & Wurfkraft (15 Min)"):
            st.markdown("**Freitags-Special:** Einarmige Medizinballwürfe über das Netz + Kräftigung oberer Rücken.")
        with st.expander("🏆 5. Abschlussspiel: Wash-Game Extrem (20 Min)"):
            st.markdown("**Turnier:** 2 Rallyes in Folge für Punktgewinn. Block- und Sicherungsaktionen geben Zusatzpunkte.")

    with w3:
        st.subheader("TE 5 (90 Min): Reaktion & Abwehr")
        with st.expander("🎾 1. Warm-up: 1-gegen-1 Kreatives Tennis Game (10 Min)"):
            st.markdown("**Gamification:** Feld in 4-5 Schläuche teilen. 1v1. Ball darf 1x aufkommen. Schult periphere Sicht.")
        with st.expander("🎯 2. Technik: Schmetter-Abwehr (30 Min)"):
            st.markdown("**Gemeinsam:** Spieler stehen tief auf Pos I/V. Trainer schlägt gezielt hart an. Arme ruhig halten, abprallen lassen.")
        with st.expander("🧠 3. Taktik: Abwehr -> Transition (30 Min)"):
            st.markdown("**Split:** Harter Angriff -> Abwehr ins Zentrum -> Notzuspiel -> Gegenangriff über außen.")
        with st.expander("🏆 4. Abschlussspiel: Abwehr-König (20 Min)"):
            st.markdown("**Sonderregel:** Spektakuläre Abwehraktionen mit erfolgreichem Gegenangriff geben 2 Punkte.")

        st.divider()
        st.subheader("TE 6 - Freitag (120 Min): Block-Timing & Feldverteidigung")
        with st.expander("🏃‍♂️ 1. Warm-up: 1v1 Tennis Auf-/Absteiger (15 Min)"):
            st.markdown("**Gemeinsam:** Kreatives Tennis-Game im Turniermodus über 15 Minuten. Sieger rückt ein Feld nach rechts.")
        with st.expander("🎯 2. Technik: Der 1er- und 2er-Block (35 Min)"):
            st.markdown("**Gemeinsam:** Timing beim Absprung, Hände fest über das Netz schieben.")
        with st.expander("🧠 3. Taktik: Block-Abwehr-Dreieck (35 Min)"):
            st.markdown("**Split:** U14 stellt Doppelblock, U13 stellt 1er-Block mit V-Abwehr dahinter. Lobs ablaufen.")
        with st.expander("⚡ 4. Athletik: Sprungausdauer am Netz (15 Min)"):
            st.markdown("**Freitags-Special:** Serien aus Blocksprüngen mit lateralen Sidesteps.")
        with st.expander("🏆 5. Abschlussspiel: Block & Defense Match (20 Min)"):
            st.markdown("**Modus:** 3v3/4v4. Kill-Blocks zählen doppelt.")

    with w4:
        st.subheader("TE 7 (90 Min): Entscheidungsfindung")
        with st.expander("🏃‍♂️ 1. Warm-up: 1v1 Tennis Game (10 Min)"):
            st.markdown("**Gemeinsam:** Schnelles Warm-up mit vollem Körpereinsatz im 1-gegen-1.")
        with st.expander("🎯 2. Technik: Hit or Lob Präzision (30 Min)"):
            st.markdown("**Gemeinsam:** Angreifer entscheidet in der Luft: Harter Schlag oder gezielter Tip über den Block.")
        with st.expander("🧠 3. Taktik: Systemprüfung unter Druck (30 Min)"):
            st.markdown("**Split:** Trainer serviert variabel. Teams müssen Annahme, Zuspiel und Angriff fehlerfrei durchbringen.")
        with st.expander("🏆 4. Abschlussspiel: TuB Bocholt Liga (20 Min)"):
            st.markdown("**Turnier:** Reiner Wettkampf 3v3/4v4.")

        st.divider()
        st.subheader("TE 8 - Freitag (120 Min): Das große Finale")
        with st.expander("🏃‍♂️ 1. Warm-up: Pre-Game Routine & Einschlagen (15 Min)"):
            st.markdown("**Gemeinsam:** Offizieller Spieltags-Ablauf: Paare einspielen, Angriffsschläge am Netz.")
        with st.expander("🎯 2. Technik: Nervenstarker Aufschlag (35 Min)"):
            st.markdown("**Drucksituation:** '14:14'. 5 harte Aufschläge fehlerfrei ins Zielfeld platzieren.")
        with st.expander("🧠 3. Taktik: Match-Taktik & Coaching (35 Min)"):
            st.markdown("**Split:** Teams analysieren gegnerische Lücken selbstständig und passen Angriffsziele an.")
        with st.expander("⚡ 4. Athletik: Final-Drill & Mobilisation (15 Min)"):
            st.markdown("**Freitags-Special:** Schnelligkeits-Parcours + Dehnen.")
        with st.expander("🏆 5. Abschlussspiel: TuB Bocholt Meisterschaft (20 Min)"):
            st.markdown("**Das große Finale:** 2 Gewinnsätze bis 15 Punkte. Profi-Schiedsrichterregeln.")

# ---------------------------------------------------------
# MONAT 3: Out-of-System & Match-Speed (NEU)
# ---------------------------------------------------------
elif monat == "Monat 3: Out-of-System & Match-Speed":
    st.header("Monat 3: Lösungen unter Stress")
    
    w1, w2, w3, w4 = st.tabs(["Woche 1", "Woche 2", "Woche 3", "Woche 4"])
    
    # ---------------- WOCHE 1 ----------------
    with w1:
        st.subheader("TE 1 (90 Min): Chaos-Management")
        with st.expander("🏃‍♂️ 1. Warm-up: Blickkontrolle (10 Min)"):
            st.markdown("**Gemeinsam:** Paarweises Baggern. A hält vor Ballkontakt Finger hoch, B muss rufen wie viele. Schult periphere Sicht.")
        with st.expander("🎯 2. Technik: Out-of-System Pass (30 Min)"):
            st.markdown("**Gemeinsam:** Trainer wirft tief ins Hinterfeld. Steller (oder Annahme) muss hohen Not-Pass an die Antenne (Pos IV/II) spielen. Schulter zum Ziel!")
        with st.expander("🧠 3. Taktik: Freeball-Kill unter Zeitdruck (30 Min)"):
            st.markdown("**Split:** Trainer schlägt Dankeball ein. U14 hat exakt 3 Sekunden, U13 hat 4 Sekunden für Annahme, Zuspiel und Angriff.")
        with st.expander("🏆 4. Abschlussspiel: Profi-Kaiserplatz (20 Min)"):
            st.markdown("**Turnier:** Ball wird per Aufschlag von oben ins Spiel gebracht. Übertreten und Netzfehler konsequent abpfeifen.")

        st.divider()

        st.subheader("TE 2 - Freitag (120 Min): Not-Pässe & Physis")
        with st.expander("🏃‍♂️ 1. Warm-up: Reaktions-Chaos (15 Min)"):
            st.markdown("**Gemeinsam:** 2 Bälle gleichzeitig im 3er-Team jonglieren (pritschen/baggern). Hohe Kommunikation gefordert.")
        with st.expander("🎯 2. Technik: Den schlechten Pass erlaufen (35 Min)"):
            st.markdown("**Gemeinsam:** Trainer wirft Bälle extrem streuend. Zuspieler muss sprinten, komplett abstoppen (!) und den Not-Pass spielen.")
        with st.expander("🧠 3. Taktik: Butterfly unter Druck (35 Min)"):
            st.markdown("**Split:** Endlos-System. Team A wehrt ab und greift an. Fällt der Ball, rückt sofort das wartende Team nach.")
        with st.expander("⚡ 4. Athletik: Sprint-Ausdauer (15 Min)"):
            st.markdown("**Freitags-Special:** Linien-Pendel-Sprints (Linien antippen). Zielt auf Erschöpfungsresistenz im 3. Satz.")
        with st.expander("🏆 5. Abschlussspiel: Out-of-System Bonus (20 Min)"):
            st.markdown("**Sonderregel:** Ein Punkt, der nach einem völlig verunglückten ersten Ball (Rettungstat) erzielt wird, zählt doppelt.")

    # ---------------- WOCHE 2 ----------------
    with w2:
        st.subheader("TE 3 (90 Min): Scramble Offense")
        with st.expander("🏃‍♂️ 1. Warm-up: Ball-Klau im 3m-Raum (10 Min)"):
            st.markdown("**Gemeinsam:** Dribbeln und anderen den Ball wegschlagen. Fördert Übersicht und Fußarbeit.")
        with st.expander("🎯 2. Technik: Angriff aus dem Hinterfeld (30 Min)"):
            st.markdown("**Gemeinsam:** Wenn der Pass nicht ans Netz kommt: Angreifer muss lernen, den Ball von der 3m-Linie oder aus dem Stand lang ins gegnerische Feld zu drücken.")
        with st.expander("🧠 3. Taktik: Rettungsaktion -> Angriff (30 Min)"):
            st.markdown("**Split:** Annahme klebt im Netz oder fliegt Richtung Aus. Spieler kratzt ihn hoch, der 3. Ball *muss* als bewusster Lob/Schlag rüber.")
        with st.expander("🏆 4. Abschlussspiel: Kein Dankeball (20 Min)"):
            st.markdown("**Punkte-Regel:** Wer einen Ball 'einfach so' per Bagger oder als Dankeball rüberspielt, kassiert einen Minuspunkt. Es muss immer aufgebaut werden.")

        st.divider()

        st.subheader("TE 4 - Freitag (120 Min): Fehlerkompensation & Rumpf")
        with st.expander("🏃‍♂️ 1. Warm-up: Koordinations-Sprints (15 Min)"):
            st.markdown("**Gemeinsam:** Sprints aus dem Sitzen, Liegen und Kniestand auf Kommando.")
        with st.expander("🎯 2. Technik: Tip/Lob aus der Not (35 Min)"):
            st.markdown("**Gemeinsam:** Der Pass kommt zu nah ans Netz (Block wartet). Angreifer muss abspringen und den Ball clever ins Zentrum der Gegner tippen.")
        with st.expander("🧠 3. Taktik: Sicherung bei schlechten Pässen (35 Min)"):
            st.markdown("**Split:** Pass ist unpräzise. Die gesamte Mannschaft muss sofort 2 Schritte Richtung Angreifer rücken, um ihn abzusichern, falls er geblockt wird.")
        with st.expander("⚡ 4. Athletik: Rumpf für die Luftkontrolle (15 Min)"):
            st.markdown("**Freitags-Special:** Bauchmuskel-Zirkel und Rückenstrecker (Supermans) für Körperkontrolle in der Luft.")
        with st.expander("🏆 5. Abschlussspiel: Wash-Game Extrem (20 Min)"):
            st.markdown("**Turnier:** 3 Rallyes am Stück gewinnen für einen großen Punkt. Absolute Nervenprobe.")

    # ---------------- WOCHE 3 ----------------
    with w3:
        st.subheader("TE 5 (90 Min): High-Speed Transition")
        with st.expander("🎾 1. Warm-up: Volley-Tennis (10 Min)"):
            st.markdown("**Gemeinsam:** 1v1 Chaos-Tennis. 1x Aufkommen erlaubt, alle Körperteile dürfen benutzt werden.")
        with st.expander("🎯 2. Technik: Abwehr -> Sofort-Angriff (30 Min)"):
            st.markdown("**Gemeinsam:** Spieler wehrt harten Ball ab, macht sofort (!) den 3er-Rhythmus und greift den gestellten Notpass an.")
        with st.expander("🧠 3. Taktik: Dauerfeuer (30 Min)"):
            st.markdown("**Split:** Trainer wirft 5 Bälle pro Team in 10 Sekunden ein. Sofortiges Reagieren, Abwehren und Umschalten gefordert.")
        with st.expander("🏆 4. Abschlussspiel: Speed-Turnier (20 Min)"):
            st.markdown("**Modus:** 3v3 / 4v4. Ball tot = Trainer wirft sofort in Sekunde 1 den nächsten Ball ein. Keine Zeit zum Durchatmen.")

        st.divider()

        st.subheader("TE 6 - Freitag (120 Min): Wettkampfhärte & Beine")
        with st.expander("🏃‍♂️ 1. Warm-up: 1v1 Auf-/Absteiger (15 Min)"):
            st.markdown("**Gemeinsam:** Volley-Tennis im Turniermodus (Minifelder).")
        with st.expander("🎯 2. Technik: Aufschlagdruck vs. Transition (35 Min)"):
            st.markdown("**Gemeinsam:** U14 feuert Aufschläge auf U13. U13 muss annehmen, aufbauen und sofort auf eine erneute Abwehraktion umschalten.")
        with st.expander("🧠 3. Taktik: Rallye aufrechterhalten (35 Min)"):
            st.markdown("**Split:** Fokus liegt darauf, den Ball unter allen Umständen im Spiel zu halten. Lobs, Blocksicherung und Hechtbagger.")
        with st.expander("⚡ 4. Athletik: Schnelle Füße (15 Min)"):
            st.markdown("**Freitags-Special:** Skippings, High-Knees und kurze Antritt-Sprints am Netz.")
        with st.expander("🏆 5. Abschlussspiel: Transition-König (20 Min)"):
            st.markdown("**Modus:** Ein Punkt zählt erst, wenn der Ball mindestens 3x (pro Seite) über das Netz ging (lange Rallye erzwungen).")

    # ---------------- WOCHE 4 ----------------
    with w4:
        st.subheader("TE 7 (90 Min): Match-Day Vorbereitung")
        with st.expander("🏃‍♂️ 1. Warm-up: Pre-Game Routine (10 Min)"):
            st.markdown("**Gemeinsam:** Komplettes offizielles Einschlagen (Paarweise -> Netz -> Aufschlag).")
        with st.expander("🎯 2. Technik: Der sichere Not-Aufschlag (30 Min)"):
            st.markdown("**Gemeinsam:** Wenn die Luft raus ist: Sicherer Aufschlag von unten oder leichter Float, der zu 100% ins Feld muss.")
        with st.expander("🧠 3. Taktik: Abstimmung U13/U14 Mix (30 Min)"):
            st.markdown("**Split:** Gemischte Teams (3v3 oder 4v4). Wer deckt welche Räume? Absprachen für das Abschluss-Turnier treffen.")
        with st.expander("🏆 4. Abschlussspiel: Liga Hinrunde (20 Min)"):
            st.markdown("**Turnier:** Start des großen Monats-Turniers. Jeder gegen Jeden. Punkte notieren!")

        st.divider()

        st.subheader("TE 8 - Freitag (120 Min): Das Saison-Finale")
        with st.expander("🏃‍♂️ 1. Warm-up: Turnier-Warm-up (15 Min)"):
            st.markdown("**Gemeinsam:** Fokus und Konzentration. Dynamisches Einspielen.")
        with st.expander("🎯 2. Technik: Feinschliff & Duelle (35 Min)"):
            st.markdown("**Gemeinsam:** Angreifer gegen Blockspieler. Aufschläger gegen Annahmeriegel. Direkte 1v1 / 2v2 Duelle zur Schärfung.")
        with st.expander("🧠 3. Taktik: Timeout-Coaching (35 Min)"):
            st.markdown("**Split:** Teams simulieren Spielstände. Sie dürfen selbst Timeouts nehmen und müssen ohne Trainer eine taktische Lösung finden.")
        with st.expander("⚡ 4. Athletik: Explosivität & Cool-down (15 Min)"):
            st.markdown("**Freitags-Special:** Letzte kurze Sprintserie, danach 10 Minuten ausgiebiges gemeinsames Dehnen.")
        with st.expander("🏆 5. Abschlussspiel: Liga Finale (20 Min)"):
            st.markdown("**Das große Finale:** Die Rückrunde. 2 Gewinnsätze, volle Regeln, absolute Wettkampfbedingungen. Krönung des Monats-Siegers!")

# ---------------------------------------------------------
# SYSTEM-SPEZIAL
# ---------------------------------------------------------
elif monat == "System-Spezial: 3v3 meets 4v4":
    st.header("System-Spezial: Transition & Kognition")
    st.success("Tipp: Nutze diese Übungen für gezieltes Kleingruppentraining.")
    
    with st.expander("⏱️ 1. Der Transition-Läufer (U13 & U14) (15 Min)"):
        st.markdown("**Aus der Abwehr ins Zuspiel:** Trainer greift auf Zuspieler an. Dieser wehrt ab, Mitspieler übernimmt das Not-Zuspiel.")
    with st.expander("👀 2. Das Scanner-Zuspiel (20 Min)"):
        st.markdown("**Block lesen:** Trainer hebt linke oder rechte Hand. Zuspieler pritscht dorthin, wo die Hand *unten* ist.")
    with st.expander("🏆 3. Spielform: Der Libero-Joker (20 Min)"):
        st.markdown("**3v3 mit Abwehr-Chef:** Ein U14-Spieler sichert hinten als Libero ab und rettet weite Bälle.")
