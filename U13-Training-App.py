import streamlit as st

# Seiten-Konfiguration
st.set_page_config(page_title="U13/U14 PRO Trainingsplan", page_icon="🏐", layout="centered")

st.title("🏐 U13/U14 PRO Plan (DVV RTK)")
st.markdown("TuB Bocholt | 2x pro Woche (TE 1: 90 Min, TE 2 Freitag: 120 Min) | Max. 15 Min pro Block")

# Navigation - Dynamik
col1, col2 = st.columns(2)
with col1:
    monat = st.selectbox(
        "Wähle den Trainingsmonat:", 
        [
            "Monat 1: Annahme-Präzision (RTK: Bagger & Athletik)", 
            "Monat 2: Grundtechnik Angriff & Aufschlag", 
            "Monat 3: Out-of-System & Match-Speed",
            "System-Spezial: 3v3 meets 4v4"
        ]
    )
with col2:
    spieler = st.radio(
        "Wie viele Spieler sind heute da?",
        ["9-12 Spieler (Wellenprinzip)", "6-8 Spieler (Intensiv)"]
    )

st.divider()

# ---------------------------------------------------------
# MONAT 1: Annahme & System (Bagger & Athletik)
# ---------------------------------------------------------
if monat == "Monat 1: Annahme-Präzision (RTK: Bagger & Athletik)":
    st.header("Monat 1: Gezielte Annahme zum Steller")
    if spieler == "9-12 Spieler (Wellenprinzip)":
        st.info("Modus: Volles Feld. Wir nutzen das Wellenprinzip und Stationswechsel, um Wartezeiten zu killen.")
    else:
        st.success("Modus: Kleingruppe. Extreme Ballberührungsdichte. Weniger Pausen, mehr Dauerschleifen!")
    
    w1, w2, w3, w4 = st.tabs(["Woche 1", "Woche 2", "Woche 3", "Woche 4"])
    
    # ---------------- WOCHE 1 ----------------
    with w1:
        st.subheader("TE 1 (90 Min): Das sichere Spielbrett")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): RTK Reaktions-Baggern"):
            if spieler == "9-12 Spieler (Wellenprinzip)":
                st.markdown("**Organisation:** 3er-Gruppen (1 Werfer, 2 arbeiten abwechselnd).")
            else:
                st.markdown("**Organisation:** Reine 2er-Paare. Dauerschleife ohne Pause.")
            st.markdown("**Ablauf:** Spieler A wirft seitlich. Spieler B macht schnellen Sidestep, formt das Spielbrett und baggert zurück.\n**Trainer-Details:** Beinarbeit *vor* Armarbeit! Keine Schwungbewegung aus den Schultern!")

        with st.expander("🎯 2. Technik I (15 Min): Ziel-Baggern aus dem Stand"):
            if spieler == "9-12 Spieler (Wellenprinzip)":
                st.markdown("**Organisation:** Zwei Reihen an der Grundlinie. Trainer wirft ein, nach dem Bagger sofort der Nächste.")
            else:
                st.markdown("**Organisation:** Ein Kasten als Ziel, alle Spieler stehen im Halbbereich und baggern fast zeitgleich auf Zuruf.")
            st.markdown("**Ablauf:** Ball im hohen Bogen auf Pos II/III baggern.\n**Trainer-Details:** Beine schulterbreit, Knie vor den Fußspitzen.")

        with st.expander("🎯 3. Technik II (15 Min): Bagger aus der Bewegung"):
            st.markdown("**Ablauf:** Bälle in Lücken werfen. Spieler erläuft Ball, stoppt ab und spielt zum Ziel.\n**Trainer-Details:** Der Bremsweg ist entscheidend. Stemmschritt setzen, Spielbrett erst im letzten Moment formen.")

        with st.expander("🧠 4. Taktik I (15 Min): Annahme-Riegel formieren"):
            if spieler == "9-12 Spieler (Wellenprinzip)":
                st.markdown("**Organisation:** Seite A (3er Riegel), Seite B (2er Riegel). Rest sammelt Bälle und rotiert nach 3 Bällen ein.")
            else:
                st.markdown("**Organisation:** Zwei feste 3er-Riegel (oder 3v4). Keine Rotation, reines Abarbeiten.")
            st.markdown("**Ablauf:** Trainer wirft leichte Bälle ein. Klare Kommunikation ('Ich!').")

        with st.expander("🧠 5. Taktik II (15 Min): Pass zum Steller"):
            st.markdown("**Ablauf:** Gezielter Bagger zum einlaufenden Steller (dieser fängt).\n**Trainer-Details:** Der Bagger muss hoch sein. Zuspieler fordert lautstark.")

        with st.expander("🏆 6. Abschlussspiel (20 Min): Annahme-Bingo"):
            if spieler == "9-12 Spieler (Wellenprinzip)":
                st.markdown("**Organisation:** Kaiserplatz-Turnier. Gewinner bleiben, Verlierer rotieren raus.")
            else:
                st.markdown("**Organisation:** 3v3 oder 4v4 Dauer-Match. Keine Auswechselspieler.")
            st.markdown("**Punkte-Regel:** Zusatzpunkt, wenn Annahme perfekt beim Zuspieler landet (ohne dass dieser laufen muss).")

        st.divider()

        st.subheader("TE 2 - Freitag (120 Min): RTK Athletik & Bagger unter Druck")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Tiefe Abwehr & Linien-Chaos"):
            st.markdown("**Ablauf:** Linienfangen mit tiefem Abwehr-Stopp auf Pfiff.\n**Trainer-Details:** Ready-Position einfordern: Knie gebeugt, Gewicht auf Vorfuß.")

        with st.expander("🎯 2. Technik I (15 Min): Dankeball-Sprint"):
            st.markdown("**Ablauf:** Sprint ans Netz, komplett abstoppen, baggern.\n**Trainer-Details:** Härte im Antritt fordern und Ruhe im Bagger-Kontakt.")

        with st.expander("🎯 3. Technik II (15 Min): Harte Bälle absorbieren"):
            if spieler == "9-12 Spieler (Wellenprinzip)":
                st.markdown("**Organisation:** Trainer schlägt von Kasten. Spieler wehren ab und rennen sofort Bälle sammeln.")
            else:
                st.markdown("**Organisation:** Trainer schlägt. Abwehrspieler wird sofort zum Steller für den nächsten Ball (Doppelbelastung).")
            st.markdown("**Ablauf:** Arme hinhalten, Ball abprallen lassen.\n**Trainer-Details:** Körper absorbiert den Druck. Arme nicht reißen!")

        with st.expander("🧠 4. Taktik I (15 Min): Serve & Pass (Leicht)"):
            st.markdown("**Ablauf:** Aufschläge von unten. Fokus auf Annahme-Aufbau.\n**Trainer-Details:** Überprüfe die Positionierung der Annahmespieler.")

        with st.expander("🧠 5. Taktik II (15 Min): Serve & Pass (Schwer)"):
            if spieler == "9-12 Spieler (Wellenprinzip)":
                st.markdown("**Organisation:** 3er-Wellen. Nach 3 Aufschlägen rückt das wartende Team aufs Feld.")
            else:
                st.markdown("**Organisation:** Butterfly-Drill. Nach dem Aufschlag sofort unter dem Netz durch auf die Annahme-Position rennen.")
            st.markdown("**Ablauf:** Harte Aufschläge von oben.")

        with st.expander("⚡ 6. Athletik I (15 Min): DVV Rumpf- & Bein-Power"):
            st.markdown("**Ablauf:** 3 Runden Zirkel (Plank, Ausfallschritte, Sprünge).\n**Trainer-Details:** Starker Rumpf = sicheres Spielbrett.")

        with st.expander("⚡ 7. Athletik II (10 Min): Puls-Aufschlag"):
            st.markdown("**Ablauf:** Direkt nach Zirkel 5 Aufschläge mit hohem Puls.\n**Trainer-Details:** Athletische Ausdauer schulen.")

        with st.expander("🏆 8. Abschlussspiel (20 Min): Handicap-Match"):
            if spieler == "9-12 Spieler (Wellenprinzip)":
                st.markdown("**Organisation:** 4v4. Wartendes Team schlägt von außen Bälle ein.")
            else:
                st.markdown("**Organisation:** 3v3 oder 4v4 (mit Trainer als Libero).")
            st.markdown("**Ablauf:** Wenn Annahme wackelt, nur Aufschläge von unten. Fokus auf lange Rallyes.")

    # ---------------- WOCHE 2 ----------------
    with w2:
        st.subheader("TE 3 (90 Min): Zuspieler-Integration")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Kognitives Chaos"):
            st.markdown("**Ablauf:** A pritscht Ball 1, B rollt Ball 2. Auf Pfiff: Sprint.")
            
        with st.expander("🎯 2. Technik I (15 Min): Bagger-Winkel anpassen"):
            st.markdown("**Ablauf:** Ball selbst anwerfen und diagonal auf Pos 2 baggern.\n**Trainer-Details:** Die innere Schulter muss tiefer sein.")

        with st.expander("🎯 3. Technik II (15 Min): Annahme + Zuspiel Kopplung"):
            if spieler == "9-12 Spieler (Wellenprinzip)":
                st.markdown("**Organisation:** Fliegender Wechsel auf der Steller-Position nach jedem Pass.")
            else:
                st.markdown("**Organisation:** Feste Zuspieler für 3 Minuten. Extreme Ausdauerbelastung für den Steller.")
            st.markdown("**Ablauf:** Annahme baggert zum Steller. Steller pritscht hoch in Korb.")

        with st.expander("🧠 4. Taktik I (15 Min): System-Laufwege (Trocken)"):
            st.markdown("**Ablauf:** Zuspieler läuft ein, fängt Ball, alle rotieren.\n**Trainer-Details:** Positionsfehler abpfeifen. Erst laufen, wenn Ball den Trainer verlässt.")

        with st.expander("🧠 5. Taktik II (15 Min): System-Laufwege (Live)"):
            if spieler == "9-12 Spieler (Wellenprinzip)":
                st.markdown("**Organisation:** Wellenprinzip. Sobald der Dankeball drüben ist, sprintet das nächste Team aufs Feld.")
            else:
                st.markdown("**Organisation:** Ein Team auf dem Feld, Trainer feuert sofort neuen Ball ein, wenn der letzte gespielt wurde.")
            st.markdown("**Ablauf:** Komplett durchgespielt (Annahme, Zuspiel, Dankeball).")

        with st.expander("🏆 6. Abschlussspiel (20 Min): Wash-Game (2 Rallyes)"):
            st.markdown("**Ablauf:** 2 Rallyes in Folge gewinnen = 1 Punkt.\n**Trainer-Details:** Zweiter Ball fliegt sofort rein. Hält Konzentration oben.")

        st.divider()

        st.subheader("TE 4 - Freitag (120 Min): RTK System unter Druck")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Ball-Handling Staffel"):
            st.markdown("**Ablauf:** Staffel mit Ball prellen, Anwurf-Simulation am Netz.")

        with st.expander("🎯 2. Technik I (15 Min): Zonen-Aufschlag"):
            st.markdown("**Ablauf:** Aufschläge gezielt auf Turnmatten in Ecken.\n**Trainer-Details:** Handgelenk muss fest sein.")

        with st.expander("🎯 3. Technik II (15 Min): Annahme-Verschiebung"):
            if spieler == "9-12 Spieler (Wellenprinzip)":
                st.markdown("**Organisation:** Aufschläger-Teams wechseln sich an der Grundlinie ab.")
            else:
                st.markdown("**Organisation:** Ein Aufschläger (Trainer) schickt die Annahme von links nach rechts.")
            st.markdown("**Ablauf:** Aufschläger wechselt permanent Position. Riegel rotiert.")

        with st.expander("🧠 4. Taktik I (15 Min): Out-of-System (Trocken)"):
            st.markdown("**Ablauf:** Trainer wirft Ball absichtlich ins Aus. Spieler rufen 'Hilfe' und fangen.\n**Trainer-Details:** Fokus auditive Kommunikation.")

        with st.expander("🧠 5. Taktik II (15 Min): Out-of-System (Live)"):
            if spieler == "9-12 Spieler (Wellenprinzip)":
                st.markdown("**Organisation:** Team A rettet, Team B wartet hinter dem Feld und rückt bei Fehler ein.")
            else:
                st.markdown("**Organisation:** Endlos-Rettung. Der Spieler, der den Notpass spielt, greift beim nächsten Ball selbst an.")
            st.markdown("**Ablauf:** Notzuspiel aus dem Chaos zum Angreifer.")

        with st.expander("⚡ 6. Athletik I (15 Min): DVV Fußarbeit (Leiter)"):
            st.markdown("**Ablauf:** Koordinationsleiter.\n**Trainer-Details:** Fersen in der Luft (Vorfuß-Lauf).")

        with st.expander("⚡ 7. Athletik II (10 Min): Core-Rotation"):
            st.markdown("**Ablauf:** Medizinball-Würfe (seitlich).")

        with st.expander("🏆 8. Abschlussspiel (20 Min): System-Kaiser"):
            st.markdown("**Ablauf:** Herausforderer rücken nur bei 3er-System-Aufbau vor.")

    # ---------------- WOCHE 3 ----------------
    with w3:
        st.subheader("TE 5 (90 Min): Annahme-Konstanz & Bewegung")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Reaktions-Sprints & Richtungswechsel"):
            st.markdown("**Ablauf:** Bauchlage am Netz. Auf Pfiff: Explosives Aufstehen, Rückwärtslauf bis 3m-Linie, Richtungswechsel und Vorwärtssprint zur Grundlinie.\n**Trainer-Details:** Schnelle Beinarbeit und tiefer Schwerpunkt beim Abstoppen einfordern.")

        with st.expander("🎯 2. Technik I (15 Min): Annahme aus der seitlichen Bewegung"):
            st.markdown("**Ablauf:** Spieler starten auf Pos VI. Trainer wirft Bälle variabel seitlich an. Spieler machen schnelle Sidesteps/Kreuzschritte, stabilisieren das Spielbrett im Moment des Kontakts und baggern zu Pos III.\n**Trainer-Details:** Beine müssen stehen, bevor der Ball das Spielbrett berührt! Schulterachse zum Ziel drehen.")

        with st.expander("🎯 3. Technik II (15 Min): Kurze und lange Bälle kontrollieren"):
            st.markdown("**Ablauf:** Wechsel zwischen kurzen Lobs hinters Netz und tiefen langen Bällen an die Grundlinie. Ziel bleibt die präzise Bogenannahme auf Pos III.\n**Trainer-Details:** Ständiges Nachfedern auf den Fußballen ('Ready Position') zur schnellen Vor- und Rückwärtsbewegung.")

        with st.expander("🧠 4. Taktik I (15 Min): Annahmeriegel dynamisch verschieben"):
            st.markdown("**Ablauf:** U14 (3er-Riegel) / U13 (2er-Riegel). Aufschläger wechselt an der Grundlinie die Position (Pos I, VI, V). Der Riegel verschiebt sich synchron vor dem Aufschlag.\n**Trainer-Details:** Klare Schnittstellen-Kommunikation bei Bällen zwischen zwei Spielern fordern ('Ich!').")

        with st.expander("🧠 5. Taktik II (15 Min): Annahme unter Aufschlagdruck"):
            st.markdown("**Ablauf:** Aufschläge von der Grundlinie mit Druck. Annahme auf den einlaufenden Steller auf Pos III, der den Ball direkt auf Pos IV oder II weiterspielt.\n**Trainer-Details:** Fokus auf die Ruhe im Spielbrett trotz harter Aufschläge – keine ausholende Armbewegung!")

        with st.expander("🏆 6. Abschlussspiel (20 Min): Druck-Turnier"):
            st.markdown("**Ablauf:** 3v3 / 4v4 auf Zeit.\n**Punkte-Regel:** Annahmefehler (direktes As) gibt 2 Punkte für das Aufschlagteam. Punkt aus perfektem 3er-Aufbau zählt ebenfalls 2 Punkte.")

        st.divider()

        st.subheader("TE 6 - Freitag (120 Min): Transition Defensive -> Annahme & Athletik")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): 1v1 Volley-Tennis"):
            st.markdown("**Ablauf:** Spielfeld in kleine Schläuche unterteilen. 1-gegen-1 mit 1x Bodenkontakt erlaubt. Alle Körperteile zulässig.\n**Trainer-Details:** Bringt den Puls hoch und schult periphere Sicht sowie Antizipation.")

        with st.expander("⚡ 2. Athletik I - ZNS & Quickness (15 Min): Schnelligkeit & Rumpf"):
            st.markdown("**Ablauf:**\n* Koordinationsleiter / Linien-Skippings (schnelle Kontakte auf den Vorfüßen).\n* Kurze explosive 3-Meter-Antritte.\n* Dynamische Rumpf- und Schulteraktivierung (Plank-Variationen mit Handtipps, Thera-Band-Züge).\n**Trainer-Details:** Direkt nach dem Warm-up durchführen, solange die Spieler noch mental und muskulär frisch sind.")

        with st.expander("🎯 3. Technik I (15 Min): Not-Annahme & Hechtbagger"):
            st.markdown("**Ablauf:** Trainer schlägt kontrolliert in den Raum. Spieler hechten/rutschen zum Ball und bringen ihn mit stabiler Plattform als hohen Notball ins Zentrum.\n**Trainer-Details:** Keine Scheu vor dem Boden; flüssiges Wiederaufstehen direkt nach der Berührung verlangen.")

        with st.expander("🎯 4. Technik II (15 Min): Einarmige Rettungsaktionen"):
            st.markdown("**Ablauf:** Weit abweichende Bälle mit sauberer einarmiger Handflächen-/Unterarmführung hoch und ins Feld zurückretten.\n**Trainer-Details:** Körperspannung halten, damit der Notball nicht unkontrolliert verspringt.")

        with st.expander("🧠 5. Taktik I (15 Min): Umschalten von Abwehr auf Spielaufbau"):
            st.markdown("**Ablauf:** Trainer schlägt Dankeball/Angriffsball ein. Nach der ersten Feldabwehr formiert sich das Team sofort für den 2. Ball (Zuspieler rückt nach, Angreifer lösen sich vom Netz).\n**Trainer-Details:** Lautes Coachen unter den Spielern ('Ich übernehme!' / 'Hilfe!').")

        with st.expander("🧠 6. Taktik II (15 Min): Transition unter Wettkampf-Bedingungen"):
            st.markdown("**Ablauf:** Endlos-Rallye-Drill. Ball muss nach erfolgreicher Abwehr sofort in einen geordneten Angriff über Pos IV/II umgewandelt werden.\n**Trainer-Details:** Strenge Taktik-Beobachtung: Wer bleibt nach der Abwehr stehen? Sofort korrigieren.")

        with st.expander("⚡ 7. Athletik II - Ermüdungs-Test (10 Min): Puls-Aufschlag"):
            st.markdown("**Ablauf:** 3x Linien-Pendelsprints (Grundlinie - 3m - Grundlinie - Netz), danach sofort 5 Aufschläge fehlerfrei ins Zielfeld bringen.\n**Trainer-Details:** Konzentration und sauberen Anwurf trotz Erschöpfung einfordern.")

        with st.expander("🏆 8. Abschlussspiel (20 Min): Transition-Match"):
            st.markdown("**Ablauf:** 3v3 / 4v4 Wash-Match.\n**Sonderregel:** Punkte zählen nur, wenn der Ballwechsel über eine erfolgreiche Abwehr-Transition gewonnen wurde.\n**Trainer-Details:** Tempo extrem hoch halten und fliegende Wechsel der wartenden Teams organisieren.")

    # ---------------- WOCHE 4 ----------------
    with w4:
        st.subheader("TE 7 (90 Min): Match-Simulation")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Pre-Game Einspielen"):
            st.markdown("**Gemeinsam:** Paarweises Warmspielen mit Fokus auf präzisen ersten Ballkontakt.")
        with st.expander("🎯 2. Technik (30 Min): Annahme-Präzisions-Test"):
            st.markdown("**Gemeinsam:** Jeder Spieler muss 10 Aufschläge annehmen; gezählt wird, wie viele perfekt im Zielkreis landen.")
        with st.expander("🧠 3. Taktik (30 Min): Abstimmung U13/U14"):
            st.markdown("**Split:** Gemischte Teams spielen mit festen Schnittstellen-Absprachen (wer nimmt Bälle in der Mitte?).")
        with st.expander("🏆 4. Abschlussspiel (20 Min): TuB Bocholt Liga"):
            st.markdown("**Turnier:** Spiel auf Zeit (4 Min pro Match). Kaiserplatz-System.")

        st.divider()

        st.subheader("TE 8 - Freitag (120 Min): Der große Monatstest")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Turnier-Warm-up"):
            st.markdown("**Gemeinsam:** Dynamisches Dehnen, Einschlagen am Netz mit Zuspiel aus der Annahme.")
        with st.expander("🎯 2. Technik (35 Min): Aufschlag & Annahme Feinschliff"):
            st.markdown("**Gemeinsam:** Duelle: Aufschläger gegen 2er/3er Annahmeriegel. Punkte für Ass vs. perfekte Annahme.")
        with st.expander("🧠 3. Taktik (35 Min): Spielaufbau unter Wettkampfstress"):
            st.markdown("**Split:** Spielstände simulieren ('23:23'). Annahme MUSS sitzen, um Sideout zu schaffen.")
        with st.expander("⚡ 4. Athletik & Auslockern (15 Min)"):
            st.markdown("**Freitags-Special:** Kurze explosive Sprungserie (3x5 Hocksprünge) + Partner-Dehnen.")
        with st.expander("🏆 5. Abschlussspiel (20 Min): Monats-Finale"):
            st.markdown("**Wettkampf:** 2 Gewinnsätze bis 15 Punkte. Volle Anwendung aller Annahme- und Laufweg-Regeln.")

