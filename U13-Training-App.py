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
    
    # ---------------- WOCHE 1 ----------------
    with w1:
        st.subheader("TE 1 (90 Min): Das sichere Spielbrett")
        with st.expander("🏃‍♂️ 1. Warm-up: Reaktions-Baggern (10 Min)"):
            st.markdown("""
            **Gemeinsam:** Paarweise. Spieler A wirft leicht seitlich. Spieler B macht schnellen Sidestep, formt das Spielbrett und baggert präzise zurück.
            
            **Trainer-Details:** Achte strikt darauf, dass die Beinarbeit *vor* der Armarbeit passiert! Häufiger Fehler: Kinder laufen mit bereits gefalteten Händen zum Ball. Korrektur: Erst hinlaufen, abstoppen, dann das Spielbrett schließen. Die Bewegung kommt aus den Beinen, nicht aus dem Schwingen der Arme.
            """)
        with st.expander("🎯 2. Technik: Ziel-Baggern zum Steller (30 Min)"):
            st.markdown("""
            **Gemeinsam:** Kasten auf Pos II/III. Trainer wirft Bälle an. Armwinkel so ausrichten, dass der Ball im hohen Bogen genau auf das Steller-Ziel fällt.
            
            **Trainer-Details:** Stell dich genau hinter den Kasten (das Ziel). So siehst du, ob die Schulterachse der Spieler wirklich zu dir zeigt. Das innere Bein (zur Spielfeldmitte) sollte leicht vorne stehen, um den Ball automatisch ins Zentrum zu lenken.
            """)
        with st.expander("🧠 3. Taktik: Annahme-Riegel formieren (30 Min)"):
            st.markdown("""
            **Split:** Seite A (U14 - 3er Riegel), Seite B (U13 - 2er Riegel). Trainer schlägt leichte Bälle ein. Fokus: Lautes Rufen ('Ich!') und Pass zum Steller (dieser fängt).
            
            **Trainer-Details:** Hier geht es nur um Kommunikation. Wer zuerst 'Ich' ruft, hat Vorfahrt. Wenn zwei Spieler zögern oder zusammenstoßen, unterbrich sofort. Der Steller muss lernen, den Ball lautstark einzufordern ('Zu mir!').
            """)
        with st.expander("🏆 4. Abschlussspiel: Annahme-Bingo (20 Min)"):
            st.markdown("""
            **Punkte-Regel:** 3v3/4v4. Zusatzpunkt, wenn die Annahme perfekt beim Zuspieler landet (ohne dass dieser laufen muss).
            
            **Trainer-Details:** Du bist der Schiedsrichter. Werte streng: Musste der Zuspieler mehr als einen Schritt machen, gibt es keinen Zusatzpunkt. Das zwingt die Annahmespieler, hoch und in die Feldmitte zu spielen, statt den Ball nur flach über das Netz zu schießen.
            """)

        st.divider()
        st.subheader("TE 2 - Freitag (120 Min): Annahme unter Druck & Athletik")
        with st.expander("🏃‍♂️ 1. Warm-up: Tiefe Abwehr & Linien-Chaos (15 Min)"):
            st.markdown("""
            **Gemeinsam:** Linienfangen kombiniert mit Sidesteps und tiefem Abwehr-Stopp auf Pfiff. Tiefe Haltung permanent einfordern.
            
            **Trainer-Details:** Fordere die 'Ready-Position': Knie gebeugt, Gewicht auf dem Vorfuß, Arme sind angewinkelt vor dem Körper, Blick nach vorne. Wer aufrecht steht, wird sofort ermahnt.
            """)
        with st.expander("🎯 2. Technik: Dankeball-Sprint & Annahme (35 Min)"):
            st.markdown("""
            **Gemeinsam:** Spieler startet Grundlinie. Trainer ruft 'Go!' und wirft kurz hinters Netz. Spieler sprintet, stoppt komplett ab und baggert hoch zum Steller.
            
            **Trainer-Details:** Der Fokus liegt auf dem Bremsweg. Nach dem Vollsprint müssen die Füße einen sicheren Stand finden. Wenn der Ball im Baggern seitlich wegfliegt, lag das Gewicht des Spielers noch in der Vorwärtsbewegung.
            """)
        with st.expander("🧠 3. Taktik: Serve & Pass Komplex (35 Min)"):
            st.markdown("""
            **Split:** U14 schlägt von oben auf. U13 kontrolliert harte Aufschläge. Fokus: Keine Arm-Bewegung beim Baggern harter Bälle!
            
            **Trainer-Details:** Bei harten Aufschlägen darf das Spielbrett nicht mehr geschwungen werden (sonst fliegt der Ball an die Decke). Der Winkel der Arme muss einfach nur gehalten werden. Der Ball springt von alleine ab. 'Bagger als Wand benutzen!'
            """)
        with st.expander("⚡ 4. Athletik & Aufschlag-Präzision (15 Min)"):
            st.markdown("""
            **Freitags-Special:** 3 Runden Rumpf- & Sprungkraft. Danach sofort 5 Ziel-Aufschläge mit erhöhtem Puls.
            
            **Trainer-Details:** Achte bei der Plank (Unterarmstütz) auf einen geraden Rücken (kein Hohlkreuz). Bei den Aufschlägen unter Belastung musst du kontrollieren, ob der Anwurf noch sauber ist. Ermüdete Spieler werfen den Ball oft unkontrolliert an.
            """)
        with st.expander("🏆 5. Abschlussspiel: Handicap-Match (20 Min)"):
            st.markdown("""
            **4v3:** U14 gegen U13. Wenn die Annahme der U13 wackelt, schlägt U14 nur von unten auf.
            
            **Trainer-Details:** Steuere das Spielniveau aktiv. Wenn die U13 völlig untergeht, greifst du ein. Das Ziel ist es, lange Ballwechsel zu generieren, damit das System verinnerlicht wird.
            """)

    # ---------------- WOCHE 2 ----------------
    with w2:
        st.subheader("TE 3 (90 Min): Zuspieler-Integration")
        with st.expander("🏃‍♂️ 1. Warm-up: Kognitives Chaos (10 Min)"):
            st.markdown("""
            **Gemeinsam:** Paarweise am Netz. A pritscht Ball 1, B rollt Ball 2. Auf Pfiff: Sprint zur Grundlinie und zurück.
            
            **Trainer-Details:** Fehler sind hier erwünscht! Die Übung überlastet das Gehirn absichtlich. Bleib laut und motivierend, fordere schnelle Reaktionen nach dem Pfiff.
            """)
        with st.expander("🎯 2. Technik: Annahme + Zuspiel (30 Min)"):
            st.markdown("""
            **Gemeinsam:** Annahme baggert zum Steller. Der Steller pritscht den Ball hoch auf Pos IV. Steller muss vor dem Pass stehen!
            
            **Trainer-Details:** Der Zuspieler ist der wichtigste Mann hier. Beobachte seine Füße. Er muss das rechte Bein leicht vorne haben, um den Körper zum Ziel (Pos IV) auszurichten. Gespielt wird über der Stirn, nicht vor der Brust.
            """)
        with st.expander("🧠 3. Taktik: Mixed-System Laufwege (30 Min)"):
            st.markdown("""
            **Split:** Seite A (U14 Raute), Seite B (U13 Läufer). Trainer wirft ein. Steller läuft erst los, wenn der Ball den Trainer verlässt.
            
            **Trainer-Details:** Ein reiner Positions-Drill. Greife rigoros durch, wenn der Zuspieler zu früh losläuft (Positionsfehler!). Er muss lernen, den Ball in der Luft zu beobachten und dann den kürzesten Weg ans Netz zu nehmen.
            """)
        with st.expander("🏆 4. Abschlussspiel: Wash-Game (20 Min)"):
            st.markdown("""
            **Punkte-Regel:** 2 Rallyes in Folge gewinnen = 1 Punkt. Fördert die Konzentration.
            
            **Trainer-Details:** Lass das Spiel fließen. Wirf den zweiten Ball sofort nach Ende der ersten Rallye ein, um den Rhythmus hochzuhalten. Wer nachlässig wird, verliert den großen Punkt.
            """)

        st.divider()
        st.subheader("TE 4 - Freitag (120 Min): System-Festigung & Dauerbelastung")
        with st.expander("🏃‍♂️ 1. Warm-up: Aufschlag-Staffel & Koordination (15 Min)"):
            st.markdown("""
            **Gemeinsam:** Staffel mit Ball prellen, Anwurf-Simulation am Netz und schnellen Richtungswechseln.
            
            **Trainer-Details:** Achte bei der Anwurf-Simulation darauf, dass der Ball vor der Schlag-Schulter angeworfen wird und eine minimale Rotation hat (beim Flatteraufschlag).
            """)
        with st.expander("🎯 2. Technik: Zonen-Aufschlag vs. Annahme (35 Min)"):
            st.markdown("""
            **Gemeinsam:** U14 schlägt gezielt auf Turnmatten in den Ecken. U13 steht in Annahme und verteidigt die Matten.
            
            **Trainer-Details:** Positioniere dich auf der Seite der U13. Beobachte, wie der Annahmeriegel verschiebt. Bei Aufschlägen aus der Mitte stehen sie neutral. Schlägt der Gegner von der Seitenlinie auf, muss der Riegel dorthin rotieren.
            """)
        with st.expander("🧠 3. Taktik: Rette das System (Out-of-System) (35 Min)"):
            st.markdown("""
            **Split:** Trainer wirft unpräzise Bälle (Netz, Aus). Ein anderer Spieler muss laut 'Hilfe' rufen und das Zuspiel übernehmen.
            
            **Trainer-Details:** Die Umschaltung im Kopf ist entscheidend. Sobald klar ist, dass der Steller den Ball nicht bekommt, muss der nächste Spieler (oft der Angreifer auf Pos IV oder II) sofort und laut das Kommando übernehmen. Passiert das nicht, unterbrich die Übung.
            """)
        with st.expander("⚡ 4. Athletik: Beinarbeit & Quickness (15 Min)"):
            st.markdown("""
            **Freitags-Special:** Koordinationsleiter/Linien-Drills für schnelle Fußarbeit + Medizinball-/Ball-Würfe.
            
            **Trainer-Details:** Qualität vor Quantität. Bei der Koordinationsleiter müssen die Fersen in der Luft bleiben (Vorfuß-Lauf). Die Medizinballwürfe imitieren die Core-Rotation beim Angriff.
            """)
        with st.expander("🏆 5. Abschlussspiel: System-Kaiser (20 Min)"):
            st.markdown("""
            **Sonderregel:** Herausforderer rücken nur auf Kaiser-Seite vor, wenn der Ball im 3er-System aufgebaut wurde.
            
            **Trainer-Details:** Erkenne auch den *Versuch* des Systemaufbaus an. Wenn der Ball nach dem Steller-Pass unglücklich ins Aus geht, lobe den strukturierten Aufbau. Wenn der Ball einfach nur drübergebaggert wird = Punktverlust.
            """)

    # ---------------- WOCHE 3 ----------------
    with w3:
        st.subheader("TE 5 (90 Min): Annahme-Konstanz")
        with st.expander("🏃‍♂️ 1. Warm-up: Reaktions-Sprints (10 Min)"):
            st.markdown("""
            **Gemeinsam:** Bauchlage am Netz. Auf Pfiff: Aufstehen, Rückwärtslauf bis 3m-Linie, Vorwärtssprint.
            
            **Trainer-Details:** Trainiert die Explosivität. Beim Rückwärtslaufen müssen die Spieler über die Schulter schauen, damit es keine Zusammenstöße gibt (Schult den Raum-Blick).
            """)
        with st.expander("🎯 2. Technik: Annahme aus der Bewegung (30 Min)"):
            st.markdown("""
            **Gemeinsam:** Spieler laufen seitlich in den Ballweg ein und stabilisieren das Spielbrett im Moment des Kontakts.
            
            **Trainer-Details:** Der klassische Fehler hierbei ist das seitliche Ausstrecken der Arme, ohne mit den Beinen nachzurücken. Verlange immer den Sidestep hinter den Ball. Der Ball muss zentral vor dem Rumpf gespielt werden.
            """)
        with st.expander("🧠 3. Taktik: Aufschlag-Druck vs. Annahme-Riegel (30 Min)"):
            st.markdown("""
            **Split:** Annahmeriegel muss sich aktiv verschieben, wenn der Aufschläger seine Position an der Grundlinie verändert.
            
            **Trainer-Details:** Steh beim Aufschläger und zeige ihm an, von wo er servieren soll (z.B. extrem von ganz links). Beobachte, ob die Annahme-Spieler drüben diese Lücke erkennen und ihren Riegel entsprechend anpassen, um den Kreuzwinkel abzudecken.
            """)
        with st.expander("🏆 4. Abschlussspiel: Druck-Turnier (20 Min)"):
            st.markdown("""
            **Punkte-Regel:** Annahmefehler (direktes As) gibt 2 Punkte für das aufschlagende Team.
            
            **Trainer-Details:** Das erhöht den psychologischen Druck auf die Annahme. Erinnere sie in Auszeiten an die Grundtechnik (tief bleiben, Winkel halten).
            """)

        st.divider()
        st.subheader("TE 6 - Freitag (120 Min): Transition Defensive -> Annahme")
        with st.expander("🏃‍♂️ 1. Warm-up: 1v1 Volley-Tennis (15 Min)"):
            st.markdown("""
            **Gemeinsam:** 1v1 in kleinen Feldern. Ball darf 1x tippen. Alle Körperteile erlaubt.
            
            **Trainer-Details:** Halte das Tempo extrem hoch. Ermutige die Spieler, die kurzen Bälle (Lobs) des Gegners zu erlaufen. Fokus auf Start-Schnelligkeit.
            """)
        with st.expander("🎯 2. Technik: Not-Annahme am Boden (35 Min)"):
            st.markdown("""
            **Gemeinsam:** Hechtbagger und einarmige Rettungsaktionen mit kontrolliertem hohen Ballbogen ins Zentrum.
            
            **Trainer-Details:** Mache die Technik vor: Wer nach dem Ball taucht (Hechtbagger/Sprawl), gleitet über Brust und Bauch ab. Keine Knie voraus in den Boden (Verletzungsgefahr!). Der Ball muss hoch gespielt werden, um dem Team Zeit zu kaufen.
            """)
        with st.expander("🧠 3. Taktik: Umschaltspiel nach Abwehr (35 Min)"):
            st.markdown("""
            **Split:** Aus der Feldabwehr heraus sofort wieder in die Annahme-Struktur für den zweiten Ball formieren.
            
            **Trainer-Details:** Nach einer Abwehraktion bleiben Spieler oft am Boden liegen oder schauen ihrem Ball hinterher. Das Kommando muss lauten: 'Ball ist oben, sofort zurück in die Position!' (Transition).
            """)
        with st.expander("⚡ 4. Athletik: Rumpfstabilität & Schultern (15 Min)"):
            st.markdown("""
            **Freitags-Special:** Kräftigung Rotatorenmanschette mit Thera-Bändern + Unterarmstütz-Variationen.
            
            **Trainer-Details:** Kontrolliere die Haltung beim Thera-Band. Ellenbogen bleibt eng am Körper, nur der Unterarm rotiert nach außen. Wichtig für die Verletzungsprävention der Schlag-Schulter.
            """)
        with st.expander("🏆 5. Abschlussspiel: Transition-Match (20 Min)"):
            st.markdown("""
            **Modus:** 3v3/4v4. Schneller Ballwechsel-Rhythmus mit Trainer-Einwurf sofort nach Rallye-Ende.
            
            **Trainer-Details:** Deine Aufgabe ist es, die Spieler physisch an die Grenze zu bringen. Wirf den Ball sofort ein. Wer nicht auf seiner Position steht, verliert den Punkt.
            """)

    # ---------------- WOCHE 4 ----------------
    with w4:
        st.subheader("TE 7 (90 Min): Match-Simulation")
        with st.expander("🏃‍♂️ 1. Warm-up: Pre-Game Einspielen (10 Min)"):
            st.markdown("""
            **Gemeinsam:** Paarweises Warmspielen mit Fokus auf präzisen ersten Ballkontakt.
            
            **Trainer-Details:** Beobachte das Einspielen wie vor einem wichtigen Ligaspiel. Korrigiere Schlampigkeit sofort. Jede Berührung muss spielnah sein (tiefer Stand).
            """)
        with st.expander("🎯 2. Technik: Annahme-Präzisions-Test (30 Min)"):
            st.markdown("""
            **Gemeinsam:** Jeder Spieler nimmt 10 Aufschläge an; zähle wie viele perfekt im Zielkreis (Steller-Pos) landen.
            
            **Trainer-Details:** Baut einen kleinen Wettkampf ein. Notiere die Werte mental. Wem unter Druck die Nerven versagen, der profitiert davon, sich diese Stresssituation bewusst zu machen.
            """)
        with st.expander("🧠 3. Taktik: Abstimmung U13/U14 (30 Min)"):
            st.markdown("""
            **Split:** Gemischte Teams spielen mit festen Schnittstellen-Absprachen.
            
            **Trainer-Details:** Lass die U14-Spieler die Führung übernehmen. Sie sollen den Jüngeren ansagen, wer den Ball zwischen zwei Spielern in der Mitte (in der Naht) nimmt. Das fördert Leadership.
            """)
        with st.expander("🏆 4. Abschlussspiel: TuB Bocholt Liga (20 Min)"):
            st.markdown("""
            **Turnier:** Spiel auf Zeit (4 Min pro Match). Kaiserplatz-System.
            
            **Trainer-Details:** Tritt in den Hintergrund. Lass sie spielen und Fehler machen. Greife nur ein, wenn die Energie sinkt.
            """)

        st.divider()
        st.subheader("TE 8 - Freitag (120 Min): Der große Monatstest")
        with st.expander("🏃‍♂️ 1. Warm-up: Turnier-Warm-up (15 Min)"):
            st.markdown("""
            **Gemeinsam:** Dynamisches Dehnen, Einschlagen am Netz mit Zuspiel aus der Annahme.
            
            **Trainer-Details:** Achte beim Einschlagen darauf, dass sich niemand in das Netz springt. Der Zuspieler verteilt die Bälle sauber.
            """)
        with st.expander("🎯 2. Technik: Aufschlag & Annahme Feinschliff (35 Min)"):
            st.markdown("""
            **Gemeinsam:** Duelle: Aufschläger gegen 2er/3er Annahmeriegel. Punkte für Ass vs. perfekte Annahme.
            
            **Trainer-Details:** Fokussiere dich auf den Aufschläger. Eine harte, flache Flugkurve direkt über die Netzkante ist das Ziel. Hohe Bogen-Aufschläge werden von der Annahme zu leicht verarbeitet.
            """)
        with st.expander("🧠 3. Taktik: Spielaufbau unter Wettkampfstress (35 Min)"):
            st.markdown("""
            **Split:** Spielstände simulieren ('23:23'). Annahme MUSS sitzen, um Sideout zu schaffen.
            
            **Trainer-Details:** Beobachte die Körpersprache. Wer versteckt sich bei 23:23? Fordere von den Schlüsselspielern, in diesen Momenten Verantwortung zu übernehmen und den Ball lautstark zu fordern.
            """)
        with st.expander("⚡ 4. Athletik & Auslockern (15 Min)"):
            st.markdown("""
            **Freitags-Special:** Kurze explosive Sprungserie (3x5 Hocksprünge) + Partner-Dehnen.
            
            **Trainer-Details:** Das Dehnen am Ende ist wichtig, um die Laktat-Zirkulation zu fördern. Zeige, wie Partner sich beim Dehnen (z.B. Brustmuskel) unterstützen können, ohne zu zerren.
            """)
        with st.expander("🏆 5. Abschlussspiel: Monats-Finale (20 Min)"):
            st.markdown("""
            **Wettkampf:** 2 Gewinnsätze bis 15 Punkte. Volle Anwendung aller Regeln.
            
            **Trainer-Details:** Sei der strenge Schiedsrichter auf dem Bock. Übertreten, Netzfehler, Doppelkontakt – pfeif alles gnadenlos ab. Das bereitet sie mental perfekt auf die echte Liga vor.
            """)

