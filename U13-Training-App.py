import streamlit as st

# Seiten-Konfiguration
st.set_page_config(page_title="U13/U14 PRO Trainingsplan", page_icon="🏐", layout="centered")

st.title("🏐 U13/U14 Trainingsplan – TuB Bocholt")
st.markdown("Fokus: Grundlagenausbildung, Annahmeplattform, Beinarbeit & 1:2/Quadrat-System (Pos I bis IV) | 1 Feld / Hallenfreiraum")

# Dynamische Navigation & Teilnehmersteuerung
col1, col2 = st.columns(2)
with col1:
    monat = st.selectbox(
        "Wähle den Trainingsmonat:", 
        [
            "Monat 1: Annahme-Plattform, Beinarbeit & Basis-Aufschlag", 
            "Monat 2: Grundtechnik Angriff & Aufschlag", 
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
# MONAT 1: Annahme-Plattform, Beinarbeit & Basis-Aufschlag
# =========================================================
if monat == "Monat 1: Annahme-Plattform, Beinarbeit & Basis-Aufschlag":
    st.header("Monat 1: Annahmebrett, Beinarbeit & kontrollierte Angaben")
    
    w1, w2, w3, w4 = st.tabs(["Woche 1", "Woche 2", "Woche 3", "Woche 4"])
    
    # ---------------- WOCHE 1 ----------------
    with w1:
        st.subheader("TE 1 (90 Min): Annahmeplattform & Beinarbeit ohne Netz")
        
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Linien-Tappings & Richtungswechsel"):
            st.markdown("""
            **Ablauf (ohne Netz):** Spieler verteilen sich an Hallenlinien. 
            * 30 Sek. schnelle Linien-Tappings auf den Fußballen (Vor-Vor-Rück-Rück).
            * Auf Trainerpfiff sofort tiefe Volleyball-Grundstellung (Ready Position).
            * Kurze 3-Meter-Antritte im tiefen Schwerpunkt.
            **Trainer-Details:** Knie gebeugt, Fersen berühren den Boden kaum!
            """)
            
        with st.expander("🎯 2. Technik I (15 Min): Wand-Druck & Plattform-Stabilität (ohne Netz)"):
            st.markdown("""
            **Ablauf (ohne Netz):** Spieler stehen ca. 50 cm vor einer freien Hallenwand. Hände überstrecken, Daumen parallel, Unterarme zusammenpressen und mit vollem Druck gegen die Wand drücken.
            * Bewegung: Arme langsam mit Druck an der Wand von Hüfthöhe bis auf Brusthöhe schieben und wieder absenken.
            **Trainer-Details:** Schultern bewusst nach vorne-innen zusammenpressen. Die Arme dürfen nicht einknicken!
            """)
            
        with st.expander("🎯 3. Technik II (15 Min): Beinarbeit-Bagger in 2er-Gruppen (ohne Netz)"):
            st.markdown("""
            **Ablauf (ohne Netz):** 2er-Paare im Hallenfreiraum (Abstand 3-4 m). 
            * Spieler A wirft Bälle 1-2 Schritte links oder rechts neben Spieler B.
            * Spieler B macht 2 schnelle Sidesteps, **stoppt komplett ab**, formt erst dann das Brett und baggert präzise zurück zu A.
            **Trainer-Details:** Erst stehen – dann spielen! Kein Schwingen aus den Armen; Kraft kommt aus der Beinstreckung.
            """)
            
        with st.expander("🧠 4. Taktik I (15 Min): Zielbagger in 3er-Gruppen (ohne Netz)"):
            st.markdown("""
            **Ablauf (ohne Netz):** 3er-Gruppen in Reihe (A = Anwerfer, B = Annahme, C = Fänger als Steller-Ziel).
            * A wirft aus 5 m Entfernung an. B bewegt sich zum Ball, baggert im hohen Bogen genau zu C. 
            * Rotation nach 8 Durchgängen: A -> B -> C -> A.
            **Trainer-Details:** B muss die Schulterachse bereits vor dem Kontakt komplett auf C ausrichten.
            """)
            
        with st.expander("🧠 5. Taktik II (15 Min): Annahme am Netz auf Pos III"):
            st.markdown("""
            **Ablauf (mit Netz):** Spieler starten auf Pos I bzw. Pos IV. Trainer wirft kontrollierte Bälle über das Netz.
            * Spieler erlaufen den Ball mit schnellen Schritte nach vorne/innen und baggern gezielt auf Pos III (wo ein Korb oder Fänger steht).
            **Trainer-Details:** Lautes Rufen ('Ich!') vor der Ballberührung einfordern.
            """)
            
        with st.expander("🏆 6. Abschlussspiel (20 Min): Annahme-Bingo (3v3 / 4v4)"):
            st.markdown("""
            **Ablauf:** Gespielt wird 3v3 (Pos I, IV, III) oder 4v4 (Pos I, II, III, IV).
            * Aufschläge werden anfangs von unten oder aus 6 m Entfernung serviert.
            * **Punkte-Regel:** Normaler Punkt = 1. Punkt aus einem Spielzug, bei dem die Annahme sauber auf Pos III landete = 2 Punkte.
            """)

        st.divider()

        st.subheader("TE 2 - Freitag (120 Min): Beinarbeit, Angaben-Kontrolle & Athletik")
        
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Baggertennis im Kleinfeld"):
            st.markdown("""
            **Ablauf (ohne Netz oder über 3m-Linie):** Minifelder markieren. 1v1 oder 2v2. Ball darf genau 1x aufkommen.
            * Es darf ausschließlich gebaggert werden.
            **Trainer-Details:** Schnelle Beinarbeit und Antizipation fordern.
            """)
            
        with st.expander("⚡ 2. Athletik I (15 Min): ZNS, Quickness & Rumpf"):
            st.markdown("""
            **Ablauf (ohne Netz):** 
            * Linien-Skippings & Scheren-Sprünge (hohe Frequenz).
            * Unterarmstütz (Planks) mit Vor- und Zurückschieben des Körpers (schult Rumpf- und Schulterstabilität).
            **Trainer-Details:** Fersen immer in der Luft halten!
            """)
            
        with st.expander("🎯 3. Technik I (15 Min): Drucklose vs. druckvolle Angaben kontrollieren"):
            st.markdown("""
            **Ablauf:** Aufschläger stehen auf der Gegenseite an Pos I und servieren zunächst von der 4,50m-/6m-Linie von unten.
            * Annahmespieler auf Pos I und Pos IV.
            * Schrittweise Steigerung: Wechsel zum dosierten Tennis-Aufschlag von oben.
            **Trainer-Details:** Bei harten Angaben Arme komplett ruhig halten (Ball nur abprallen lassen). Nicht schlagen!
            """)
            
        with st.expander("🎯 4. Technik II (15 Min): Tiefen-Staffelung erlaufen (Vor & Zurück)"):
            st.markdown("""
            **Ablauf:** Trainer wirft abwechselnd kurze Bälle direkt hinters Netz und lange Bälle an die Grundlinie.
            * Annahmespieler auf Pos I bzw. IV müssen explosive Vorwärts- und Rückwärtsschritte machen.
            **Trainer-Details:** Beim Rückwärtslaufen nicht stolpern – Sidesteps oder Kreuzschritte nach hinten nutzen.
            """)
            
        with st.expander("🧠 5. Taktik I (15 Min): 2er- und 3er-Riegel Ausrichtung (Pos I, IV, II)"):
            st.markdown("""
            **Ablauf:** Aufschläger wechselt die Aufschlagzone auf der Gegenseite (von Pos I nach Pos II).
            * Annahmespieler (Pos I und IV in der U13 bzw. Pos I, IV, II in der U14) passen ihren Winkel an.
            **Trainer-Details:** Äußere Schulter leicht vorschieben, damit der Abprallwinkel immer zur Netzmitte (Pos III) zeigt.
            """)
            
        with st.expander("🧠 6. Taktik II (15 Min): Serve & Pass im Wellenbetrieb"):
            st.markdown("""
            **Ablauf:** 3 Aufschläge pro Durchgang. Annahme muss hoch auf Pos III gebracht werden, wo der Zuspieler den Ball fängt oder auf Pos IV ablegt.
            **Trainer-Details:** Klare Absprache an den Schnittstellen ('Mein Ball!').
            """)
            
        with st.expander("⚡ 7. Athletik II (10 Min): Ermüdungs-Aufschlag"):
            st.markdown("""
            **Ablauf:** 3 kurze Pendelsprints Grundlinie -> 3m-Linie, danach sofort 5 Aufschläge konzentriert ins gegnerische Feld bringen.
            **Trainer-Details:** Ruhiger Anwurf trotz erhöhtem Puls!
            """)
            
        with st.expander("🏆 8. Abschlussspiel (20 Min): Handicap-Match"):
            st.markdown("""
            **Ablauf:** 3v3 / 4v4 Wettkampf. 
            * Wenn Angaben zu oft im Netz landen, rücken die Aufschläger 2 Meter ins Feld vor, um erfolgreiche Ballwechsel zu garantieren.
            """)

    # ---------------- WOCHE 2 ----------------
    with w2:
        st.subheader("TE 3 (90 Min): Beinarbeit & Zuspiel-Kopplung")
        
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Baggertennis 2v2 (ohne Netz)"):
            st.markdown("**Ablauf:** 2er-Teams baggern sich den Ball über eine Bodenlinie zu (1x Bodenkontakt erlaubt).")
            
        with st.expander("🎯 2. Technik I (15 Min): Dreieck-Baggern in 3er-Gruppen (ohne Netz)"):
            st.markdown("""
            **Ablauf (ohne Netz):** 3 Spieler bilden ein Dreieck (Abstand je 3-4 m).
            * Ball wird im Bagger im Uhrzeigersinn weitergespielt.
            * Vor jedem Ballkontakt muss der Spieler einen schnellen Ausfallschritt zum Ball machen und die Schulterachse zum nächsten Ziel eindrehen.
            **Trainer-Details:** Blickkontakt und Eindrehen des Körpers schulen.
            """)
            
        with st.expander("🎯 3. Technik II (15 Min): Stemmschritt & Bagger-Kontrolle"):
            st.markdown("""
            **Ablauf:** Spieler starten an Pos I, laufen diagonal nach vorne zu Pos III, stoppen mit festem Stemmschritt und baggern den zugeworfenen Ball hoch zu Pos IV.
            **Trainer-Details:** Kein Nachfedern oder Weiterlaufen im Moment des Ballkontakts.
            """)
            
        with st.expander("🧠 4. Taktik I (15 Min): Läufer-Timing von Pos I auf Pos III"):
            st.markdown("""
            **Ablauf:** Zuspieler steht hinten auf Pos I. Annahme steht auf Pos IV. 
            * Trainer schlägt/wirft ein. Erst beim Ballabgang sprintet der Zuspieler von Pos I auf Pos III vor und pritscht/fängt den Annahmeball.
            **Trainer-Details:** Zuspieler darf nicht zu früh starten (kein Überlappen).
            """)
            
        with st.expander("🧠 5. Taktik II (15 Min): Annahme-Zuspiel Kette live"):
            st.markdown("""
            **Ablauf:** Aufschlag von drüben -> Annahme Pos I/IV zu Pos III -> Zuspieler stellt hoch auf Pos IV -> Angreifer spielt kontrollierten Dankeball zurück.
            **Trainer-Details:** Ballflugbahn muss hoch sein, um Hektik zu vermeiden.
            """)
            
        with st.expander("🏆 6. Abschlussspiel (20 Min): Wash-Game (2 Rallyes)"):
            st.markdown("**Ablauf:** Ein Punkt wird nur vergeben, wenn 2 aufeinanderfolgende Ballwechsel über Pos III aufgebaut und gewonnen werden.")

        st.divider()

        st.subheader("TE 4 - Freitag (120 Min): Druckaufbau & Annahme unter Belastung")
        
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Ball-Handling Staffel & Richtungswechsel"):
            st.markdown("**Ablauf:** Dribbeln, Richtungswechsel um Hütchen und saubere Anwurfsimulation vor der Schlagschulter.")
            
        with st.expander("⚡ 2. Athletik I (15 Min): Quick-Feet & Leiter-Ersatz an Linien"):
            st.markdown("**Ablauf:** Linien-Tappings, Scheren-Sprünge und explosive 3-Meter-Antritte.")
            
        with st.expander("🎯 3. Technik I (15 Min): Gezielte Angaben auf Zielzonen"):
            st.markdown("""
            **Ablauf:** Aufschläge von Pos I gezielt in markierte Zonen (z. B. auf Matten an Pos I oder IV auf der Gegenseite).
            **Trainer-Details:** Stabiler Stand, Handgelenk fest abklappen.
            """)
            
        with st.expander("🎯 4. Technik II (15 Min): Annahme nach vorne schieben"):
            st.markdown("""
            **Ablauf:** Kurze, drucklose Angaben aktiv mit den Beinen nach vorne auf Pos III drücken.
            **Trainer-Details:** Nicht die Arme nach vorne reißen, sondern den ganzen Körper durch Beinstreckung nach vorne bewegen.
            """)
            
        with st.expander("🧠 5. Taktik I (15 Min): Schnittstellen-Kommunikation"):
            st.markdown("""
            **Ablauf:** Bälle werden exakt zwischen Pos I und Pos IV geschlagen.
            * Wer zuerst 'Ich!' ruft, nimmt den Ball; der andere sichert ab.
            **Trainer-Details:** Zögern sofort korrigieren.
            """)
            
        with st.expander("🧠 6. Taktik II (15 Min): Notball-Zuspiel (Out-of-System)"):
            st.markdown("""
            **Ablauf:** Annahme gerät ungenau weit weg von Pos III. Nächststehender Spieler ruft 'Hilfe' und spielt einen hohen Notpass zu Pos IV.
            """)
            
        with st.expander("⚡ 7. Athletik II (10 Min): Rumpf & Schulter-Power"):
            st.markdown("**Ablauf:** Seitstütz (Side-Planks) und Theraband-Züge für die Schulterblatt-Stabilität.")
            
        with st.expander("🏆 8. Abschlussspiel (20 Min): System-Kaiser"):
            st.markdown("**Ablauf:** Kaiserplatz-Turnier mit 3v3 / 4v4 Teams. Rotation bei Fehler.")

    # ---------------- WOCHE 3 ----------------
    with w3:
        st.subheader("TE 5 (90 Min): Annahme-Konstanz & Beinarbeit")
        
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Reaktions-Sprints (ohne Netz)"):
            st.markdown("""
            **Ablauf (ohne Netz):** Bauchlage. Auf Pfiff: Explosives Aufstehen, 3 m Rückwärtslauf im tiefen Schwerpunkt, Richtungswechsel und Vorwärtssprint.
            **Trainer-Details:** Schnelle Beinarbeit und tiefer Schwerpunkt beim Abstoppen.
            """)
            
        with st.expander("🎯 2. Technik I (15 Min): Defense-Beinarbeit (Tennisbälle)"):
            st.markdown("""
            **Ablauf (ohne Netz):** 2er-Teams arbeiten im Freiraum der Halle. Der Werfer hat zwei Tennis- oder Unihockeybälle.
            * Der Werfer wirft nacheinander zwei Bälle tief und leicht versetzt auf den Boden. 
            * Der Abwehrspieler bleibt durchgehend in der tiefen Grundposition, verschiebt sich mit schnellen Sideshuffles zur Seite und holt beide Bälle.
            **Trainer-Details:** Der Fokus liegt auf dem Schwerpunkt! Der Spieler darf sich zwischen den Bällen **auf keinen Fall aufrichten**. Wer hochkommt, muss danach wieder runter und verliert die entscheidenden Millisekunden.
            """)
            
        with st.expander("🎯 3. Technik II (15 Min): Kurze und lange Bälle kontrollieren"):
            st.markdown("""
            **Ablauf (am Netz):** Spieler auf Pos I bzw. IV. Trainer variiert zwischen kurzen Bällen hinters Netz und langen Bällen zur Grundlinie.
            * Ziel bleibt die präzise Bogenannahme auf Pos III.
            **Trainer-Details:** Ständiges Nachfedern auf den Fußballen (Ready Position).
            """)
            
        with st.expander("🧠 4. Taktik I (15 Min): Reiner Schlag ohne Sprung (niedriges Netz)"):
            st.markdown("""
            **Organisation:** Das Netz wird deutlich niedriger gespannt (z.B. auf Kopfhöhe oder leicht darüber). Die Spieler stellen sich nah ans Netz.
            **Ablauf:** Der Trainer (oder ein Mitspieler) wirft den Ball präzise vor die Schlagschulter an. Die Kinder machen **keinen Anlauf und keinen Sprung**, sondern schlagen den Ball aus dem sicheren, hüftbreiten Stand über das Netz.
            **Trainer-Fokus:** Volle Konzentration auf den isolierten Armzug. Der Ellenbogen muss hoch bleiben, der Ball wird am höchsten Punkt vor dem Körper getroffen und das Handgelenk klappt aktiv ("peitschenartig") ab, damit der Ball nach unten ins Feld fliegt.
            """)
            
        with st.expander("🧠 5. Taktik II (15 Min): Stemmschritt über Hindernis (ohne Ball)"):
            st.markdown("""
            **Organisation:** Als flaches Hindernis dienen flache Hütchen oder kleine Markierungsscheiben auf dem Boden.
            **Ablauf:** Die Kinder starten mit einem Bein in der Luft. Der erste Schritt geht gezielt über das flache Hindernis in Richtung Netz. Direkt danach folgen die letzten beiden Schritte im Stemmschritt ("Links-Rechts" bei Rechtshändern).
            **Trainer-Fokus:** Voller Doppelarmschwung nach hinten-oben, explosive Bremsbewegung. Kein Ball!
            """)
            
        with st.expander("🏆 6. Abschlussspiel (20 Min): Druck-Turnier (3v3 / 4v4)"):
            st.markdown("""
            **Ablauf:** 3v3 / 4v4 auf Zeit. 
            * **Punkte-Regel:** Annahmefehler gibt 2 Punkte für das Aufschlagteam. Punkt aus perfektem 3er-Aufbau zählt 2 Punkte.
            """)

        st.divider()

        st.subheader("TE 6 - Freitag (120 Min): Transition & Abwehr-Beinarbeit")
        
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): 1v1 Volley-Tennis (ohne Netz / Kleinfeld)"):
            st.markdown("**Ablauf:** 1v1 mit 1x Bodenkontakt. Schult periphere Sicht, Antizipation und Beinarbeit.")
            
        with st.expander("⚡ 2. Athletik I (15 Min): Quickness & Rumpf"):
            st.markdown("**Ablauf:** Linien-Skippings, kurze 3m-Sprints und Plank-Variationen mit Handtipps.")
            
        with st.expander("🎯 3. Technik I (15 Min): Not-Annahme & Hechtbagger"):
            st.markdown("""
            **Ablauf:** Trainer schlägt kontrolliert in den Raum. Spieler bewegen sich explosiv zum Ball und bringen ihn mit stabiler Plattform als hohen Notball ins Zentrum.
            **Trainer-Details:** Flüssiges Wiederaufstehen direkt nach dem Bodenkontakt fordern.
            """)
            
        with st.expander("🎯 4. Technik II (15 Min): Einarmige Rettungsaktionen"):
            st.markdown("""
            **Ablauf:** Weit abweichende Bälle mit sauberer einarmiger Führung hoch ins Feld zurückretten.
            **Trainer-Details:** Körperspannung halten, damit der Notball nicht verspringt.
            """)
            
        with st.expander("🧠 5. Taktik I (15 Min): Umschalten von Abwehr auf Spielaufbau"):
            st.markdown("""
            **Ablauf:** Nach der ersten Feldabwehr formiert sich das Team sofort für den 2. Ball (Zuspieler rückt nach Pos III, Angreifer lösen sich vom Netz).
            **Trainer-Details:** Lautes Coachen unter den Spielern ('Ich übernehme!' / 'Hilfe!').
            """)
            
        with st.expander("🧠 6. Taktik II (15 Min): Transition unter Wettkampf-Bedingungen"):
            st.markdown("""
            **Ablauf:** Endlos-Rallye-Drill. Ball muss nach erfolgreicher Abwehr sofort in einen geordneten Angriff über Pos IV/II umgewandelt werden.
            """)
            
        with st.expander("⚡ 7. Athletik II (10 Min): Ermüdungs-Aufschlag"):
            st.markdown("**Ablauf:** 3x Linien-Pendelsprints, danach sofort 5 Aufschläge fehlerfrei ins gegnerische Zielfeld bringen.")
            
        with st.expander("🏆 8. Abschlussspiel (20 Min): Transition-Match (3v3 / 4v4)"):
            st.markdown("**Ablauf:** Wash-Match. Punkte zählen nur, wenn der Ballwechsel über eine erfolgreiche Abwehr-Transition gewonnen wurde.")

    # ---------------- WOCHE 4 ----------------
    with w4:
        st.subheader("TE 7 (90 Min): Annahme-Präzisionstest")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Pre-Game Einspielen in Paaren (ohne Netz)"):
            st.markdown("**Ablauf:** Paarweises Warmspielen mit Fokus auf präzisem Baggerkontakt und sauberer Beinarbeit.")
        with st.expander("🎯 2. Technik (30 Min): Annahme-Präzisionstest"):
            st.markdown("**Ablauf:** Jeder Spieler nimmt 10 Aufschläge an; gezählt wird, wie viele im markierten Zielkreis an Pos III landen.")
        with st.expander("🧠 3. Taktik (30 Min): Abstimmung U13 (3v3) & U14 (4v4)"):
            st.markdown("**Split:** Feste Schnittstellen-Absprachen zwischen Pos I, IV und II.")
        with st.expander("🏆 4. Abschlussspiel (20 Min): TuB Bocholt Liga"):
            st.markdown("**Turnier:** 3v3 / 4v4 Kurzspiele auf Zeit (4 Min pro Match).")

        st.divider()

        st.subheader("TE 8 - Freitag (120 Min): Der große Monatstest")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Turnier-Warm-up & Einschlagen"):
            st.markdown("**Ablauf:** Dynamisches Dehnen, Einschlagen am Netz mit Zuspiel aus der Annahme.")
        with st.expander("🎯 2. Technik (35 Min): Aufschlag & Annahme Feinschliff"):
            st.markdown("**Ablauf:** Duelle Aufschläger vs. Annahmeriegel (Pos I, IV, II).")
        with st.expander("🧠 3. Taktik (35 Min): Spielaufbau unter Wettkampfstress"):
            st.markdown("**Ablauf:** Simulation von Drucksituationen (z. B. Spielstand '13:13').")
        with st.expander("⚡ 4. Athletik & Auslockern (15 Min)"):
            st.markdown("**Ablauf:** Kurze Sprungserien (3x5 Hocksprünge) + ausgiebiges Partner-Dehnen.")
        with st.expander("🏆 5. Abschlussspiel (20 Min): Monats-Finale"):
            st.markdown("**Wettkampf:** 2 Gewinnsätze bis 15 Punkte unter voller Anwendung aller Annahme- und Läuferregeln.")

# =========================================================
# MONAT 2: Grundtechnik Angriff & Aufschlag
# =========================================================
elif monat == "Monat 2: Grundtechnik Angriff & Aufschlag":
    st.header("Monat 2: Schlagen über das Netz & gezielter Aufschlag")
    
    w1, w2, w3, w4 = st.tabs(["Woche 1", "Woche 2", "Woche 3", "Woche 4"])
    
    with w1:
        st.subheader("TE 1 (90 Min): Der Armzug (ohne Netz / an der Wand)")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Schulter-Aktivierung (ohne Netz)"):
            st.markdown("**Ablauf:** Baseball-Würfe in Paaren. Fokus auf Aufdrehen der Schulterachse.")
            
        with st.expander("🎯 2. Technik (30 Min): Wand-Schlagen (ohne Netz)"):
            st.markdown("**Ablauf:** Vor der Wand: Hoher Ellenbogen, Handgelenk klappt aktiv ab, Ball tippt vor der Wand auf den Boden.")
            
        with st.expander("🧠 3. Taktik I (15 Min): Reiner Schlag ohne Sprung (niedriges Netz)"):
            st.markdown("""
            **Organisation:** Das Netz wird deutlich niedriger gespannt (z.B. auf Kopfhöhe oder leicht darüber). Die Spieler stellen sich nah ans Netz.
            **Ablauf:** Der Trainer (oder ein Mitspieler) wirft den Ball präzise vor die Schlagschulter an. Die Kinder machen **keinen Anlauf und keinen Sprung**, sondern schlagen den Ball aus dem sicheren, hüftbreiten Stand über das Netz.
            **Trainer-Fokus:** Volle Konzentration auf den isolierten Armzug. Der Ellenbogen muss hoch bleiben, der Ball wird am höchsten Punkt vor dem Körper getroffen und das Handgelenk klappt aktiv ("peitschenartig") ab, damit der Ball nach unten ins Feld fliegt.
            """)
            
        with st.expander("🧠 4. Taktik II (15 Min): Einschlagen mit Ball & Stemmschritt"):
            st.markdown("""
            **Organisation:** Netz wieder auf normaler Höhe. Trainer oder Zuspieler steht auf Pos III mit Ballwagen. Angreifer in Reihe auf Pos IV.
            **Ablauf:** Hoher Bogenpass auf Pos IV. Die Kinder fokussieren sich auf den Stemmschritt, springen ab und übertragen den isolierten Armzug aus Taktik I nun live auf den anfliegenden Ball.
            **Trainer-Fokus:** Rhythmus übertragen! Der Ball muss am höchsten Punkt vor der Schlag-Schulter getroffen werden.
            """)
            
        with st.expander("🏆 5. Abschlussspiel (20 Min): Angriffs-Bingo"):
            st.markdown("**Punkte-Regel:** Punkte zählen nur bei geschlagenem Ball oder aggressivem Angriff.")

        st.divider()

        st.subheader("TE 2 - Freitag (120 Min): Der 3er-Anlauf & Sprungkraft")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Rhythmus-Schulung (ohne Netz)"):
            st.markdown("**Ablauf:** Anlauf-Rhythmus trocken ('Links... Rechts-Links!'). Explosiver Doppelarmschwung nach oben.")
        with st.expander("🎯 2. Technik (35 Min): Anlauf, Absprung & Schlag"):
            st.markdown("**Ablauf:** Zuspieler stellt Bogenbälle von Pos III auf Pos IV. Angreifer läuft aus 3m-Distanz an, springt beidbeinig ab und schlägt über das Netz.")
        with st.expander("🧠 3. Taktik (35 Min): Hit or Lob"):
            st.markdown("**Ablauf:** Trainer signalisiert Block. Hand oben = gezielter Lob; Hand unten = voller Schlag.")
        with st.expander("⚡ 4. Athletik (15 Min): Sprungkraft & Rumpf"):
            st.markdown("**Ablauf:** Box-Jumps (Kasten) + Core-Stabilität.")
        with st.expander("🏆 5. Abschlussspiel (20 Min): Angriffs-Turnier"):
            st.markdown("**Modus:** 3v3 / 4v4. Erfolgreiche Angriffsschläge zählen doppelt.")

    with w2:
        st.subheader("TE 3 (90 Min): Aufschlag-Härte")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Hechten & Block-Schatten"):
            st.markdown("**Ablauf:** Blocksprung am Netz, landen, rückwärts ausweichen, Abwehrhecht.")
        with st.expander("🎯 2. Technik (30 Min): Tennis-Aufschlag"):
            st.markdown("**Ablauf:** Aufschlag von oben ab 3m-Linie. Bei 3 Treffern 1 Meter nach hinten rücken.")
        with st.expander("🧠 3. Taktik (30 Min): Aufschlag vs. Riegel"):
            st.markdown("**Ablauf:** Team A serviert von oben. Team B kontrolliert die Annahme auf Pos III.")
        with st.expander("🏆 4. Abschlussspiel (20 Min): Aufschlag-Kaiser"):
            st.markdown("**Ablauf:** Kaiserplatz-Turnier mit direktem Wechsel bei Aufschlag-Ass.")

        st.divider()

        st.subheader("TE 4 - Freitag (120 Min): Komplex-Training & Sicherung")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Reaktions-Baggern & Sprints (ohne Netz)"):
            st.markdown("**Ablauf:** Schnelle Sidesteps, Spielbrett stabilisieren, Antritte.")
        with st.expander("🎯 2. Technik (35 Min): Freeball-Kill im Ablauf"):
            st.markdown("**Ablauf:** Dankeball -> Annahme Pos I/IV zu Pos III -> Zuspiel auf Pos IV/II -> Schlagangriff.")
        with st.expander("🧠 3. Taktik (35 Min): Die Angriffssicherung"):
            st.markdown("**Ablauf:** Angreifer schlägt in Kasten-Block. Mitspieler sichern tief am Boden ab.")
        with st.expander("⚡ 4. Athletik (15 Min): Schulter-Power"):
            st.markdown("**Ablauf:** Einarmige Medizinballwürfe über das Netz.")
        with st.expander("🏆 5. Abschlussspiel (20 Min): Wash-Game Extrem"):
            st.markdown("**Ablauf:** 2 Rallyes in Folge für Punktgewinn.")

    with w3:
        st.subheader("TE 5 (90 Min): Reaktion & Abwehr")
        with st.expander("🎾 1. Warm-up (10 Min): 1v1 Kreatives Tennis Game"):
            st.markdown("**Ablauf:** 1v1 mit 1x Bodenkontakt in Kleinfeldschläuchen.")
        with st.expander("🎯 2. Technik (30 Min): Schmetter-Abwehr"):
            st.markdown("**Ablauf:** Spieler stehen tief auf Pos I/IV. Trainer schlägt gezielt an. Ruhiges Brett halten.")
        with st.expander("🧠 3. Taktik (30 Min): Abwehr -> Transition"):
            st.markdown("**Ablauf:** Harter Angriff -> Abwehr auf Pos III -> Zuspiel -> Gegenangriff über Pos IV.")
        with st.expander("🏆 4. Abschlussspiel (20 Min): Abwehr-König"):
            st.markdown("**Sonderregel:** Abwehraktionen mit erfolgreichem Gegenangriff geben 2 Punkte.")

        st.divider()

        st.subheader("TE 6 - Freitag (120 Min): Block-Timing & Feldverteidigung")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): 1v1 Tennis Auf-/Absteiger"):
            st.markdown("**Ablauf:** Kreatives Tennis-Game im Turniermodus.")
        with st.expander("🎯 2. Technik (35 Min): Der 1er- und 2er-Block"):
            st.markdown("**Ablauf:** Timing beim Absprung am Netz (Pos III/II), Hände übergreifen.")
        with st.expander("🧠 3. Taktik (35 Min): Block-Abwehr Abstimmung"):
            st.markdown("**Ablauf:** U14 stellt Doppelblock, U13 stellt 1er-Block mit Feldabwehr dahinter (Pos I und IV).")
        with st.expander("⚡ 4. Athletik (15 Min): Sprungausdauer am Netz"):
            st.markdown("**Ablauf:** Serien aus Blocksprüngen mit lateralen Sidesteps.")
        with st.expander("🏆 5. Abschlussspiel (20 Min): Block & Defense Match"):
            st.markdown("**Modus:** 3v3 / 4v4. Kill-Blocks zählen doppelt.")

    with w4:
        st.subheader("TE 7 (90 Min): Entscheidungsfindung")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): 1v1 Tennis Game"):
            st.markdown("**Ablauf:** Schnelles Warm-up im 1-gegen-1.")
        with st.expander("🎯 2. Technik (30 Min): Hit or Lob Präzision"):
            st.markdown("**Ablauf:** Blitzschnelle Entscheidung: Harter Schlag oder Lob über den Block.")
        with st.expander("🧠 3. Taktik (30 Min): Systemprüfung unter Druck"):
            st.markdown("**Ablauf:** Annahme -> Zuspiel -> Angriff fehlerfrei durchbringen.")
        with st.expander("🏆 4. Abschlussspiel (20 Min): TuB Bocholt Liga"):
            st.markdown("**Turnier:** Reiner Wettkampf 3v3 / 4v4.")

        st.divider()

        st.subheader("TE 8 - Freitag (120 Min): Das große Finale")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Pre-Game Routine & Einschlagen"):
            st.markdown("**Ablauf:** Offizieller Spieltags-Ablauf.")
        with st.expander("🎯 2. Technik (35 Min): Nervenstarker Aufschlag"):
            st.markdown("**Ablauf:** 5 harte Aufschläge fehlerfrei ins Zielfeld platzieren.")
        with st.expander("🧠 3. Taktik (35 Min): Match-Taktik & Coaching"):
            st.markdown("**Ablauf:** Teams analysieren Lücken selbstständig.")
        with st.expander("⚡ 4. Athletik (15 Min): Final-Drill & Mobilisation"):
            st.markdown("**Ablauf:** Schnelligkeits-Parcours + Dehnen.")
        with st.expander("🏆 5. Abschlussspiel (20 Min): Meisterschaft"):
            st.markdown("**Wettkampf:** 2 Gewinnsätze bis 15 Punkte.")