# ---------------------------------------------------------
# MONAT 2: Grundtechnik Angriff & Aufschlag
# ---------------------------------------------------------
elif monat == "Monat 2: Grundtechnik Angriff & Aufschlag":
    st.header("Monat 2: Schlagen über das Netz")
    
    w1, w2, w3, w4 = st.tabs(["Woche 1", "Woche 2", "Woche 3", "Woche 4"])
    
    # ---------------- WOCHE 1 ----------------
    with w1:
        st.subheader("TE 1 (90 Min): Der Armzug")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Schulter-Aktivierung"):
            st.markdown("**Gemeinsam:** Einarmiges Baseball-Werfen paarweise. Fokus auf Aufdrehen der Schulterachse.")
        with st.expander("🎯 2. Technik (30 Min): Wand-Schlagen"):
            st.markdown("**Gemeinsam:** Vor der Wand: Hoher Ellenbogen, Handgelenk klappt aktiv ab, Ball tippt vor Wand auf den Boden.")
        with st.expander("🧠 3. Taktik/Technik (30 Min): Schlagen aus dem Stand"):
            st.markdown("**Gemeinsam:** Trainer wirft auf Pos IV. Spieler machen Stemmschritt aus dem Stand und schlagen mit Handgelenkseinsatz übers Netz.")
        with st.expander("🏆 4. Abschlussspiel (20 Min): Angriffs-Bingo"):
            st.markdown("**Punkte-Regel:** 3v3/4v4. Punkte zählen nur bei geschlagenem Ball oder aggressivem Angriff.")

        st.divider()

        st.subheader("TE 2 - Freitag (120 Min): Der 3er-Anlauf & Sprungkraft")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Rhythmus-Schulung"):
            st.markdown("**Gemeinsam:** Anlauf-Rhythmus trocken ('Links... Rechts-Links!'). Steigerung mit explosivem Armschwung nach oben.")
        with st.expander("🎯 2. Technik (35 Min): Anlauf, Absprung & Schlag"):
            st.markdown("**Gemeinsam:** Zuspieler wirft/stellt Bogenbälle. Angreifer läuft aus 3m-Distanz an, springt beidbeinig ab und schlägt über das Netz.")
        with st.expander("🧠 3. Taktik (35 Min): Hit or Lob"):
            st.markdown("**Split:** Trainer signalisiert Block. Hand oben = gezielter Lob in die Lücke. Hand unten = voller Schlagangriff.")
        with st.expander("⚡ 4. Athletik (15 Min): Sprungkraft & Rumpf"):
            st.markdown("**Freitags-Special:** Box-Jumps (auf Weichboden/Kasten) + Core-Stabi für die Bogen-Spannung in der Luft.")
        with st.expander("🏆 5. Abschlussspiel (20 Min): Angriffs-Turnier"):
            st.markdown("**Modus:** 3v3/4v4. Erfolgreiche Angriffsschläge aus vollem Anlauf zählen 2 Punkte.")

    # ---------------- WOCHE 2 ----------------
    with w2:
        st.subheader("TE 3 (90 Min): Aufschlag-Härte")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Hechten & Block-Schatten"):
            st.markdown("**Gemeinsam:** Blocksprung am Netz, landen, rückwärts ausweichen, Abwehrhecht auf den Boden, schnell hoch.")
        with st.expander("🎯 2. Technik (30 Min): Tennis-Aufschlag"):
            st.markdown("**Gemeinsam:** Aufschlag von oben ab 3m-Linie. Anwurf vor dem Körper. Bei 3 Treffern 1 Meter nach hinten gehen.")
        with st.expander("🧠 3. Taktik (30 Min): Aufschlag vs. Riegel"):
            st.markdown("**Split:** Team A schlägt hart von oben auf. Team B kontrolliert die Annahme auf den Steller. Wechsel nach 5 Bällen.")
        with st.expander("🏆 4. Abschlussspiel (20 Min): Aufschlag-Kaiser"):
            st.markdown("**Direkter As-Wechsel:** Kaiserplatz. Direktes Aufschlag-Ass bringt sofortigen Wechsel auf die Kaiserseite.")

        st.divider()

        st.subheader("TE 4 - Freitag (120 Min): Komplex-Training & Sicherung")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Reaktions-Baggern & Sprints"):
            st.markdown("**Gemeinsam:** Schnelle Sidesteps, Spielbrett stabilisieren, gefolgt von kurzen Sprints ans Netz.")
        with st.expander("🎯 2. Technik (35 Min): Freeball-Kill im Ablauf"):
            st.markdown("**Gemeinsam:** Trainer schlägt Dankeball ein. Komplette Kette: Annahme -> Zuspiel -> voller Schlagangriff (ohne Fangen).")
        with st.expander("🧠 3. Taktik (35 Min): Die Angriffssicherung"):
            st.markdown("**Split:** Angreifer schlägt absichtlich in einen Kasten-/Doppelblock. Die 2-3 Mitspieler sichern tief am Boden ab und kratzen den Abpraller hoch.")
        with st.expander("⚡ 4. Athletik (15 Min): Schulter-Power & Wurfkraft"):
            st.markdown("**Freitags-Special:** Einarmige Medizinballwürfe über das Netz + Kräftigung oberer Rücken.")
        with st.expander("🏆 5. Abschlussspiel (20 Min): Wash-Game Extrem"):
            st.markdown("**Turnier:** 2 Rallyes in Folge für Punktgewinn. Block- und Sicherungsaktionen geben Zusatzpunkte.")

    # ---------------- WOCHE 3 ----------------
    with w3:
        st.subheader("TE 5 (90 Min): Reaktion & Abwehr")
        with st.expander("🎾 1. Warm-up (10 Min): 1-gegen-1 Kreatives Tennis Game"):
            st.markdown("**Gamification:** Feld in 4-5 Schläuche teilen. 1v1. Ball darf 1x aufkommen. Alle Körperteile erlaubt. Schult die periphere Sicht.")
        with st.expander("🎯 2. Technik (30 Min): Schmetter-Abwehr"):
            st.markdown("**Gemeinsam:** Spieler stehen tief auf Pos I/V. Trainer schlägt gezielt hart an. Arme ruhig halten, Ball abprallen lassen.")
        with st.expander("🧠 3. Taktik (30 Min): Abwehr -> Transition"):
            st.markdown("**Split:** Harter Angriff -> Abwehr ins Zentrum -> Notzuspiel -> Gegenangriff über außen.")
        with st.expander("🏆 4. Abschlussspiel (20 Min): Abwehr-König"):
            st.markdown("**Sonderregel:** Spektakuläre Abwehraktionen mit erfolgreichem Gegenangriff geben 2 Punkte.")

        st.divider()

        st.subheader("TE 6 - Freitag (120 Min): Block-Timing & Feldverteidigung")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): 1v1 Tennis Auf-/Absteiger"):
            st.markdown("**Gemeinsam:** Kreatives Tennis-Game im Turniermodus über 15 Minuten. Sieger rückt ein Feld nach rechts.")
        with st.expander("🎯 2. Technik (35 Min): Der 1er- und 2er-Block"):
            st.markdown("**Gemeinsam:** Timing beim Absprung (leicht nach dem Angreifer springen), Hände fest über das Netz schieben.")
        with st.expander("🧠 3. Taktik (35 Min): Block-Abwehr-Dreieck"):
            st.markdown("**Split:** U14 stellt Doppelblock, U13 stellt 1er-Block mit V-Abwehr dahinter. Lobs und Blockabpraller ablaufen.")
        with st.expander("⚡ 4. Athletik (15 Min): Sprungausdauer am Netz"):
            st.markdown("**Freitags-Special:** Serien aus Blocksprüngen mit lateralen Sidesteps entlang des Netzes.")
        with st.expander("🏆 5. Abschlussspiel (20 Min): Block & Defense Match"):
            st.markdown("**Modus:** 3v3/4v4. Kill-Blocks zählen doppelt.")

    # ---------------- WOCHE 4 ----------------
    with w4:
        st.subheader("TE 7 (90 Min): Entscheidungsfindung")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): 1v1 Tennis Game"):
            st.markdown("**Gemeinsam:** Schnelles Warm-up mit vollem Körpereinsatz im 1-gegen-1.")
        with st.expander("🎯 2. Technik (30 Min): Hit or Lob Präzision"):
            st.markdown("**Gemeinsam:** Angreifer entscheidet blitzschnell: Harter Diagonal-Schlag oder gezielter Tip über den Block.")
        with st.expander("🧠 3. Taktik (30 Min): Systemprüfung unter Druck"):
            st.markdown("**Split:** Trainer serviert variabel. Teams müssen Annahme, Zuspiel und Angriff fehlerfrei durchbringen.")
        with st.expander("🏆 4. Abschlussspiel (20 Min): TuB Bocholt Liga"):
            st.markdown("**Turnier:** Reiner Wettkampf 3v3/4v4. Schnelle Rotation.")

        st.divider()

        st.subheader("TE 8 - Freitag (120 Min): Das große Finale")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Pre-Game Routine & Einschlagen"):
            st.markdown("**Gemeinsam:** Offizieller Spieltags-Ablauf: Paare einspielen, Angriffsschläge am Netz über Pos IV und II.")
        with st.expander("🎯 2. Technik (35 Min): Nervenstarker Aufschlag"):
            st.markdown("**Drucksituation:** '14:14 im 3. Satz'. 5 harte Aufschläge von oben fehlerfrei ins Zielfeld platzieren.")
        with st.expander("🧠 3. Taktik (35 Min): Match-Taktik & Coaching"):
            st.markdown("**Split:** Teams analysieren gegnerische Lücken selbstständig und passen ihre Angriffsziele an.")
        with st.expander("⚡ 4. Athletik (15 Min): Final-Drill & Mobilisation"):
            st.markdown("**Freitags-Special:** Schnelligkeits-Parcours + Dehnen und Cool-Down.")
        with st.expander("🏆 5. Abschlussspiel (20 Min): TuB Bocholt Meisterschaft"):
            st.markdown("**Das große Finale:** 2 Gewinnsätze bis 15 Punkte. Profi-Schiedsrichterregeln.")