# ---------------------------------------------------------
# MONAT 2: Grundtechnik Angriff & Aufschlag
# ---------------------------------------------------------
elif monat == "Monat 2: Grundtechnik Angriff & Aufschlag":
    st.header("Monat 2: Schlagen über das Netz")
    
    w1, w2, w3, w4 = st.tabs(["Woche 1", "Woche 2", "Woche 3", "Woche 4"])
    
    # ---------------- WOCHE 1 ----------------
    with w1:
        st.subheader("TE 1 (90 Min): Der Armzug")
        with st.expander("🏃‍♂️ 1. Warm-up: Schulter-Aktivierung (10 Min)"):
            st.markdown("""
            **Gemeinsam:** Einarmiges Baseball-Werfen paarweise. Fokus auf Aufdrehen der Schulterachse.
            
            **Trainer-Details:** Achte darauf, dass der Wurf aus der Körperrotation kommt. Die nicht-werfende Schulter zeigt zuerst zum Partner, dann dreht der Oberkörper ein. Ellenbogen hochhalten!
            """)
        with st.expander("🎯 2. Technik: Wand-Schlagen (30 Min)"):
            st.markdown("""
            **Gemeinsam:** Vor der Wand: Hoher Ellenbogen, Handgelenk klappt aktiv ab, Ball tippt vor Wand auf den Boden.
            
            **Trainer-Details:** Der häufigste Fehler: Die Kinder 'schieben' den Ball aus der Schulter. Zwinge sie, den Ball mit der flachen, harten Hand zu treffen und den Arm komplett durchzuschwingen (Follow-through bis zur Hüfte).
            """)
        with st.expander("🧠 3. Taktik/Technik: Schlagen aus dem Stand (30 Min)"):
            st.markdown("""
            **Gemeinsam:** Trainer wirft auf Pos IV. Spieler machen Stemmschritt aus dem Stand und schlagen mit Handgelenkseinsatz übers Netz.
            
            **Trainer-Details:** Steh seitlich zum Angreifer. Der linke Fuß (bei Rechtshändern) muss leicht eingedreht sein. Der Armzug muss explosiv sein. Der Ball muss vor dem Körper (auf 1-2 Uhr Position) getroffen werden, nicht hinter dem Kopf!
            """)
        with st.expander("🏆 4. Abschlussspiel: Angriffs-Bingo (20 Min)"):
            st.markdown("""
            **Punkte-Regel:** 3v3/4v4. Punkte zählen nur bei geschlagenem Ball oder aggressivem Angriff.
            
            **Trainer-Details:** Unterbrich, wenn Bälle aus Faulheit nur im Bagger rübergespielt werden. Notfalls Minuspunkt. Der Mut zum Schlagen (auch wenn der Ball im Aus landet) muss belohnt werden.
            """)

        st.divider()
        st.subheader("TE 2 - Freitag (120 Min): Der 3er-Anlauf & Sprungkraft")
        with st.expander("🏃‍♂️ 1. Warm-up: Rhythmus-Schulung (15 Min)"):
            st.markdown("""
            **Gemeinsam:** Anlauf-Rhythmus trocken ('Links... Rechts-Links!'). Steigerung mit explosivem Armschwung nach oben.
            
            **Trainer-Details:** Der letzte Doppelschritt (Rechts-Links) muss rasend schnell ('Tack-Tack') und aggressiv sein. Die Arme müssen vor dem Sprung weit nach hinten gerissen werden.
            """)
        with st.expander("🎯 2. Technik: Anlauf, Absprung & Schlag (35 Min)"):
            st.markdown("""
            **Gemeinsam:** Zuspieler wirft Bogenbälle. Angreifer läuft aus 3m-Distanz an, springt beidbeinig ab und schlägt.
            
            **Trainer-Details:** Oft laufen die Kinder zu früh los und springen dann *unter* den Ball. Sie müssen warten, bis der Ball den höchsten Punkt erreicht hat, und dann explosiv in den Ball hineinlaufen.
            """)
        with st.expander("🧠 3. Taktik: Hit or Lob (35 Min)"):
            st.markdown("""
            **Split:** Trainer signalisiert Block. Hand oben = gezielter Lob in die Lücke. Hand unten = voller Schlagangriff.
            
            **Trainer-Details:** Der Angreifer muss lernen, trotz des vollen Anlaufs und der Aggressivität in der Luft das Feld im Blick zu haben. Der Lob ('Tip') darf nicht aus dem Ellenbogen geworfen werden, sondern die Schlagbewegung wird kurz vor dem Treffpunkt gestoppt.
            """)
        with st.expander("⚡ 4. Athletik: Sprungkraft & Rumpf (15 Min)"):
            st.markdown("""
            **Freitags-Special:** Box-Jumps (auf Weichboden) + Core-Stabi für die Bogen-Spannung in der Luft.
            
            **Trainer-Details:** Box-Jumps erfordern volle Konzentration. Landung auf der Box mit weichen Knien (federn). Die Core-Stabi (Bauch/Rücken) ist essenziell, damit der Körper in der Luft nicht einknickt wie ein nasser Sack.
            """)
        with st.expander("🏆 5. Abschlussspiel: Angriffs-Turnier (20 Min)"):
            st.markdown("""
            **Modus:** 3v3/4v4. Erfolgreiche Angriffsschläge aus vollem Anlauf zählen 2 Punkte.
            
            **Trainer-Details:** Feiere jeden mutigen Angriff! Die Zuspieler müssen die Bälle hoch ans Netz stellen, damit überhaupt angegriffen werden kann. Coach die Zuspieler, wenn die Pässe zu flach sind.
            """)

    # ---------------- WOCHE 2 ----------------
    with w2:
        st.subheader("TE 3 (90 Min): Aufschlag-Härte")
        with st.expander("🏃‍♂️ 1. Warm-up: Hechten & Block-Schatten (10 Min)"):
            st.markdown("""
            **Gemeinsam:** Blocksprung am Netz, landen, rückwärts ausweichen, Abwehrhecht auf den Boden, schnell hoch.
            
            **Trainer-Details:** Die Landung beim Blocksprung muss auf beiden Füßen kontrolliert erfolgen, bevor das Ausweichen beginnt. Verletzungsgefahr minimieren!
            """)
        with st.expander("🎯 2. Technik: Tennis-Aufschlag (30 Min)"):
            st.markdown("""
            **Gemeinsam:** Aufschlag von oben ab 3m-Linie. Anwurf vor dem Körper. Bei 3 Treffern 1 Meter nach hinten gehen.
            
            **Trainer-Details:** Der Anwurf ist 80% des Aufschlags. Der Ball muss leicht vor der Schlagschulter sein und darf nicht zu hoch (schwer zu timen) oder zu niedrig (Ball landet im Netz) geworfen werden. Blockiere Spieler, die aus der Hand schlagen.
            """)
        with st.expander("🧠 3. Taktik: Aufschlag vs. Riegel (30 Min)"):
            st.markdown("""
            **Split:** Team A schlägt hart von oben auf. Team B kontrolliert die Annahme auf den Steller.
            
            **Trainer-Details:** Steh hinter der Annahme. Wenn die Aufschläger zu viele Fehler machen, zwinge sie einen Schritt vorzugehen. Der Riegel muss konstant unter realem Druck arbeiten.
            """)
        with st.expander("🏆 4. Abschlussspiel: Aufschlag-Kaiser (20 Min)"):
            st.markdown("""
            **Direkter As-Wechsel:** Kaiserplatz. Direktes Aufschlag-Ass bringt sofortigen Wechsel auf die Kaiserseite.
            
            **Trainer-Details:** Dies verleitet zu Risikoaufschlägen. Beobachte, ob die Spieler trotz Risiko ihre Technik (Anwurf, harter Handgelenks-Kontakt) sauber durchführen.
            """)

        st.divider()
        st.subheader("TE 4 - Freitag (120 Min): Komplex-Training & Sicherung")
        with st.expander("🏃‍♂️ 1. Warm-up: Reaktions-Baggern & Sprints (15 Min)"):
            st.markdown("""
            **Gemeinsam:** Schnelle Sidesteps, Spielbrett stabilisieren, gefolgt von kurzen Sprints ans Netz.
            
            **Trainer-Details:** Der Wechsel aus tiefer Stabilität (Baggern) in den Vollsprint (ans Netz) trainiert die Muskelfasern, die beim Volleyball ständig gefordert sind.
            """)
        with st.expander("🎯 2. Technik: Freeball-Kill im Ablauf (35 Min)"):
            st.markdown("""
            **Gemeinsam:** Trainer schlägt Dankeball ein. Komplette Kette: Annahme -> Zuspiel -> voller Schlagangriff.
            
            **Trainer-Details:** Flüssigkeit ist der Schlüssel. Sobald der Zuspieler den Ball berührt, muss der Angreifer in den ersten Schritt (Stemmschritt) seines Anlaufs gehen. Stehen bleiben = Tempo-Verlust.
            """)
        with st.expander("🧠 3. Taktik: Die Angriffssicherung (35 Min)"):
            st.markdown("""
            **Split:** Angreifer schlägt in Doppelblock. 2-3 Mitspieler sichern tief ab und kratzen Abpraller hoch.
            
            **Trainer-Details:** Das ist die Übung, an der sich U13/U14 oft scheiden. Die nicht-angreifenden Spieler bleiben oft stehen und gucken zu. Fordere lautes 'Sicherung!'-Rufen und zwinge sie in eine extrem tiefe Haltung rund um den Angreifer.
            """)
        with st.expander("⚡ 4. Athletik: Schulter-Power & Wurfkraft (15 Min)"):
            st.markdown("""
            **Freitags-Special:** Einarmige Medizinballwürfe über das Netz + Kräftigung oberer Rücken.
            
            **Trainer-Details:** Nutze leichte Medizinbälle (1-2 kg). Es geht nicht um rohe Kraft, sondern um die Schnellkraft (Peitschenschlag) in der Schulter.
            """)
        with st.expander("🏆 5. Abschlussspiel: Wash-Game Extrem (20 Min)"):
            st.markdown("""
            **Turnier:** 2 Rallyes in Folge für Punktgewinn. Block- und Sicherungsaktionen geben Zusatzpunkte.
            
            **Trainer-Details:** Belohne schmutzige Punkte! Ein hochgekratzter Block-Abpraller, der danach im Chaos rübergespielt wird und den Punkt macht, ist wertvoller als ein sauberer Aufschlag.
            """)

    # ---------------- WOCHE 3 ----------------
    with w3:
        st.subheader("TE 5 (90 Min): Reaktion & Abwehr")
        with st.expander("🎾 1. Warm-up: 1-gegen-1 Kreatives Tennis Game (10 Min)"):
            st.markdown("""
            **Gamification:** Feld in 4-5 Schläuche teilen. 1v1. Ball darf 1x aufkommen. Schult periphere Sicht.
            
            **Trainer-Details:** Lass laufen! Greif nicht bei technischer Unsauberkeit ein. Hier geht es rein um Auge-Hand-Koordination und den Spaß, den Gegner auszutricksen.
            """)
        with st.expander("🎯 2. Technik: Schmetter-Abwehr (30 Min)"):
            st.markdown("""
            **Gemeinsam:** Spieler stehen tief auf Pos I/V. Trainer schlägt gezielt hart an. Arme ruhig halten, abprallen lassen.
            
            **Trainer-Details:** Bei harten Schlägen den Ball *nicht* schlagen. Das Spielbrett wird nur als Reflex in den Weg gehalten (Winkel zum Zentrum). Der Ball absorbiert sich selbst. Wer nach dem Ball schwingt, schießt ihn an die Decke.
            """)
        with st.expander("🧠 3. Taktik: Abwehr -> Transition (30 Min)"):
            st.markdown("""
            **Split:** Harter Angriff -> Abwehr ins Zentrum -> Notzuspiel -> Gegenangriff über außen.
            
            **Trainer-Details:** Der Umschaltmoment ist kritisch. Nach der Abwehr müssen alle Spieler sofort wieder in den Angriffsmodus (weg vom Netz, Anlauf nehmen) wechseln.
            """)
        with st.expander("🏆 4. Abschlussspiel: Abwehr-König (20 Min)"):
            st.markdown("""
            **Sonderregel:** Spektakuläre Abwehraktionen mit erfolgreichem Gegenangriff geben 2 Punkte.
            
            **Trainer-Details:** Wenn ein Spieler hechtet oder sich voll auf den Boden wirft, pfeif kurz ab und lob ihn vor der ganzen Gruppe. Das kreiert eine Mentalität, keinen Ball aufzugeben.
            """)

        st.divider()
        st.subheader("TE 6 - Freitag (120 Min): Block-Timing & Feldverteidigung")
        with st.expander("🏃‍♂️ 1. Warm-up: 1v1 Tennis Auf-/Absteiger (15 Min)"):
            st.markdown("""
            **Gemeinsam:** Kreatives Tennis-Game im Turniermodus über 15 Minuten. Sieger rückt ein Feld nach rechts.
            
            **Trainer-Details:** Ein reiner Cardio-Puls-Treiber. Halte die Standzeiten kurz, wechsle alle 2-3 Minuten die Partner durch Pfiff.
            """)
        with st.expander("🎯 2. Technik: Der 1er- und 2er-Block (35 Min)"):
            st.markdown("""
            **Gemeinsam:** Timing beim Absprung, Hände fest über das Netz schieben.
            
            **Trainer-Details:** Das Timing ist alles. Der Blocker darf erst springen, wenn der Angreifer bereits in der Luft ist (leicht verzögert). Hände bleiben starr (Handgelenke anspannen), Finger gespreizt. Nicht 'nach dem Ball schlagen' im Block.
            """)
        with st.expander("🧠 3. Taktik: Block-Abwehr-Dreieck (35 Min)"):
            st.markdown("""
            **Split:** U14 stellt Doppelblock, U13 stellt 1er-Block mit V-Abwehr dahinter. Lobs ablaufen.
            
            **Trainer-Details:** Die Abwehrspieler positionieren sich im Schatten des Blocks. Sie dürfen sich nicht hinter dem Blocker verstecken, sondern müssen die Linien abdecken, die der Block offen lässt.
            """)
        with st.expander("⚡ 4. Athletik: Sprungausdauer am Netz (15 Min)"):
            st.markdown("""
            **Freitags-Special:** Serien aus Blocksprüngen mit lateralen Sidesteps.
            
            **Trainer-Details:** Belastet die Waden stark. Achte auf weiche, federnde Landungen. Bei Knieproblemen von Spielern diese Übung sofort abbrechen lassen.
            """)
        with st.expander("🏆 5. Abschlussspiel: Block & Defense Match (20 Min)"):
            st.markdown("""
            **Modus:** 3v3/4v4. Kill-Blocks zählen doppelt.
            
            **Trainer-Details:** Fordere von der U13, dass sie den Block als echtes Mittel ansehen. Wenn ein Kind den Ball sauber blockt, entsteht enormes Selbstvertrauen.
            """)

    # ---------------- WOCHE 4 ----------------
    with w4:
        st.subheader("TE 7 (90 Min): Entscheidungsfindung")
        with st.expander("🏃‍♂️ 1. Warm-up: 1v1 Tennis Game (10 Min)"):
            st.markdown("""
            **Gemeinsam:** Schnelles Warm-up mit vollem Körpereinsatz im 1-gegen-1.
            
            **Trainer-Details:** Gleiches Konzept wie Woche 3, um die Gelenke und Reaktionen schnell hochzufahren.
            """)
        with st.expander("🎯 2. Technik: Hit or Lob Präzision (30 Min)"):
            st.markdown("""
            **Gemeinsam:** Angreifer entscheidet in der Luft: Harter Schlag oder gezielter Tip über den Block.
            
            **Trainer-Details:** Achte auf die Körperhaltung des Angreifers. Er darf den Lob nicht durch eine andere Absprunghaltung verraten. Der Anlauf muss für Lob und harten Schlag völlig identisch aussehen.
            """)
        with st.expander("🧠 3. Taktik: Systemprüfung unter Druck (30 Min)"):
            st.markdown("""
            **Split:** Trainer serviert variabel. Teams müssen Annahme, Zuspiel und Angriff fehlerfrei durchbringen.
            
            **Trainer-Details:** Wenn die Teams zu sicher werden, erhöhe als Trainer massiv den Druck (Aufschlag-Geschwindigkeit). Produziere bewusst Chaos-Bälle, um die Anpassung zu testen.
            """)
        with st.expander("🏆 4. Abschlussspiel: TuB Bocholt Liga (20 Min)"):
            st.markdown("""
            **Turnier:** Reiner Wettkampf 3v3/4v4.
            
            **Trainer-Details:** Mache die Halle heiß für das Final-Wochenende!
            """)

        st.divider()
        st.subheader("TE 8 - Freitag (120 Min): Das große Finale")
        with st.expander("🏃‍♂️ 1. Warm-up: Pre-Game Routine & Einschlagen (15 Min)"):
            st.markdown("""
            **Gemeinsam:** Offizieller Spieltags-Ablauf: Paare einspielen, Angriffsschläge am Netz.
            
            **Trainer-Details:** Lass die Kapitäne das Einspielen komplett selbst leiten. Du stehst nur da und beobachtest das Aufwärmverhalten (Team-Spirit).
            """)
        with st.expander("🎯 2. Technik: Nervenstarker Aufschlag (35 Min)"):
            st.markdown("""
            **Drucksituation:** '14:14'. 5 harte Aufschläge fehlerfrei ins Zielfeld platzieren.
            
            **Trainer-Details:** Baue künstlichen Druck auf (z.B. Trainer pfeift schrill, Nebengeräusche, enge Vorgaben). Wer verschlägt, muss 5 Strecksprünge machen und von vorne anfangen.
            """)
        with st.expander("🧠 3. Taktik: Match-Taktik & Coaching (35 Min)"):
            st.markdown("""
            **Split:** Teams analysieren gegnerische Lücken selbstständig und passen Angriffsziele an.
            
            **Trainer-Details:** Hol die Teams in den Kreis und frage: 'Wo steht die U13 am schwächsten? Wer blockt nicht?' Sie müssen lernen, das Spiel analytisch zu lesen, statt nur blind mitzuspielen.
            """)
        with st.expander("⚡ 4. Athletik: Final-Drill & Mobilisation (15 Min)"):
            st.markdown("""
            **Freitags-Special:** Schnelligkeits-Parcours + Dehnen.
            
            **Trainer-Details:** Fokus liegt auf Cool-down nach einer sehr intensiven Trainingswoche, um die Muskelspannung für das Wochenende abzubauen.
            """)
        with st.expander("🏆 5. Abschlussspiel: TuB Bocholt Meisterschaft (20 Min)"):
            st.markdown("""
            **Das große Finale:** 2 Gewinnsätze bis 15 Punkte. Profi-Schiedsrichterregeln.
            
            **Trainer-Details:** Zelebriere dieses Spiel! Lass Punkte von den Auswechselspielern notieren, pfeife sauber und ehre am Ende das Gewinner-Team. Das schweißt die Truppe enorm zusammen.
            """)

