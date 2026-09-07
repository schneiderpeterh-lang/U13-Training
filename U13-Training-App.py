import streamlit as st

# Seiten-Konfiguration
st.set_page_config(page_title="U13/U14 Trainingsplan - DVV RTK", page_icon="🏐", layout="centered")

st.title("🏐 U13/U14 PRO Plan (DVV RTK)")
st.markdown("TuB Bocholt | Differenziertes Training & Dynamische Orga")

# Navigation - Dynamik
col1, col2 = st.columns([3, 2])
with col1:
    monat = st.selectbox(
        "Wähle den Trainingsmonat:", 
        [
            "Monat 1: Annahme-Präzision (RTK: Bagger)", 
            "Monat 2: Angriff (RTK: Anlauf-Rhythmus)", 
            "Monat 3: Out-of-System (RTK: Highball)",
            "System-Spezial: 3v3 meets 4v4"
        ]
    )
with col2:
    spieler = st.slider("Spieleranzahl heute:", min_value=6, max_value=16, value=11, step=1)

# Dynamische Organisations-Logik
if spieler <= 8:
    orga_modus = "🔥 **Kleingruppe (6-8):** Extreme Ballberührungsdichte. Keine Pausen, Dauerschleifen (Butterfly-Drills)."
elif spieler <= 12:
    orga_modus = "🌊 **Standard (9-12):** Wellenprinzip. 3er/4er-Teams wechseln sich fliegend ab. Ein Team auf dem Feld, eins wartet und rotiert nach 3 Bällen ein."
else:
    orga_modus = "🎪 **Großgruppe (13-16):** Volles Haus! Wir nutzen Stationen. Wartende Spieler werfen Bälle ein oder machen Athletik."

st.success(f"Aktueller Modus für {spieler} Spieler:\n {orga_modus}")
st.divider()