# ---------------------------------------------------------
# MONAT 3: Out-of-System & Match-Speed
# ---------------------------------------------------------
elif monat == "Monat 3: Out-of-System & Match-Speed":
    st.header("Monat 3: Lösungen unter Stress")
    
    w1, w2, w3, w4 = st.tabs(["Woche 1", "Woche 2", "Woche 3", "Woche 4"])
    
    # ---------------- WOCHE 1 ----------------
    with w1:
        st.subheader("TE 1 (90 Min): Chaos-Management")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Blickkontrolle"):
            st.markdown("**Gemeinsam:** Paarweises Baggern. A hält vor Ballkontakt Finger hoch, B muss rufen wie viele. Schult periphere Sicht.")
        with st.expander("🎯 2. Technik (30 Min): Out-of-System Pass"):
            st.markdown("**Gemeinsam:** Trainer wirft tief ins Hinterfeld. Steller (oder Annahme) muss hohen Not-Pass an die Antenne (Pos IV/II) spielen. Schulter zum Ziel!")
        with st.expander("🧠 3. Taktik (30 Min): Freeball-Kill unter Zeitdruck"):
            st.markdown("**Split:** Trainer schlägt Dankeball ein. U14 hat exakt 3 Sekunden, U13 hat 4 Sekunden für Annahme, Zuspiel und Angriff.")
        with st.expander("🏆 4. Abschlussspiel (20 Min): Profi-Kaiserplatz"):
            st.markdown("**Turnier:** Ball wird per Aufschlag von oben ins Spiel gebracht. Übertreten und Netzfehler konsequent abpfeifen.")

        st.divider()

        st.subheader("TE 2 - Freitag (120 Min): Not-Pässe & Physis")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Reaktions-Chaos"):
            st.markdown("**Gemeinsam:** 2 Bälle gleichzeitig im 3er-Team jonglieren (pritschen/baggern). Hohe Kommunikation gefordert.")
        with st.expander("🎯 2. Technik (35 Min): Den schlechten Pass erlaufen"):
            st.markdown("**Gemeinsam:** Trainer wirft Bälle extrem streuend. Zuspieler muss sprinten, komplett abstoppen (!) und den Not-Pass spielen.")
        with st.expander("🧠 3. Taktik (35 Min): Butterfly unter Druck"):
            st.markdown("**Split:** Endlos-System. Team A wehrt ab und greift an. Fällt der Ball, rückt sofort das wartende Team nach.")
        with st.expander("⚡ 4. Athletik (15 Min): Sprint-Ausdauer"):
            st.markdown("**Freitags-Special:** Linien-Pendel-Sprints (Linien antippen). Zielt auf Erschöpfungsresistenz im 3. Satz.")
        with st.expander("🏆 5. Abschlussspiel (20 Min): Out-of-System Bonus"):
            st.markdown("**Sonderregel:** Ein Punkt, der nach einem völlig verunglückten ersten Ball (Rettungstat) erzielt wird, zählt doppelt.")

    # ---------------- WOCHE 2 ----------------
    with w2:
        st.subheader("TE 3 (90 Min): Scramble Offense")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Ball-Klau im 3m-Raum"):
            st.markdown("**Gemeinsam:** Dribbeln und anderen den Ball wegschlagen. Fördert Übersicht und Fußarbeit.")
        with st.expander("🎯 2. Technik (30 Min): Angriff aus dem Hinterfeld"):
            st.markdown("**Gemeinsam:** Wenn der Pass nicht ans Netz kommt: Angreifer muss lernen, den Ball von der 3m-Linie oder aus dem Stand lang ins gegnerische Feld zu drücken.")
        with st.expander("🧠 3. Taktik (30 Min): Rettungsaktion -> Angriff"):
            st.markdown("**Split:** Annahme klebt im Netz oder fliegt Richtung Aus. Spieler kratzt ihn hoch, der 3. Ball *muss* als bewusster Lob/Schlag rüber.")
        with st.expander("🏆 4. Abschlussspiel (20 Min): Kein Dankeball"):
            st.markdown("**Punkte-Regel:** Wer einen Ball 'einfach so' per Bagger oder als Dankeball rüberspielt, kassiert einen Minuspunkt. Es muss immer aufgebaut werden.")

        st.divider()

        st.subheader("TE 4 - Freitag (120 Min): Fehlerkompensation & Rumpf")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Koordinations-Sprints"):
            st.markdown("**Gemeinsam:** Sprints aus dem Sitzen, Liegen und Kniestand auf Kommando.")
        with st.expander("🎯 2. Technik (35 Min): Tip/Lob aus der Not"):
            st.markdown("**Gemeinsam:** Der Pass kommt zu nah ans Netz (Block wartet). Angreifer muss abspringen und den Ball clever ins Zentrum der Gegner tippen.")
        with st.expander("🧠 3. Taktik (35 Min): Sicherung bei schlechten Pässen"):
            st.markdown("**Split:** Pass ist unpräzise. Die gesamte Mannschaft muss sofort 2 Schritte Richtung Angreifer rücken, um ihn abzusichern, falls er geblockt wird.")
        with st.expander("⚡ 4. Athletik (15 Min): Rumpf für die Luftkontrolle"):
            st.markdown("**Freitags-Special:** Bauchmuskel-Zirkel und Rückenstrecker (Supermans) für Körperkontrolle in der Luft.")
        with st.expander("🏆 5. Abschlussspiel (20 Min): Wash-Game Extrem"):
            st.markdown("**Turnier:** 3 Rallyes am Stück gewinnen für einen großen Punkt. Absolute Nervenprobe.")

    # ---------------- WOCHE 3 ----------------
    with w3:
        st.subheader("TE 5 (90 Min): High-Speed Transition")
        with st.expander("🎾 1. Warm-up (10 Min): Volley-Tennis"):
            st.markdown("**Gemeinsam:** 1v1 Chaos-Tennis. 1x Aufkommen erlaubt, alle Körperteile dürfen benutzt werden.")
        with st.expander("🎯 2. Technik (30 Min): Abwehr -> Sofort-Angriff"):
            st.markdown("**Gemeinsam:** Spieler wehrt harten Ball ab, macht sofort (!) den 3er-Rhythmus und greift den gestellten Notpass an.")
        with st.expander("🧠 3. Taktik (30 Min): Dauerfeuer"):
            st.markdown("**Split:** Trainer wirft 5 Bälle pro Team in 10 Sekunden ein. Sofortiges Reagieren, Abwehren und Umschalten gefordert.")
        with st.expander("🏆 4. Abschlussspiel (20 Min): Speed-Turnier"):
            st.markdown("**Modus:** 3v3 / 4v4. Ball tot = Trainer wirft sofort in Sekunde 1 den nächsten Ball ein. Keine Zeit zum Durchatmen.")

        st.divider()

        st.subheader("TE 6 - Freitag (120 Min): Wettkampfhärte & Beine")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): 1v1 Auf-/Absteiger"):
            st.markdown("**Gemeinsam:** Volley-Tennis im Turniermodus (Minifelder).")
        with st.expander("🎯 2. Technik (35 Min): Aufschlagdruck vs. Transition"):
            st.markdown("**Gemeinsam:** U14 feuert Aufschläge auf U13. U13 muss annehmen, aufbauen und sofort auf eine erneute Abwehraktion umschalten.")
        with st.expander("🧠 3. Taktik (35 Min): Rallye aufrechterhalten"):
            st.markdown("**Split:** Fokus liegt darauf, den Ball unter allen Umständen im Spiel zu halten. Lobs, Blocksicherung und Hechtbagger.")
        with st.expander("⚡ 4. Athletik (15 Min): Schnelle Füße"):
            st.markdown("**Freitags-Special:** Skippings, High-Knees und kurze Antritt-Sprints am Netz.")
        with st.expander("🏆 5. Abschlussspiel (20 Min): Transition-König"):
            st.markdown("**Modus:** Ein Punkt zählt erst, wenn der Ball mindestens 3x (pro Seite) über das Netz ging (lange Rallye erzwungen).")

    # ---------------- WOCHE 4 ----------------
    with w4:
        st.subheader("TE 7 (90 Min): Match-Day Vorbereitung")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Pre-Game Routine"):
            st.markdown("**Gemeinsam:** Komplettes offizielles Einschlagen (Paarweise -> Netz -> Aufschlag).")
        with st.expander("🎯 2. Technik (30 Min): Der sichere Not-Aufschlag"):
            st.markdown("**Gemeinsam:** Wenn die Luft raus ist: Sicherer Aufschlag von unten oder leichter Float, der zu 100% ins Feld muss.")
        with st.expander("🧠 3. Taktik (30 Min): Abstimmung U13/U14 Mix"):
            st.markdown("**Split:** Gemischte Teams (3v3 oder 4v4). Wer deckt welche Räume? Absprachen für das Abschluss-Turnier treffen.")
        with st.expander("🏆 4. Abschlussspiel (20 Min): Liga Hinrunde"):
            st.markdown("**Turnier:** Start des großen Monats-Turniers. Jeder gegen Jeden. Punkte notieren!")

        st.divider()

        st.subheader("TE 8 - Freitag (120 Min): Das Saison-Finale")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Turnier-Warm-up"):
            st.markdown("**Gemeinsam:** Fokus und Konzentration. Dynamisches Einspielen.")
        with st.expander("🎯 2. Technik (35 Min): Feinschliff & Duelle"):
            st.markdown("**Gemeinsam:** Angreifer gegen Blockspieler. Aufschläger gegen Annahmeriegel. Direkte 1v1 / 2v2 Duelle zur Schärfung.")
        with st.expander("🧠 3. Taktik (35 Min): Timeout-Coaching"):
            st.markdown("**Split:** Teams simulieren Spielstände. Sie dürfen selbst Timeouts nehmen und müssen ohne Trainer eine taktische Lösung finden.")
        with st.expander("⚡ 4. Athletik (15 Min): Explosivität & Cool-down"):
            st.markdown("**Freitags-Special:** Letzte kurze Sprintserie, danach 10 Minuten ausgiebiges gemeinsames Dehnen.")
        with st.expander("🏆 5. Abschlussspiel (20 Min): Liga Finale"):
            st.markdown("**Das große Finale:** Die Rückrunde. 2 Gewinnsätze, volle Regeln, absolute Wettkampfbedingungen. Krönung des Monats-Siegers!")