# =========================================================
# MONAT 3: Out-of-System & Match-Speed
# =========================================================
elif monat == "Monat 3: Out-of-System & Match-Speed":
    st.header("Monat 3: Lösungen unter Stress & hohes Tempo")
    
    w1, w2, w3, w4 = st.tabs(["Woche 1", "Woche 2", "Woche 3", "Woche 4"])
    
    with w1:
        st.subheader("TE 1 (90 Min): Chaos-Management")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Blickkontrolle (ohne Netz)"):
            st.markdown("**Ablauf:** Paarweises Baggern mit Fingereigenzeige für periphere Sicht.")
        with st.expander("🎯 2. Technik (30 Min): Out-of-System Notpass"):
            st.markdown("**Ablauf:** Trainer wirft tief ins Hinterfeld (Pos I). Hoher Not-Bagger an die Antenne zu Pos IV.")
        with st.expander("🧠 3. Taktik (30 Min): Freeball-Kill unter Zeitdruck"):
            st.markdown("**Ablauf:** Annahme, Zuspiel und Angriff innerhalb von 3-4 Sekunden abschließen.")
        with st.expander("🏆 4. Abschlussspiel (20 Min): Profi-Kaiserplatz"):
            st.markdown("**Ablauf:** Kaiserplatz mit vollen Aufschlägen.")

        st.divider()

        st.subheader("TE 2 - Freitag (120 Min): Not-Pässe & Physis")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Reaktions-Chaos in 3er-Gruppen (ohne Netz)"):
            st.markdown("**Ablauf:** 2 Bälle gleichzeitig im 3er-Team jonglieren.")
        with st.expander("🎯 2. Technik (35 Min): Schlechte Pässe erlaufen"):
            st.markdown("**Ablauf:** Streuende Bälle erlaufen, komplett abstoppen und Notpass spielen.")
        with st.expander("🧠 3. Taktik (35 Min): Butterfly unter Druck"):
            st.markdown("**Ablauf:** Endlos-System mit fliegendem Einrücken.")
        with st.expander("⚡ 4. Athletik (15 Min): Sprint-Ausdauer"):
            st.markdown("**Ablauf:** Linien-Pendelsprints.")
        with st.expander("🏆 5. Abschlussspiel (20 Min): Out-of-System Bonus"):
            st.markdown("**Punkte-Regel:** Punkte nach geretteten Notbällen zählen doppelt.")

    with w2:
        st.subheader("TE 3 (90 Min): Angriff aus unsauberer Annahme")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Ball-Klau (ohne Netz)"):
            st.markdown("**Ablauf:** Dribbeln und Bälle wegschlagen.")
        with st.expander("🎯 2. Technik (30 Min): Angriff aus 3m-Distanz"):
            st.markdown("**Ablauf:** Bälle von hinter der 3m-Linie kontrolliert und lang ins gegnerische Feld drücken.")
        with st.expander("🧠 3. Taktik (30 Min): Rettungsaktion -> Angriff"):
            st.markdown("**Ablauf:** Ball kratzen -> hoher Notpass -> gezielter Lob/Schlag.")
        with st.expander("🏆 4. Abschlussspiel (20 Min): Kein Dankeball"):
            st.markdown("**Regel:** Wer unkontrollierte Bälle 'einfach so' rüberspielt, verliert den Punkt.")

        st.divider()

        st.subheader("TE 4 - Freitag (120 Min): Fehlerkompensation & Rumpf")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Koordinations-Sprints (ohne Netz)"):
            st.markdown("**Ablauf:** Sprints aus dem Sitzen/Liegen auf Kommando.")
        with st.expander("🎯 2. Technik (35 Min): Tip/Lob aus der Not"):
            st.markdown("**Ablauf:** Ball klebt am Netz -> gezielter Tip über den Block.")
        with st.expander("🧠 3. Taktik (35 Min): Sicherung bei schlechten Pässen"):
            st.markdown("**Ablauf:** Mannschaft rückt geschlossen zur Blocksicherung nach.")
        with st.expander("⚡ 4. Athletik (15 Min): Core-Power"):
            st.markdown("**Ablauf:** Bauchmuskel-Zirkel und Rückenstrecker.")
        with st.expander("🏆 5. Abschlussspiel (20 Min): Wash-Game Extrem"):
            st.markdown("**Turnier:** 3 Rallyes am Stück gewinnen.")

    with w3:
        st.subheader("TE 5 (90 Min): High-Speed Transition")
        with st.expander("🎾 1. Warm-up (10 Min): Volley-Tennis (ohne Netz)"):
            st.markdown("**Ablauf:** 1v1 Chaos-Tennis.")
        with st.expander("🎯 2. Technik (30 Min): Abwehr -> Sofort-Angriff"):
            st.markdown("**Ablauf:** Bagger-Abwehr auf Pos I -> sofortiger Anlauf und Angriff über Pos IV.")
        with st.expander("🧠 3. Taktik (30 Min): Dauerfeuer"):
            st.markdown("**Ablauf:** Trainer bringt 5 Bälle pro Team in 10 Sekunden ins Spiel.")
        with st.expander("🏆 4. Abschlussspiel (20 Min): Speed-Turnier"):
            st.markdown("**Modus:** Neuer Ball kommt ohne Pause sofort ins Spiel.")

        st.divider()

        st.subheader("TE 6 - Freitag (120 Min): Wettkampfhärte & Beine")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): 1v1 Auf-/Absteiger"):
            st.markdown("**Ablauf:** Volley-Tennis im Turniermodus.")
        with st.expander("🎯 2. Technik (35 Min): Aufschlagdruck vs. Transition"):
            st.markdown("**Ablauf:** Gezielte Aufschläge von Pos I auf Pos IV, sofortige Transition.")
        with st.expander("🧠 3. Taktik (35 Min): Rallye aufrechterhalten"):
            st.markdown("**Ablauf:** Bälle durch Lobs und Blocksicherung im Spiel halten.")
        with st.expander("⚡ 4. Athletik (15 Min): Schnelle Füße"):
            st.markdown("**Ablauf:** Skippings und Antritte an Hallenlinien.")
        with st.expander("🏆 5. Abschlussspiel (20 Min): Transition-König"):
            st.markdown("**Modus:** Punkte zählen erst nach mindestens 3 Netzüberquerungen.")

    with w4:
        st.subheader("TE 7 (90 Min): Match-Day Vorbereitung")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Pre-Game Routine"):
            st.markdown("**Ablauf:** Vollständiges Einschlagen.")
        with st.expander("🎯 2. Technik (30 Min): Sicherer Not-Aufschlag"):
            st.markdown("**Ablauf:** 100% Quote bei Angaben von unten/leichtem Float.")
        with st.expander("🧠 3. Taktik (30 Min): Raumaufteilung Pos I bis IV"):
            st.markdown("**Ablauf:** Feste Absprachen im 3v3 und 4v4.")
        with st.expander("🏆 4. Abschlussspiel (20 Min): Liga Hinrunde"):
            st.markdown("**Turnier:** Jeder gegen Jeden.")

        st.divider()

        st.subheader("TE 8 - Freitag (120 Min): Das Saison-Finale")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Turnier-Warm-up"):
            st.markdown("**Ablauf:** Dynamisches Einspielen.")
        with st.expander("🎯 2. Technik (35 Min): Direkte Duelle"):
            st.markdown("**Ablauf:** Angreifer vs. Block, Aufschläger vs. Annahme.")
        with st.expander("🧠 3. Taktik (35 Min): Timeout-Coaching"):
            st.markdown("**Ablauf:** Teams lösen taktische Probleme im Timeout selbst.")
        with st.expander("⚡ 4. Athletik (15 Min): Cool-down & Dehnen"):
            st.markdown("**Ablauf:** Auslaufen und Partner-Dehnen.")
        with st.expander("🏆 5. Abschlussspiel (20 Min): Liga Finale"):
            st.markdown("**Das große Finale:** 2 Gewinnsätze unter vollen Wettkampfbedingungen.")

