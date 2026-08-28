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
            
    with w2:
        st.info("Woche 2-4 setzen das Konzept (Bagger-Präzision & Athletik) fort. Siehe vorherigen Code für Details, ergänzt um ständige Korrektur des 'ruhigen Spielbretts'.")

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

    with w2:
        st.info("Woche 2-4 vertiefen diese Elemente (Kopplung von Armzug und Anlauf unter Zeitdruck, Aufschlag als 'erster Angriff').")

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
            
    with w2:
        st.info("Woche 2-4 festigen das Highball-Set unter massivem Druck und integrieren es in komplette Turnier-Simulationen.")

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