# ---------------------------------------------------------
# MONAT 1: Annahme & System
# ---------------------------------------------------------
if monat == "Monat 1: Annahme-Präzision (RTK: Bagger)":
    st.header("Monat 1: Gezielte Annahme zum Steller")
    
    w1, w2, w3, w4 = st.tabs(["Woche 1", "Woche 2", "Woche 3", "Woche 4"])
    
    # ---------------- WOCHE 1 ----------------
    with w1:
        st.subheader("TE 1 (90 Min) & TE 2 (120 Min)")
        st.info("Woche 1 ist bereits vollständig implementiert.")

    # ---------------- WOCHE 2 ----------------
    with w2:
        st.subheader("TE 3 (90 Min Mittwoch): Zuspieler-Integration & Bagger-Winkel")
        with st.expander("🎾 1. Warm-up (10 Min): Baggertennis (1v1-Minifeld)"):
            st.markdown(f"**Orga bei {spieler} Spielern:** Das Feld wird in mehrere kleine Schläuche unterteilt (z.B. 3-4 Minifelder quer). Modus: Auf- und Absteiger-Turnier.")
            st.markdown("""
            **Ablauf:** 1 gegen 1 auf Mini-Feldern. Jeder Spieler hat ein eigenes kleines Feld. Der Ball darf einmal den Boden berühren (wie beim Tennis), muss dann aber über das Netz in das gegnerische Feld zurückgespielt werden (primär im Bagger).
            **Trainer-Details:** Fördert maximale Ballberührungsdichte, Beinarbeit, Schnelligkeit und Präzision unter Wettkampfdruck.
            **🚀 PRO-Level:** Starke Spieler dürfen den Ball *nicht* aufkommen lassen (Direkt-Duell Volley-Tennis) oder nur mit einer Hand retten.
            """)

        with st.expander("⚡ 2. Athletik (10 Min): ZNS-Aktivierung & Fußarbeit"):
            st.markdown("""
            **Ablauf:** Linien-Tappings (Quick Feet) und Scheren-Sprünge an der 3m-Linie.
            **Trainer-Details:** Schnelle, kurze Bodenkontaktzeiten auf dem Vorfuß. Aktivierung des Nervensystems.
            **🚀 PRO-Level:** Auf Pfiff sofort aus der schnellen Fußarbeit in die tiefe Abwehr-Haltung abtauchen.
            """)

        with st.expander("🎯 3. Technik I (15 Min): Bagger-Winkel anpassen"):
            st.markdown(f"**Orga bei {spieler} Spielern:** {'Fliegender Wechsel am Netz.' if spieler <= 10 else 'Ganze Netzlänge nutzen, parallele Kleingruppen.'}")
            st.markdown("""
            **Ablauf:** Ball selbst anwerfen und diagonal auf Position 2 baggern.
            **Trainer-Details (RTK Bagger):** Die innere Schulter muss tiefer sein, damit das Spielbrett exakt zum Ziel zeigt.
            **🚀 PRO-Level:** Der Ball wird nicht selbst angeworfen, sondern von einem Partner aus der Bewegung zugeworfen.
            """)

        with st.expander("🎯 4. Technik II (15 Min): Annahme + Zuspiel Kopplung"):
            st.markdown("""
            **Ablauf:** Annahme baggert zum Steller. Steller pritscht hoch in einen Korb oder auf Zielposition.
            **Trainer-Details:** Der Bagger muss hoch genug sein, damit der Steller in Ruhe unter den Ball treten kann.
            **🚀 PRO-Level:** Der Steller darf den Ball nicht fangen, sondern muss ihn direkt als sauberen Pass über Kopf auf Position II spielen.
            """)

        with st.expander("🧠 5. Taktik I (15 Min): System-Laufwege (Trocken)"):
            st.markdown(f"**Orga bei {spieler} Spielern:** {'Grundaufstellung auf dem Feld.' if spieler <= 8 else 'Wellenwechsel nach jeweils 3 erfolgreichen Abläufen.'}")
            st.markdown("""
            **Ablauf:** U14/U13 in Grundaufstellung. Trainer wirft Bälle hoch. Zuspieler läuft ein, fängt den Ball, alle rotieren.
            **Trainer-Details:** Positionsfehler streng abpfeifen. Erst laufen, wenn der Ball den Trainer verlässt.
            """)

        with st.expander("🏆 6. Abschlussspiel (20 Min): Wash-Game (2 Rallyes)"):
            st.markdown(f"**Orga bei {spieler} Spielern:** {'3v3 / 4v4 ohne Wechsel.' if spieler <= 8 else 'Kaiserplatz-Modus.'}")
            st.markdown("""
            **Ablauf:** 2 Rallyes in Folge gewinnen = 1 Punkt.
            **Trainer-Details:** Zweiter Ball fliegt sofort rein. Hält die Konzentration oben.
            **🚀 PRO-Level:** Wenn ein starker Spieler das Zuspiel übernimmt, muss der Pass zwingend im Sprung erfolgen.
            """)

        st.divider()

        st.subheader("TE 4 - Freitag (120 Min): RTK Athletik & System unter Druck")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Ball-Handling & Anwurf"):
            st.markdown("""
            **Ablauf:** Staffel mit Ball prellen, Anwurf-Simulation am Netz und Richtungswechseln.
            **Trainer-Details:** Ball muss vor der Schlag-Schulter angeworfen werden (Vorbereitung für Aufschlag).
            """)

        with st.expander("⚡ 2. Athletik (15 Min): DVV Fußarbeit & Rumpf"):
            st.markdown("""
            **Ablauf:** Laterale Sidesteps an den Linien & Medizinball-Würfe (seitlich).
            **Trainer-Details:** Rumpf-Rotation stärken für stabiles Baggern aus der Drehung.
            **🚀 PRO-Level:** Zusatzgewicht oder schwerere Medizinbälle nutzen.
            """)

        with st.expander("🎯 3. Technik I (15 Min): Zonen-Aufschlag"):
            st.markdown("""
            **Ablauf:** Aufschläge gezielt auf Turnmatten in Ecken.
            **Trainer-Details:** Handgelenk muss fest sein, um Druck und Genauigkeit zu erzeugen.
            **🚀 PRO-Level:** Matten werden halbiert (schwierigeres Ziel). Aufschlag muss knallhart als Float gespielt werden.
            """)

        with st.expander("🎯 4. Technik II (15 Min): Annahme-Verschiebung"):
            st.markdown(f"**Orga bei {spieler} Spielern:** {'Aufschläger-Teams wechseln sich an der Grundlinie ab.' if spieler <= 10 else 'Zwei Aufschläger schicken die Annahme variabel.'}")
            st.markdown("""
            **Ablauf:** Aufschläger wechselt permanent die Position (Mitte, Seite). Annahmeriegel muss rotieren.
            **Trainer-Details:** Den Kreuzwinkel abdecken! Das äußere Bein blockiert den Ball Richtung Aus.
            """)

        with st.expander("🧠 5. Taktik I (15 Min): Out-of-System (Trocken & Live)"):
            st.markdown("""
            **Ablauf:** Trainer wirft Ball absichtlich ins Aus. Spieler rufen 'Hilfe' und spielen Notpass ans Netz.
            **Trainer-Details:** Auditive Kommunikation (wer ruft?) und hoher Notpass (Highball-Vorbereitung).
            **🚀 PRO-Level:** Starke Angreifer müssen den Notpass zwingend als harten Angriffsschlag aus dem Hinterfeld lösen.
            """)

        with st.expander("🧠 6. Taktik II (15 Min): System-Integration"):
            st.markdown("""
            **Ablauf:** Komplex-Übung Aufschlag -> Annahme -> Zuspiel -> Angriff.
            **Trainer-Details:** Flüssigkeit im Ablauf erzwingen. Keine stehenden Spieler nach der Ballberührung.
            """)

        with st.expander("🏆 7. Abschlussspiel (20 Min): System-Kaiser"):
            st.markdown(f"**Orga bei {spieler} Spielern:** {'3v3 / 4v4 Turniermodus.' if spieler <= 8 else 'Kaiserplatz mit mehreren Teams.'}")
            st.markdown("""
            **Ablauf:** Herausforderer rücken nur bei 3er-System-Aufbau auf die Kaiserseite.
            **Trainer-Details:** Lobe auch den Versuch, wenn der finale Ball im Aus landet!
            **🚀 PRO-Level:** Ein direkter Blockpunkt eines starken Spielers zählt doppelt.
            """)

    # ---------------- WOCHE 3 & 4 ----------------
    with w3:
        st.info("Woche 3 widmet sich der Annahme-Konstanz und der Transition von der Abwehr zur Annahme.")
    with w4:
        st.info("Woche 4 schließt den Monat mit Match-Simulationen und dem großen Monatstest ab.")

# [Monat 2, 3 und Spezial-Tab Platzhalter]
elif monat == "Monat 2: Angriff (RTK: Anlauf-Rhythmus)":
    st.info("Die Struktur für Monat 2 skaliert ebenfalls dynamisch mit dem Slider.")
elif monat == "Monat 3: Out-of-System (RTK: Highball)":
    st.info("Die Struktur für Monat 3 skaliert ebenfalls dynamisch mit dem Slider.")
elif monat == "System-Spezial: 3v3 meets 4v4":
    st.info("Hier greifen bei >12 Spielern sofort Turniermodi (zwei kleine Felder quer).")