# ---------------------------------------------------------
# SYSTEM-SPEZIAL
# ---------------------------------------------------------
elif monat == "System-Spezial: 3v3 meets 4v4":
    st.header("System-Spezial: Transition & Kognition")
    st.success("Tipp: Nutze diese Übungen für gezieltes Kleingruppentraining.")
    
    with st.expander("⏱️ 1. Der Transition-Läufer (U13 & U14) (15 Min)"):
        st.markdown("""
        **Aus der Abwehr ins Zuspiel:** 
        Trainer schlägt auf den Zuspieler. Der Zuspieler wehrt ab, ein anderer übernimmt das Not-Zuspiel.
        * **U13:** Der Läufer startet von hinten (Pos I).
        * **U14:** Der Zuspieler (meist Pos II) lässt sich in die Abwehr fallen und wird vertreten.
        """)
    with st.expander("👀 2. Das Scanner-Zuspiel (20 Min)"):
        st.markdown("**Block lesen:** Trainer hebt linke oder rechte Hand. Zuspieler pritscht dorthin, wo die Hand *unten* ist. U14 Zuspieler müssen im Sprung zuspielen!")
    with st.expander("🌪️ 3. Der Dauerläufer (20 Min)"):
        st.markdown("""
        **Physische Härte für den Spielmacher:**
        * **U13:** Sprint Pos I -> III -> Zuspiel IV. Zurück auf I. 10x am Stück.
        * **U14:** Start auf Pos II. Block-Sprung -> Zurückziehen auf 3m-Linie -> Zuspiel aus der Bewegung auf IV. 10x am Stück.
        """)
    with st.expander("🏆 4. Spielform: Der Libero-Joker (20 Min)"):
        st.markdown("**3v3 mit Abwehr-Chef:** Ein U14-Spieler sichert hinten als Libero ab und rettet weite Bälle für die U13.")
