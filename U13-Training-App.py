import streamlit as st

# Seiten-Konfiguration
st.set_page_config(page_title="U13/U14 Trainingsplan - DVV RTK", page_icon="🏐", layout="centered")

st.title("🏐 U13/U14 PRO Plan (DVV RTK)")
st.markdown("TuB Bocholt | Max. 15 Min pro Übung\n**Fokus DVV Starting Six:** Anlauf-Rhythmus, Schlagbewegung, Highball-Set, Bagger & Athletik")

# Navigation - Dynamik
col1, col2 = st.columns(2)
with col1:
    monat = st.selectbox(
        "Wähle den Trainingsmonat:", 
        [
            "Monat 1: Annahme-Präzision (RTK: Bagger & Athletik)", 
            "Monat 2: Angriff (RTK: Anlauf-Rhythmus & Schlagbewegung)", 
            "Monat 3: Out-of-System (RTK: Highball-Set & Abwehr-Bagger)",
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

    with w3:
        st.info("Das dynamische Spieler-Raster (6-8 vs. 9-12) wird analog in die Wochen 3 und 4 übernommen.")
    with w4:
        st.success("Die Teams passen sich automatisch im Abschlussspiel und Taktik-Training der Anzahl an!")