# ---------------------------------------------------------
# MONAT 3: Out-of-System & Match-Speed
# ---------------------------------------------------------
elif monat == "Monat 3: Out-of-System & Match-Speed":
    st.header("Monat 3: Lösungen unter Stress")
    
    w1, w2, w3, w4 = st.tabs(["Woche 1", "Woche 2", "Woche 3", "Woche 4"])
    
    # ---------------- WOCHE 1 ----------------
    with w1:
        st.subheader("TE 1 (90 Min): Chaos-Management")
        with st.expander("🏃‍♂️ 1. Warm-up: Blickkontrolle (10 Min)"):
            st.markdown("""
            **Gemeinsam:** Paarweises Baggern. A hält vor Ballkontakt Finger hoch, B muss rufen wie viele.
            
            **Trainer-Details:** Schult die periphere Sicht massiv. Kontrolliere, dass B wirklich ruft *bevor* der Ball auf seinen Armen landet. Nimmt den Tunnelblick vom Ball.
            """)
        with st.expander("🎯 2. Technik: Out-of-System Pass (30 Min)"):
            st.markdown("""
            **Gemeinsam:** Trainer wirft tief ins Hinterfeld. Steller (oder Annahme) muss hohen Not-Pass an die Antenne (Pos IV/II) spielen.
            
            **Trainer-Details:** Die Schulterachse muss zwingend zum Ziel (Antenne) zeigen. Aus dem Hinterfeld wird der Ball meist gebaggert. Der Druck kommt aus den Beinen, um die nötige Weite und Höhe zu erzielen.
            """)
        with st.expander("🧠 3. Taktik: Freeball-Kill unter Zeitdruck (30 Min)"):
            st.markdown("""
            **Split:** Trainer schlägt Dankeball ein. U14 hat exakt 3 Sekunden, U13 hat 4 Sekunden für kompletten Aufbau.
            
            **Trainer-Details:** Stoppe laut mit: 'Eins.. Zwei.. Drei!' Wenn der Ball nicht drüben ist, wird abgepfiffen. Das erzeugt Panik, die sie lernen müssen zu managen. Leichte Bälle *müssen* getötet werden.
            """)
        with st.expander("🏆 4. Abschlussspiel: Profi-Kaiserplatz (20 Min)"):
            st.markdown("""
            **Turnier:** Ball wird per Aufschlag von oben ins Spiel gebracht. Übertreten und Netzfehler konsequent abpfeifen.
            
            **Trainer-Details:** Du tolerierst keine Schlampigkeiten mehr. Wenn das Chaos-Management scheitert, ist der Punkt verloren. Härte in der Regelauslegung!
            """)

        st.divider()

        st.subheader("TE 2 - Freitag (120 Min): Not-Pässe & Physis")
        with st.expander("🏃‍♂️ 1. Warm-up: Reaktions-Chaos (15 Min)"):
            st.markdown("""
            **Gemeinsam:** 2 Bälle gleichzeitig im 3er-Team jonglieren (pritschen/baggern).
            
            **Trainer-Details:** Ohne extreme Kommunikation kracht es. Fordere lautes Sprechen und Namensnennung ('Tim, zu dir!').
            """)
        with st.expander("🎯 2. Technik: Den schlechten Pass erlaufen (35 Min)"):
            st.markdown("""
            **Gemeinsam:** Trainer wirft Bälle extrem streuend. Zuspieler muss sprinten, abstoppen (!) und den Not-Pass spielen.
            
            **Trainer-Details:** Das Abstoppen ist essenziell. Wer im Vollsprint pritscht, produziert Doppelfehler oder wirft den Ball. Rechter Fuß blockiert den Schwung, Schulter dreht ein.
            """)
        with st.expander("🧠 3. Taktik: Butterfly unter Druck (35 Min)"):
            st.markdown("""
            **Split:** Endlos-System. Team A wehrt ab und greift an. Fällt der Ball, rückt sofort das wartende Team nach.
            
            **Trainer-Details:** Achte auf die Laufwege abseits des Balles. Rotieren die Spieler schnell genug rein und raus, ohne sich im Weg zu stehen?
            """)
        with st.expander("⚡ 4. Athletik: Sprint-Ausdauer (15 Min)"):
            st.markdown("""
            **Freitags-Special:** Linien-Pendel-Sprints (Linien antippen).
            
            **Trainer-Details:** Zielt auf Erschöpfungsresistenz im 3. Satz. Achte darauf, dass die Linien wirklich mit der Hand berührt werden – kein Schummeln!
            """)
        with st.expander("🏆 5. Abschlussspiel: Out-of-System Bonus (20 Min)"):
            st.markdown("""
            **Sonderregel:** Ein Punkt, der nach einer Rettungstat (aus dem Chaos) erzielt wird, zählt doppelt.
            
            **Trainer-Details:** Loben, wenn eine völlig verunglückte Annahme doch noch im 3. Ball clever beim Gegner versenkt wird.
            """)

    # ---------------- WOCHE 2 ----------------
    with w2:
        st.subheader("TE 3 (90 Min): Scramble Offense")
        with st.expander("🏃‍♂️ 1. Warm-up: Ball-Klau im 3m-Raum (10 Min)"):
            st.markdown("""
            **Gemeinsam:** Dribbeln und anderen den Ball wegschlagen.
            
            **Trainer-Details:** Fördert Übersicht, Ballkontrolle und flinke Fußarbeit auf engem Raum.
            """)
        with st.expander("🎯 2. Technik: Angriff aus dem Hinterfeld (30 Min)"):
            st.markdown("""
            **Gemeinsam:** Wenn der Pass nicht ans Netz kommt: Angreifer drückt den Ball von der 3m-Linie lang ins gegnerische Feld.
            
            **Trainer-Details:** Wenn der Ball zu weit vom Netz weg ist, ist ein harter Schlag oft sinnlos (landet im Netz). Zeige die 'Push'-Technik: Ball tief greifen und im Bogen gezielt in die tiefen Ecken des Gegners drücken.
            """)
        with st.expander("🧠 3. Taktik: Rettungsaktion -> Angriff (30 Min)"):
            st.markdown("""
            **Split:** Annahme klebt im Netz oder fliegt Richtung Aus. Spieler kratzt ihn hoch, der 3. Ball *muss* als bewusster Lob/Schlag rüber.
            
            **Trainer-Details:** Simuliere die fiesen, halbgaren Bälle des Gegners. Die Spieler müssen lernen, dass auch aus einem kaputten System heraus noch ein taktischer Ball (z.B. tief in Ecke 1) gespielt werden kann.
            """)
        with st.expander("🏆 4. Abschlussspiel: Kein Dankeball (20 Min)"):
            st.markdown("""
            **Punkte-Regel:** Wer einen Ball 'einfach so' per Bagger rüberspielt, kassiert einen Minuspunkt. Es muss immer aufgebaut werden.
            
            **Trainer-Details:** Hält die Disziplin extrem hoch. Ein Angreifer (auch aus dem Stand gepritscht/gedrückt) ist Pflicht!
            """)

        st.divider()

        st.subheader("TE 4 - Freitag (120 Min): Fehlerkompensation & Rumpf")
        with st.expander("🏃‍♂️ 1. Warm-up: Koordinations-Sprints (15 Min)"):
            st.markdown("""
            **Gemeinsam:** Sprints aus dem Sitzen, Liegen und Kniestand auf Kommando.
            
            **Trainer-Details:** Fordert maximale Explosivkraft aus ungewohnten Positionen, die in der Abwehr oft vorkommen.
            """)
        with st.expander("🎯 2. Technik: Tip/Lob aus der Not (35 Min)"):
            st.markdown("""
            **Gemeinsam:** Pass kommt zu nah ans Netz (Block wartet). Angreifer muss abspringen und Ball clever ins Zentrum tippen.
            
            **Trainer-Details:** Wenn der Pass zu nah am Netz ist, führt ein Vollschlag oft zum Block-Abpraller ins eigene Gesicht. Zeige, wie man den Ball in der Luft sanft abfedert und am Block vorbeilegt.
            """)
        with st.expander("🧠 3. Taktik: Sicherung bei schlechten Pässen (35 Min)"):
            st.markdown("""
            **Split:** Pass ist unpräzise. Die Mannschaft muss sofort Richtung Angreifer rücken, um abzusichern.
            
            **Trainer-Details:** Wenn das System wackelt (Out-of-System), wird der Angreifer oft allein gelassen. Zwinge die Mitspieler, sich schützend tief um ihn zu postieren, um Block-Abpraller zu retten.
            """)
        with st.expander("⚡ 4. Athletik: Rumpf für die Luftkontrolle (15 Min)"):
            st.markdown("""
            **Freitags-Special:** Bauchmuskel-Zirkel und Rückenstrecker (Supermans) für Körperkontrolle in der Luft.
            
            **Trainer-Details:** Bei den Rückenstreckern auf langsame, kontrollierte Bewegungen achten. Verhindert Rückenschmerzen beim Angreifen.
            """)
        with st.expander("🏆 5. Abschlussspiel: Wash-Game Extrem (20 Min)"):
            st.markdown("""
            **Turnier:** 3 Rallyes am Stück gewinnen für einen großen Punkt. Absolute Nervenprobe.
            
            **Trainer-Details:** Das erfordert brutale Konstanz. Ermutige die Teams, zwischen den Rallyes durchzuatmen und sich neu zu fokussieren.
            """)

    # ---------------- WOCHE 3 ----------------
    with w3:
        st.subheader("TE 5 (90 Min): High-Speed Transition")
        with st.expander("🎾 1. Warm-up: Volley-Tennis (10 Min)"):
            st.markdown("""
            **Gemeinsam:** 1v1 Chaos-Tennis. 1x Aufkommen erlaubt, alle Körperteile dürfen benutzt werden.
            
            **Trainer-Details:** Mach Musik an, lass sie auspowern. Perfektes Mentaltraining nach einem harten Schultag.
            """)
        with st.expander("🎯 2. Technik: Abwehr -> Sofort-Angriff (30 Min)"):
            st.markdown("""
            **Gemeinsam:** Spieler wehrt harten Ball ab, macht sofort (!) den 3er-Rhythmus und greift den gestellten Notpass an.
            
            **Trainer-Details:** Das ist physisch extrem anstrengend. Beobachte den Übergang: Aus der Hocke der Abwehr sofort aufrichten, nach hinten weg vom Netz lösen, um Anlauf nehmen zu können.
            """)
        with st.expander("🧠 3. Taktik: Dauerfeuer (30 Min)"):
            st.markdown("""
            **Split:** Trainer wirft 5 Bälle pro Team in 10 Sekunden ein.
            
            **Trainer-Details:** Bringe sie an die Kotzgrenze. Sofortiges Reagieren, Abwehren und Umschalten. Das Gehirn darf nicht abschalten.
            """)
        with st.expander("🏆 4. Abschlussspiel: Speed-Turnier (20 Min)"):
            st.markdown("""
            **Modus:** 3v3 / 4v4. Ball tot = Trainer wirft in Sekunde 1 den nächsten Ball ein.
            
            **Trainer-Details:** Halte den Korb Bälle bereit. Wer jubelt oder sich ärgert, hat schon den nächsten Ball im Gesicht. Extrem hohe Ballberührungsdichte!
            """)

        st.divider()

        st.subheader("TE 6 - Freitag (120 Min): Wettkampfhärte & Beine")
        with st.expander("🏃‍♂️ 1. Warm-up: 1v1 Auf-/Absteiger (15 Min)"):
            st.markdown("""
            **Gemeinsam:** Volley-Tennis im Turniermodus.
            
            **Trainer-Details:** Schnelle Auf-/Abstiege halten den Wettkampfgedanken frisch.
            """)
        with st.expander("🎯 2. Technik: Aufschlagdruck vs. Transition (35 Min)"):
            st.markdown("""
            **Gemeinsam:** U14 feuert Aufschläge auf U13. U13 muss annehmen, aufbauen und sofort auf erneute Abwehraktion umschalten.
            
            **Trainer-Details:** Eine Endlos-Schleife der Härte. Achte darauf, dass die Annahme-Technik nicht durch Müdigkeit schlampig wird (Beine zu steif).
            """)
        with st.expander("🧠 3. Taktik: Rallye aufrechterhalten (35 Min)"):
            st.markdown("""
            **Split:** Fokus liegt darauf, den Ball unter allen Umständen im Spiel zu halten. Lobs, Blocksicherung und Hechtbagger.
            
            **Trainer-Details:** Der Trainer (Du) belohnst nur Ballwechsel, die über 4 Netzüberquerungen dauern. Bring Geduld ins Spiel der Jugendlichen.
            """)
        with st.expander("⚡ 4. Athletik: Schnelle Füße (15 Min)"):
            st.markdown("""
            **Freitags-Special:** Skippings, High-Knees und kurze Antritt-Sprints am Netz.
            
            **Trainer-Details:** Letzter athletischer Reiz für die Beine vor dem Abschluss-Turnier. Achte auf sauberen Armeinsatz beim Laufen!
            """)
        with st.expander("🏆 5. Abschlussspiel: Transition-König (20 Min)"):
            st.markdown("""
            **Modus:** Punkt zählt erst, wenn der Ball mindestens 3x (pro Seite) über das Netz ging.
            
            **Trainer-Details:** Verhindert dumme Fehler im Aufschlag oder ersten Angriff und erzwingt lange, intensive Rallyes.
            """)

    # ---------------- WOCHE 4 ----------------
    with w4:
        st.subheader("TE 7 (90 Min): Match-Day Vorbereitung")
        with st.expander("🏃‍♂️ 1. Warm-up: Pre-Game Routine (10 Min)"):
            st.markdown("""
            **Gemeinsam:** Komplettes offizielles Einschlagen (Paarweise -> Netz -> Aufschlag).
            
            **Trainer-Details:** Der Fokus liegt auf der Routine. Lass die Kinder den Ablauf einer echten Spieltagsvorbereitung selbstständig leiten.
            """)
        with st.expander("🎯 2. Technik: Der sichere Not-Aufschlag (30 Min)"):
            st.markdown("""
            **Gemeinsam:** Wenn die Luft raus ist: Sicherer Aufschlag von unten oder leichter Float, der zu 100% ins Feld muss.
            
            **Trainer-Details:** Zeige, wie man das Risiko komplett rausnimmt. Konzentrierter Anwurf, ruhiger Arm, Mitte des gegnerischen Feldes anvisieren (größte Fläche).
            """)
        with st.expander("🧠 3. Taktik: Abstimmung U13/U14 Mix (30 Min)"):
            st.markdown("""
            **Split:** Gemischte Teams. Wer deckt welche Räume? Absprachen für das Abschluss-Turnier treffen.
            
            **Trainer-Details:** Lass die Teams ihre eigene Taktik besprechen (Wo steht der Zuspieler? Wer blockt?). Das schult das Spielverständnis enorm.
            """)
        with st.expander("🏆 4. Abschlussspiel: Liga Hinrunde (20 Min)"):
            st.markdown("""
            **Turnier:** Start des großen Monats-Turniers. Jeder gegen Jeden. Punkte notieren!
            
            **Trainer-Details:** Führe eine echte Tabelle (Whiteboard/Zettel). Das motiviert für den Freitag!
            """)

        st.divider()

        st.subheader("TE 8 - Freitag (120 Min): Das Saison-Finale")
        with st.expander("🏃‍♂️ 1. Warm-up: Turnier-Warm-up (15 Min)"):
            st.markdown("""
            **Gemeinsam:** Fokus und Konzentration. Dynamisches Einspielen.
            
            **Trainer-Details:** Achte auf die Körperspannung. Keine lockeren Faxen am Netz, volle Spieltags-Mentalität.
            """)
        with st.expander("🎯 2. Technik: Feinschliff & Duelle (35 Min)"):
            st.markdown("""
            **Gemeinsam:** Angreifer gegen Blockspieler. Aufschläger gegen Annahmeriegel. Direkte Duelle.
            
            **Trainer-Details:** Korrigiere nur noch minimale Details. Es geht hier darum, den Spielern Selbstvertrauen in ihre Waffen zu geben. Lobe gute Aktionen laut!
            """)
        with st.expander("🧠 3. Taktik: Timeout-Coaching (35 Min)"):
            st.markdown("""
            **Split:** Teams simulieren Spielstände. Sie nehmen selbst Timeouts und suchen taktische Lösungen.
            
            **Trainer-Details:** Misch dich nicht ins Timeout ein. Hör nur zu. Lerne, wie deine Spieler miteinander kommunizieren und ob sie die Probleme (z.B. 'wir decken den Longline nicht') selbst erkennen.
            """)
        with st.expander("⚡ 4. Athletik: Explosivität & Cool-down (15 Min)"):
            st.markdown("""
            **Freitags-Special:** Letzte kurze Sprintserie, danach 10 Minuten ausgiebiges gemeinsames Dehnen.
            
            **Trainer-Details:** Das Dehnen bringt den Kopf runter. Lass die Spieler das Dehnen abwechselnd anleiten.
            """)
        with st.expander("🏆 5. Abschlussspiel: Liga Finale (20 Min)"):
            st.markdown("""
            **Das große Finale:** Die Rückrunde. 2 Gewinnsätze, volle Regeln, absolute Wettkampfbedingungen.
            
            **Trainer-Details:** Kröne den Monats-Sieger! Überreichung von (imaginären oder echten) Schoko-Medaillen. Du agierst als Schiedsrichter und zelebrierst das Spiel.
            """)

