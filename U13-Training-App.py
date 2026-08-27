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

    # ---------------- WOCHE 3 & 4 (PLATZHALTER) ----------------
    with w3:
        st.info("Woche 3: Wird nach dem 15-Minuten-Raster für Transition und Annahme-Konstanz generiert.")
    with w4:
        st.success("Woche 4: Wird nach dem 15-Minuten-Raster für Wettkampfhärte generiert.")

# [Monat 2, 3 und Spezial-Tab bleiben wie bisher, bis sie umgewandelt werden]
elif monat == "Monat 2: Grundtechnik Angriff & Aufschlag":
    st.info("Die Struktur für Monat 2 wartet auf das 15-Minuten-Update.")
elif monat == "Monat 3: Out-of-System & Match-Speed":
    st.info("Die Struktur für Monat 3 wartet auf das 15-Minuten-Update.")
elif monat == "System-Spezial: 3v3 meets 4v4":
    st.info("System-Spezial wartet auf das 15-Minuten-Update.")
