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
    orga_modus = "🎪 **Großgruppe (13-16):** Volles Haus! Wir nutzen Stationen. Wartende Spieler stehen nicht rum, sondern werfen Bälle ein, fangen Pässe als Zielspieler oder machen Athletik am Spielfeldrand."

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
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): RTK Reaktions-Baggern"):
            st.markdown(f"**Orga bei {spieler} Spielern:** Paarweise. Bei ungerader Zahl eine 3er-Gruppe mit fliegendem Wechsel.")
            st.markdown("""
            **Ablauf:** Spieler A wirft seitlich. Spieler B macht schnellen Sidestep, formt das Spielbrett und baggert zurück.
            **🚀 PRO-Level:** Der Werfer wirft absichtlich extrem fies (sehr kurz oder flach), sodass der Stärkere zwingend abtauchen (Sprawl) muss.
            """)

        with st.expander("🎯 2. Technik I (15 Min): Ziel-Baggern aus dem Stand"):
            st.markdown(f"**Orga bei {spieler} Spielern:** {'Alle auf ein Ziel im fliegenden Wechsel.' if spieler <= 10 else 'Feld dritteln. Zwei Ziele aufbauen (Kästen), damit zwei Reihen gleichzeitig baggern können.'}")
            st.markdown("""
            **Ablauf:** Trainer/Zuspieler wirft Bälle zentral an. Ball im hohen Bogen auf das Ziel baggern.
            **🚀 PRO-Level:** Stärkere Spieler dürfen den Ball nicht anwerfen lassen, sondern bekommen ihn hart per Tennis-Aufschlag serviert.
            """)

        with st.expander("🎯 3. Technik II (15 Min): Bagger aus der Bewegung"):
            st.markdown("""
            **Ablauf:** Bälle in Lücken werfen. Spieler erläuft Ball, stoppt ab und spielt zum Ziel.
            **🚀 PRO-Level:** Starke Spieler starten auf dem Bauch liegend. Auf Pfiff aufstehen, sprinten und den Ball erlaufen.
            """)

        with st.expander("🧠 4. Taktik I (15 Min): Annahme-Riegel formieren"):
            st.markdown(f"**Orga bei {spieler} Spielern:** {'Zwei feste Riegel.' if spieler <= 8 else 'Wellenprinzip: Nach 3 Bällen sprintet der nächste Riegel aufs Feld.' if spieler <= 12 else 'Querfeld-Stationen. Wartende Spieler schlagen von der Seite auf.'}")
            st.markdown("""
            **Ablauf:** Trainer/Spieler werfen Bälle ein. Klare Kommunikation ('Ich!').
            **🚀 PRO-Level:** Starke Spieler müssen im 2er-Riegel das halbe Feld allein abdecken.
            """)

        with st.expander("🧠 5. Taktik II (15 Min): Pass zum Steller"):
            st.markdown("""
            **Ablauf:** Gezielter Bagger zum einlaufenden Steller (dieser fängt).
            **🚀 PRO-Level:** Starke Zuspieler fangen den Ball nicht, sondern leiten ihn direkt als sauberes Zuspiel weiter.
            """)

        with st.expander("🏆 6. Abschlussspiel (20 Min): Annahme-Bingo"):
            st.markdown(f"**Orga bei {spieler} Spielern:** {'3v3 / 4v4 Dauer-Match.' if spieler <= 8 else 'Kaiserplatz mit 3er-Teams.'}")
            st.markdown("""
            **Punkte-Regel:** Zusatzpunkt, wenn Annahme perfekt beim Zuspieler landet.
            **🚀 PRO-Level:** Für starke Spieler (U14) zählen Punkte im Angriff nur, wenn der Ball gesprungen und geschlagen wird.
            """)

        st.divider()

        st.subheader("TE 2 - Freitag (120 Min): Annahme unter Druck (Volleycorner)")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Tiefe Abwehr & Linien-Chaos"):
            st.markdown("**Ablauf:** Linienfangen mit tiefem Abwehr-Stopp auf Pfiff.\n**🚀 PRO-Level:** Fänger dürfen nur im Seitgalopp (Sidesteps) fangen.")

        with st.expander("🎯 2. Technik I (15 Min): Plattform-Entwicklung an der Wand"):
            st.markdown(f"**Orga bei {spieler} Spielern:** {'Jeder hat einen eigenen Platz an der Wand.' if spieler <= 10 else 'In Paaren arbeiten: Einer arbeitet an der Wand, der andere drückt leicht von hinten gegen die Schultern.'}")
            st.markdown("""
            **Ablauf:** Hände abknicken und mit Spannung gegen die Wand drücken. Hände langsam bis auf Brusthöhe nach unten und wieder nach oben führen.
            **Trainer-Details:** Übung ist bewusst anstrengend! Schultern zusammenpressen, Arme komplett überstrecken. Ziel: Die Körperspannung für das perfekte Spielbrett automatisieren.
            **🚀 PRO-Level:** Bewegung mit geschlossenen Augen ausführen. Fokus komplett auf isolierter Muskelspannung.
            """)

        with st.expander("🎯 3. Technik II (15 Min): Harte Bälle absorbieren"):
            st.markdown(f"**Orga bei {spieler} Spielern:** {'Endlos-Reihe.' if spieler <= 10 else 'Zwei Trainer/Aufschläger an den Netzkanten schießen diagonal ab.'}")
            st.markdown("""
            **Ablauf:** Arme hinhalten, Ball abprallen lassen (Bagger-Winkel). Gefühl aus der Wandübung direkt auf den Ball übertragen.
            **🚀 PRO-Level:** Starke Spieler stellen sich 2 Meter näher ans Netz (weniger Reaktionszeit!).
            """)

        with st.expander("🧠 4. Taktik I (15 Min): Annahme-Winkel (1-Mann-Riegel)"):
            st.markdown(f"**Orga bei {spieler} Spielern:** {'Hohe Frequenz: Jeder nimmt 3 Bälle in Folge, dann schneller Wechsel.' if spieler <= 10 else 'Zwei Felder nutzen (falls möglich) oder 2 Spieler stehen nebeneinander und werden abwechselnd angespielt.'}")
            st.markdown("""
            **Ablauf:** Ein Spieler nimmt alleine an. Aufschläge kommen von 3 Positionen (Links, Mitte, Rechts). Das kann mit 3 Aufschlägern oder einer **Ballmaschine** (wird umpositioniert) geschehen. Der Annahmespieler muss vor jedem Ball seine Plattform und seinen Körperwinkel zur Aufschlagposition ausrichten.
            **Trainer-Details:** Die äußere Schulter des Spielers muss leicht vorgeschoben werden, damit das Spielbrett immer ins Feld-Zentrum zeigt. 
            **🚀 PRO-Level:** Starke Spieler bekommen die Bälle in hoher Frequenz aus der Ballmaschine und müssen zwischen den Aufschlägen in der Mitte das Feld berühren (Beinarbeit!).
            """)

        with st.expander("🧠 5. Taktik II (15 Min): Annahme-Taktik (3er-Riegel vs. variable Aufschläge)"):
            st.markdown(f"**Orga bei {spieler} Spielern:** {'Ein 3er-Team wehrt 6 Bälle ab, dann Rotation.' if spieler <= 10 else 'Wellenprinzip: Team A nimmt 6 Bälle, Team B rückt sofort nach.'}")
            st.markdown("""
            **Ablauf:** 3er-Riegel. Insgesamt 6 Aufschläge (mit Maschine oder 3 Aufschlägern) von wechselnden Positionen (Links, Mitte, Rechts). 
            **Trainer-Details:** Fokus liegt auf der Absprache *vor* dem Aufschlag! Wenn der Aufschlag von links kommt, wer übernimmt die rechte Schnittstelle? Der Riegel muss sich als Einheit verschieben. Ohne lautes Sprechen kein Aufschlag!
            **🚀 PRO-Level:** Starke Spieler müssen denselben Riegel-Drill zu zweit (2er-Riegel) auf dem vollen Feld absolvieren.
            """)

        with st.expander("⚡ 6. Athletik (15 Min): DVV Rumpf & Puls"):
            st.markdown("""
            **Ablauf:** 3 Runden Zirkel (Plank, Ausfallschritte). Danach sofort Aufschläge.
            **🚀 PRO-Level:** Bei Planks diagonal Arm und Bein heben. 
            """)

        with st.expander("🏆 7. Abschlussspiel (20 Min): Handicap-Match"):
            st.markdown(f"**Orga bei {spieler} Spielern:** {'4v4 normal.' if spieler <= 8 else '3 Teams. A vs B, C fungiert als ständige Aufschläger von außen.'}")
            st.markdown("""
            **Ablauf:** Matchpraxis.
            **🚀 PRO-Level:** Starke Spieler dürfen *nur* ins hintere Felddrittel (Pos 1, 6, 5) angreifen, Anfänger überallhin.
            """)

    # ---------------- WOCHE 2 ----------------
    with w2:
        st.subheader("TE 3 (90 Min): Zuspieler-Integration")
        with st.expander("🏃‍♂️ 1. Warm-up (10 Min): Kognitives Chaos"):
            st.markdown("**Ablauf:** A pritscht Ball 1, B rollt Ball 2. Auf Pfiff: Sprint.\n**🚀 PRO-Level:** Statt Pritschen müssen die Starken den Ball im Bagger oben halten.")
            
        with st.expander("🎯 2. Technik I (15 Min): Zuspieler Beinarbeit"):
            st.markdown(f"**Orga bei {spieler} Spielern:** {'Fliegender Wechsel am Netz.' if spieler <= 10 else 'Ganze Netzlänge nutzen, 3 Stationen parallel aufbauen.'}")
            st.markdown("""
            **Ablauf:** Zuspieler pendelt zwischen Netz und Pos 3.
            **🚀 PRO-Level:** Starke Spieler müssen den gefangenen Ball sofort im Sprung zurückwerfen.
            """)

        with st.expander("🎯 3. Technik II (15 Min): Annahme + Zuspiel Kopplung"):
            st.markdown("""
            **Ablauf:** Annahme baggert zum Steller. Steller pritscht hoch in Korb.
            **🚀 PRO-Level:** Der Steller darf den Ball nicht fangen, sondern muss ihn über Kopf auf Pos II spielen.
            """)

        with st.expander("🧠 4. Taktik (30 Min): System-Laufwege"):
            st.markdown(f"**Orga bei {spieler} Spielern:** {'Eine Gruppe spielt endlos.' if spieler <= 8 else 'Wellenprinzip: 3 Bälle pro Team, dann Sprint raus.'}")
            st.markdown("""
            **Ablauf:** Trainer wirft ein. Zuspieler läuft ein. Komplett durchgespielt.
            **🚀 PRO-Level:** Der Trainer wirft absichtlich fiese Dankebälle ins Aus, das System muss gerettet werden.
            """)

        with st.expander("🏆 5. Abschlussspiel (20 Min): Wash-Game"):
            st.markdown("""
            **Ablauf:** 2 Rallyes in Folge gewinnen = 1 Punkt.
            **🚀 PRO-Level:** Wenn ein starker Spieler das Zuspiel übernimmt, muss der Pass zwingend im Sprung erfolgen.
            """)

        st.divider()

        st.subheader("TE 4 - Freitag (120 Min): System unter Druck")
        with st.expander("🏃‍♂️ 1. Warm-up (15 Min): Ball-Handling Staffel"):
            st.markdown("**Ablauf:** Staffel mit Ball prellen, Anwurf-Simulation am Netz.\n**🚀 PRO-Level:** Die Stärkeren müssen die Staffel rückwärts laufen.")

        with st.expander("🎯 2. Technik (15 Min): Zonen-Aufschlag"):
            st.markdown("""
            **Ablauf:** Aufschläge gezielt auf Turnmatten in Ecken.
            **🚀 PRO-Level:** Matten werden halbiert (schwierigeres Ziel).
            """)

        with st.expander("🧠 3. Taktik (30 Min): Rette das System (Out-of-System)"):
            st.markdown(f"**Orga bei {spieler} Spielern:** {'Warte-Spieler sammeln Bälle hinter dem Feld.' if spieler > 10 else 'Dauerbelastung.'}")
            st.markdown("""
            **Ablauf:** Trainer wirft Ball absichtlich ins Aus. Spieler rufen 'Hilfe' und spielen Notpass.
            **🚀 PRO-Level:** Starke Angreifer müssen den Notpass zwingend als harten Angriffsschlag lösen.
            """)

        with st.expander("⚡ 4. Athletik (20 Min): DVV Fußarbeit & Rumpf"):
            st.markdown("""
            **Ablauf:** Koordinationsleiter & Medizinball-Würfe.
            **🚀 PRO-Level:** Kontaktzeiten in der Leiter messen (Wettbewerb).
            """)

        with st.expander("🏆 5. Abschlussspiel (20 Min): System-Kaiser"):
            st.markdown("""
            **Ablauf:** Herausforderer rücken nur bei 3er-System-Aufbau vor.
            **🚀 PRO-Level:** Ein direkter Blockpunkt eines starken Spielers zählt doppelt.
            """)

    with w3:
        st.info("Woche 3 und 4 folgen der gleichen Logik mit dynamischer Orga-Anpassung und PRO-Levels.")
    with w4:
        st.success("Tipp: Nutze die PRO-Levels, um die U14 in denselben Übungen ans Limit zu bringen.")

# [Monat 2, 3 und Spezial-Tab Platzhalter]
elif monat == "Monat 2: Angriff (RTK: Anlauf-Rhythmus)":
    st.info("Die Struktur für Monat 2 skaliert ebenfalls dynamisch mit dem Slider.")
elif monat == "Monat 3: Out-of-System (RTK: Highball)":
    st.info("Die Struktur für Monat 3 skaliert ebenfalls dynamisch mit dem Slider.")
elif monat == "System-Spezial: 3v3 meets 4v4":
    st.info("Hier greifen bei >12 Spielern sofort Turniermodi (zwei kleine Felder quer).")
