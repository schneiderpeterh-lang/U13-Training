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
        st.subheader("TE 1 (90 Min): Das sichere Spielbrett")
        st.info("Training 1 ist bereits abgeschlossen. Fokus liegt auf TE 2 (Freitag).")

        st.divider()

        st.subheader("TE 2 - Freitag (120 Min): Annahme & Steller-Rotation")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Tiefe Abwehr & Linien-Chaos"):
            st.markdown("**Ablauf:** Linienfangen mit tiefem Abwehr-Stopp auf Pfiff.\n**🚀 PRO-Level:** Fänger dürfen nur im Seitgalopp (Sidesteps) fangen.")

        with st.expander("⚡ 2. Athletik (10 Min): ZNS-Aktivierung & Rumpf"):
            st.markdown("""
            **Ablauf:** Linien-Tappings für die Fußarbeit und kurze Planks (Unterarmstütz) für das Spielbrett.
            **Trainer-Details:** Fokus liegt auf Explosivität (kurze Bodenkontaktzeiten), nicht auf Erschöpfung!
            **🚀 PRO-Level:** Bei Planks diagonal Arm und Bein heben. 
            """)

        with st.expander("🎯 3. Technik I (15 Min): Plattform-Entwicklung an der Wand"):
            st.markdown(f"**Orga bei {spieler} Spielern:** {'Jeder hat einen eigenen Platz an der Wand.' if spieler <= 10 else 'In Paaren arbeiten: Einer arbeitet, der andere drückt leicht von hinten gegen die Schultern.'}")
            st.markdown("""
            **Ablauf:** Hände abknicken und mit Spannung gegen die Wand drücken. Hände langsam bis auf Brusthöhe nach unten und wieder nach oben führen.
            **Trainer-Details:** Die Spannung aus dem Athletik-Teil direkt mitnehmen. Schultern zusammenpressen, Arme komplett überstrecken.
            **🚀 PRO-Level:** Bewegung mit geschlossenen Augen ausführen.
            """)

        with st.expander("🎯 4. Technik II (15 Min): Harte Bälle absorbieren"):
            st.markdown(f"**Orga bei {spieler} Spielern:** {'Endlos-Reihe.' if spieler <= 10 else 'Zwei Trainer/Aufschläger an den Netzkanten schießen diagonal ab.'}")
            st.markdown("""
            **Ablauf:** Arme hinhalten, Ball abprallen lassen. Gefühl aus der Wandübung auf den Ball übertragen.
            **🚀 PRO-Level:** Starke Spieler stellen sich 2 Meter näher ans Netz.
            """)

        with st.expander("🧠 5. Taktik I (15 Min): Annahme-Winkel (1-Mann-Riegel)"):
            st.markdown(f"**Orga bei {spieler} Spielern:** {'Hohe Frequenz: Jeder nimmt 3 Bälle in Folge.' if spieler <= 10 else 'Zwei Felder nutzen oder 2 Spieler nebeneinander abwechselnd anspielen.'}")
            st.markdown("""
            **Ablauf:** Aufschläge von Links, Mitte, Rechts. Der Spieler muss seine Plattform und Körperwinkel ausrichten.
            **Trainer-Details:** Die äußere Schulter vorschieben, damit das Spielbrett ins Feld-Zentrum zeigt. 
            **🚀 PRO-Level:** Bälle kommen in hoher Frequenz, dazwischen die Spielfeldmitte berühren.
            """)

        with st.expander("🧠 6. Taktik II (15 Min): Annahme-Taktik (3er-Riegel)"):
            st.markdown(f"**Orga bei {spieler} Spielern:** {'Ein 3er-Team wehrt 6 Bälle ab, dann Rotation.' if spieler <= 10 else 'Wellenprinzip: Team A nimmt 6 Bälle, Team B rückt sofort nach.'}")
            st.markdown("""
            **Ablauf:** 3er-Riegel. 6 Aufschläge von wechselnden Positionen. 
            **Trainer-Details:** Fokus liegt auf der Absprache *vor* dem Aufschlag! Wer übernimmt die Schnittstelle?
            **🚀 PRO-Level:** Starke Spieler müssen denselben Drill im 2er-Riegel absolvieren.
            """)

        with st.expander("🧠 7. Taktik III (20 Min): Rotations-Karussell (Läufersystem)"):
            st.markdown(f"**Orga bei {spieler} Spielern:** {'Dauer-Laufwege mit fliegendem Wechsel auf der Steller-Position.' if spieler <= 10 else 'Team A macht 3 Rotationen, dann fliegender Wechsel mit Team B.'}")
            st.markdown("""
            **Ablauf:** 4 Spieler auf dem Feld (Zuspieler + 3er Annahmeriegel). Der Zuspieler startet nacheinander aus den Positionen I (hinten rechts), VI (hinten Mitte) und V (hinten links). Der Trainer schlägt den Ball an (Signal). Der Steller sprintet auf seine Netzposition (Schnittstelle zwischen II und III) und pritscht die Annahme zu einem Angreifer. Danach sofort Rotation zur nächsten Startposition.
            **Trainer-Details:** Der Zuspieler darf erst loslaufen, wenn der Trainer den Ball schlägt! Auf den direkten, kürzesten Weg ans Netz achten. Im Moment des Zuspiels muss er komplett abgestoppt sein und zum Ziel (Pos IV) schauen.
            **🚀 PRO-Level:** Starke Zuspieler müssen beim Einlaufen aus Pos V (dem längsten Weg) den Ball zwingend im Sprung zuspielen.
            """)

        with st.expander("🏆 8. Abschlussspiel (20 Min): Handicap-Match (Läufer-Fokus)"):
            st.markdown(f"**Orga bei {spieler} Spielern:** {'4v4 normal.' if spieler <= 8 else '3 Teams. A vs B, C fungiert als Aufschläger.'}")
            st.markdown("""
            **Ablauf:** Matchpraxis. Das Läufersystem wird nun im Spiel angewendet.
            **🚀 PRO-Level:** Punkte zählen doppelt, wenn der Steller aus einer Hinterfeld-Position eingelaufen ist und der Angriff direkt zum Punkt führt (sauberer Systemaufbau).
            """)

    # ---------------- WOCHE 2-4 (Platzhalter) ----------------
    with w2:
        st.info("Woche 2 setzt den Fokus auf die weitere Zuspieler-Integration.")
    with w3:
        st.info("Woche 3 fokussiert sich auf Annahme-Konstanz und Rumpf.")
    with w4:
        st.info("Woche 4 bereitet auf den Match-Day vor.")

# [Monat 2, 3 und Spezial-Tab Platzhalter]
elif monat == "Monat 2: Angriff (RTK: Anlauf-Rhythmus)":
    st.info("Die Struktur für Monat 2 skaliert ebenfalls dynamisch mit dem Slider.")
elif monat == "Monat 3: Out-of-System (RTK: Highball)":
    st.info("Die Struktur für Monat 3 skaliert ebenfalls dynamisch mit dem Slider.")
elif monat == "System-Spezial: 3v3 meets 4v4":
    st.info("Hier greifen bei >12 Spielern sofort Turniermodi (zwei kleine Felder quer).")