# =========================================================
# SYSTEM-SPEZIAL
# =========================================================
elif monat == "System-Spezial: 3v3 meets 4v4":
    st.header("System-Spezial: Transition & Kognition (Pos I bis IV)")
    
    with st.expander("⏱️ 1. Der Transition-Läufer (15 Min)"):
        st.markdown("""
        **Aus der Abwehr ins Zuspiel (Pos I -> Pos III):** 
        Trainer schlägt auf den Zuspieler. Zuspieler wehrt ab, Mitspieler von Pos IV übernimmt das Zuspiel.
        * **U13 (3v3):** Läufer startet von hinten (Pos I) und läuft nach Pos III ein.
        * **U14 (4v4):** Zuspieler lässt sich aus Pos II/I in die Abwehr fallen und wird vertreten.
        """)
    with st.expander("👀 2. Das Scanner-Zuspiel (20 Min)"):
        st.markdown("**Block lesen:** Trainer hebt linke oder rechte Hand. Zuspieler auf Pos III pritscht dorthin, wo die Hand *unten* ist.")
    with st.expander("🌪️ 3. Der Dauerläufer (20 Min)"):
        st.markdown("""
        **Laufwege & Beinarbeit automatisieren:**
        * Sprint Pos I -> Pos III -> Zuspiel auf Pos IV. Zurück zu Pos I. 8x am Stück wiederholen.
        """)
    with st.expander("🏆 4. Spielform: Der Libero-Joker (20 Min)"):
        st.markdown("**3v3 / 4v4 Match:** Ein Spieler sichert auf der Grundlinie (hinter Pos I und IV) ab und rettet Notbälle.")