# ---------------------------------------------------------
# SYSTEM-SPEZIAL
# ---------------------------------------------------------
elif monat == "System-Spezial: 3v3 meets 4v4":
    st.header("System-Spezial: Transition & Kognition")
    st.success("Tipp: Nutze diese Übungen für gezieltes Kleingruppentraining.")
    
    with st.expander("⏱️ 1. Der Transition-Läufer (U13 & U14) (15 Min)"):
        st.markdown("""
        **Aus der Abwehr ins Zuspiel:** Trainer greift auf Zuspieler an. Dieser wehrt ab, Mitspieler übernimmt Not-Zuspiel.
        
        **Trainer-Details:** Zwingt den Zuspieler, in der Abwehr zu arbeiten, anstatt nur aufs Netz zu laufen.
        """)
    with st.expander("👀 2. Das Scanner-Zuspiel (20 Min)"):
        st.markdown("""
        **Block lesen:** Trainer hebt linke/rechte Hand. Zuspieler pritscht dorthin, wo die Hand *unten* ist.
        
        **Trainer-Details:** Schult periphere Sicht. Der Zuspieler darf den Ball nur an den Angreifer geben, der keinen gegnerischen (Trainer-)Block vor sich hat.
        """)
    with st.expander("🏆 3. Spielform: Der Libero-Joker (20 Min)"):
        st.markdown("""
        **3v3 mit Abwehr-Chef:** Ein U14-Spieler sichert hinten als Libero ab und rettet weite Bälle für die U13.
        
        **Trainer-Details:** Großartige Übung, um die Großen (U14) in die Verantwortung für die Abwehr zu nehmen, während die U13 vorne ungestört das System aufbauen kann.
        """)
