import streamlit as st

# Seiten-Konfiguration
st.set_page_config(page_title="U13 PRO Trainingsplan", page_icon="🏐", layout="centered")

st.title("🏐 U13 PRO Trainingsplan – TuB Bocholt")
st.markdown("Für fortgeschrittene Teams (Fokus: 1 Feld, High-Speed 1:2 System, kein Fangen).")

# Navigation
monat = st.selectbox(
    "Wähle den Trainingsbereich:", 
    [
        "Monat 1: Tempo & Aufschlag von oben", 
        "Monat 2: Angriff & Sicherung", 
        "Monat 3: Out-of-System & Match-Speed",
        "Läufer-Spezial: Transition & Kognition"
    ]
)

# ---------------------------------------------------------
# MONAT 1
# ---------------------------------------------------------
if monat == "Monat 1: Tempo & Aufschlag von oben":
    st.header("Monat 1: Schnelles System & Aufschlagdruck")
    
    tab1, tab2 = st.tabs(["TE 1 (Fokus Tempo)", "TE 2 (Fokus Aufschlag)"])
    
    with tab1:
        st.subheader("Trainingseinheit 1")
        
        with st.expander("🏃‍♂️ 1. Warm-up: Kognitives Chaos (10 Min)"):
            st.markdown("""
            **Zwei-Ball-Koordination & Reaktionssprints**
            * **Organisation:** Paarweise am Netz.
            * **Ablauf:** Spieler A pritscht Ball 1 zu B, gleichzeitig rollt B Ball 2 über den Boden zu A. Dauerschleife. Auf Pfiff: Ball liegen lassen, Sprint zur Grundlinie, Sidesteps zurück.
            * **Trainer-Fokus:** Füße müssen permanent in Bewegung bleiben. Fehler bei der Koordination provozieren – das schult den Kopf!
            """)
            
        with st.expander("🎯 2. Technik: Zuspiel im Sprung & Dankeball (30 Min)"):
            st.markdown("""
            **Ziel-Pritschen in der höchsten Reichhöhe**
            * **Organisation (Wellenprinzip):** 3er-Gruppen quer über das Feld.
            * **Ablauf:** Trainer schlägt scharfe Dankebälle ein. Die Annahme baggert hart zur Pos. III. Der Zuspieler *muss* hochspringen und den Ball im Sprung pritschen.
            * **Trainer-Fokus:** Der Zuspieler darf den Ball nicht fallen lassen. Die Annahme muss flacher und schneller ans Netz kommen, keine langsamen "Mondbälle" mehr.
            """)
            
        with st.expander("🧠 3. Taktik: High-Speed 1:2 System (30 Min)"):
            st.markdown("""
            **Volley-System unter Druck**
            * **Organisation:** 3v3 auf 1 Feld. Teams rotieren rein/raus.
            * **Ablauf:** Trainer bringt den Ball per hartem Aufschlag von unten (oder leicht von oben) ins Spiel. Das Team muss das System sauber über Pos. III aufbauen. **Kein Fangen!** Der 3. Ball wird lang in die Ecken ge-lobt oder im Sprung rübergepritscht.
            * **Trainer-Fokus:** Das Tempo der Ballwechsel steigt. Der Läufer muss explosiver starten.
            """)
            
        with st.expander("🏆 4. Abschlussspiel: Wash-Game mit Minuspunkt (20 Min)"):
            st.markdown("""
            **Konsequenz bei leichten Fehlern**
            * **Organisation:** 3v3 auf Zeit.
            * **Ablauf:** Wash-Game (ein Team muss 2 Ballwechsel in Folge gewinnen für 1 großen Punkt). 
            * **Zusatzregel:** Wer den Ball beim 1. Kontakt (direkt zurück) oder als "Dankeball-Bagger" über das Netz spielt, bekommt einen Minuspunkt. Es *muss* aufgebaut werden.
            """)

    with tab2:
        st.subheader("Trainingseinheit 2")
        st.info("Fokus Aufschlag von oben: In Teil 2 (Technik) üben wir den Tennis-Aufschlag gegen die Wand oder an die Zauberschnur. Handgelenk-Klappung (Snap) betonen!")

# ---------------------------------------------------------
# MONAT 2
# ---------------------------------------------------------
elif monat == "Monat 2: Angriff & Sicherung":
    st.header("Monat 2: Harter Angriff und Angriffs-Sicherung")
    
    tab1, tab2 = st.tabs(["TE 1 (Fokus Angriffshärte)", "TE 2 (Fokus Sicherung)"])
    
    with tab1:
        st.subheader("Trainingseinheit 1")
        
        with st.expander("🏃‍♂️ 1. Warm-up: Hechten & Block-Schatten (10 Min)"):
            st.markdown("""
            **Abwehr-Dynamik**
            * **Ablauf:** Auf Pfiff des Trainers: Blocksprung am Netz, landen, sofort rückwärts ausweichen, auf den Bauch hechten (Defense-Sprawl), schnell wieder aufstehen. 
            * **Trainer-Fokus:** Aggressive, schnelle Bewegungen. Keine Angst vor dem Boden.
            """)
            
        with st.expander("🎯 2. Technik: Der Schlagangriff (30 Min)"):
            st.markdown("""
            **Armzug und Handgelenkseinsatz**
            * **Organisation:** Spieler stehen in Reihe an der 3m-Linie (Pos IV). Trainer steht auf Pos III mit Ballwagen.
            * **Ablauf:** Trainer wirft perfekten Pass. Spieler macht den 3er-Rhythmus (Links-Rechts-Links für Rechtshänder), springt ab und schlägt den Ball. 
            * **Trainer-Fokus:** Vor dem Sprung müssen beide Arme nach hinten gerissen werden. Handgelenk muss abklappen ("dem Ball einen Deckel aufsetzen").
            """)
            
        with st.expander("🧠 3. Taktik: Die Angriffssicherung (30 Min)"):
            st.markdown("""
            **Wer deckt den Angreifer?**
            * **Organisation:** 3v3, aber auf einer Seite baut das Team gezielt auf, auf der anderen stehen 2 Spieler auf einem Kasten und bilden einen starren Doppelblock.
            * **Ablauf:** Der Zuspieler pritscht auf Pos IV. Der Angreifer schlägt absichtlich in den Block. Der Zuspieler und der zweite Annahmespieler müssen tief runtergehen und den abprallenden Ball hochkratzen (Sicherung).
            * **Trainer-Fokus:** "Angreifer greift an, alle anderen sichern!" Keiner bleibt stehen und guckt zu.
            """)
            
        with st.expander("🏆 4. Abschlussspiel: Angriffs-Bingo (20 Min)"):
            st.markdown("""
            **Punkte nur bei echtem Angriff**
            * **Ablauf:** 3v3 Endlos-Turnier. 
            * **Sonderregel:** Ein Punkt für ein Team zählt nur dann, wenn der letzte Ball gesprungen und geschlagen (oder aggressiv ge-lobt) wurde. Im Stand gepritschte Bälle geben den Aufschlag ab, aber keine Punkte.
            """)

    with tab2:
        st.subheader("Trainingseinheit 2")
        st.info("Fokus auf die Sicht des Angreifers: Kann er den Block sehen und den Ball gezielt als Lob (Tip) hinter den Blockspieler legen?")

# ---------------------------------------------------------
# MONAT 3
# ---------------------------------------------------------
elif monat == "Monat 3: Out-of-System & Match-Speed":
    st.header("Monat 3: Lösungen unter Stress")
    
    tab1, tab2 = st.tabs(["TE 1 (Fokus Not-Zuspiel)", "TE 2 (Profi-Turnier)"])
    
    with tab1:
        st.subheader("Trainingseinheit 1")
        
        with st.expander("🏃‍♂️ 1. Warm-up: Periphere Sicht (10 Min)"):
            st.markdown("""
            **Blickkontrolle**
            * **Ablauf:** Paarweises Baggern. Spieler A hält vor dem Ballkontakt 1, 2 oder 3 Finger hoch. Spieler B muss rufen, wie viele Finger es waren, *bevor* er den Ball spielt.
            * **Trainer-Fokus:** Blick weg vom Ball, rein ins Feld!
            """)
            
        with st.expander("🎯 2. Technik: Das Out-of-System Zuspiel (30 Min)"):
            st.markdown("""
            **Hoher Bagger aus dem Hinterfeld**
            * **Organisation:** Trainer steht auf Pos VI und wirft Bälle tief ins Hinterfeld oder an die Seitenlinien.
            * **Ablauf:** Der Zuspieler (oder Annahmespieler, falls Läufer nicht rankommt) muss den Ball im Bagger als extrem hohen, sauberen Pass an die Antenne (Pos IV oder II) spielen.
            * **Trainer-Fokus:** Schulterachse muss zum Ziel zeigen! Aus den Beinen schieben, kein wildes Schwingen der Arme.
            """)
            
        with st.expander("🧠 3. Taktik: Freeball-Kill (< 4 Sekunden) (30 Min)"):
            st.markdown("""
            **Dankebälle sofort bestrafen**
            * **Organisation (Wellenprinzip):** 3er-Teams. Trainer schlägt ganz leichten Dankeball (Freeball) ein.
            * **Ablauf:** Das Team hat exakt 4 Sekunden Zeit, um den Ball anzunehmen, perfekt auf Pos III zu spielen und einen harten Angriffs-Schlag auszuführen. 
            * **Trainer-Fokus:** Umschalten im Kopf! Ein leichter Ball des Gegners bedeutet maximale Aggressivität im eigenen Angriff.
            """)
            
        with st.expander("🏆 4. Abschlussspiel: Profi-Kaiserplatz (20 Min)"):
            st.markdown("""
            **Vollgas 3-gegen-3**
            * **Ablauf:** Kaiserplatz, ABER der Ball wird per echtem Aufschlag von oben ins Spiel gebracht (nicht vom Trainer eingeworfen). 
            * **Regel:** Es gelten alle Profi-Regeln. Netzfehler, unsauberes Pritschen (Doppelkontakt) und Übertreten werden streng abgepfiffen.
            """)

    with tab2:
        st.subheader("Trainingseinheit 2")
        st.info("Reines 3v3 Turnier. Fokus für den Trainer: Spielt das Team in Bedrängnis clevere Bälle in die Ecken, statt blind draufzuhauen?")

# ---------------------------------------------------------
# LÄUFER-SPEZIAL (PRO-LEVEL)
# ---------------------------------------------------------
elif monat == "Läufer-Spezial: Transition & Kognition":
    st.header("Läufer-Spezial: Transition für Fortgeschrittene")
    st.success("Tipp: Der Zuspieler ist der Spielmacher. Diese Drills zwingen ihn, das gegnerische Feld zu scannen.")
    
    with st.expander("⏱️ 1. Der Transition-Läufer (15 Min)"):
        st.markdown("""
        **Fokus: Aus der Abwehr ins Zuspiel umschalten.**
        * **Organisation:** Trainer steht auf Pos IV (Gegenseite) auf einem Kasten und greift an. Läufer steht in der Abwehr auf Pos I.
        * **Ablauf:** Trainer schlägt (moderat) auf Pos I. Der Läufer muss den Ball selbst abwehren (hoch in die Feldmitte). Ein Annahmespieler springt ein und übernimmt das "Not-Zuspiel". 
        * **Trainer-Fokus:** Der Läufer lernt, dass er nicht stur einlaufen darf, wenn der Ball genau auf ihn zugeschlagen wird.
        """)

    with st.expander("👀 2. Das Scanner-Zuspiel (20 Min)"):
        st.markdown("""
        **Fokus: Zuspieler muss den Block lesen.**
        * **Organisation:** Zuspieler läuft auf Pos III ein. Auf der Gegenseite steht der Trainer und hebt entweder die linke oder rechte Hand.
        * **Ablauf:** Ball wird vom Annahmespieler zum Zuspieler gebaggert. Während der Ball in der Luft ist, muss der Zuspieler schauen, welche Hand der Trainer hebt. 
        * **Entscheidung:** Trainer hebt Hand bei Pos IV -> Zuspieler pritscht auf Pos II (und umgekehrt). Er pritscht dorthin, wo kein "Block" ist.
        """)

    with st.expander("🌪️ 3. Der Dauerläufer (20 Min)"):
        st.markdown("""
        **Fokus: Physische Härte für den Zuspieler.**
        * **Ablauf:** 1 Zuspieler, 2 Angreifer. Der Zuspieler startet auf Pos I, sprintet auf Pos III, pritscht auf Pos IV. Rennt rückwärts (!) zurück auf Pos I, sprintet wieder vor, pritscht auf Pos II. 
        * **Intensität:** 10 Pässe am Stück, danach sofort Wechsel. Brennen in den Oberschenkeln ist garantiert!
        """)

    with st.expander("🏆 4. Spielform: Der unsichtbare Zuspieler (20 Min)"):
        st.markdown("""
        **Fokus: Den Zuspieler schützen.**
        * **Ablauf:** 3v3 Turnier. Wenn das aufschlagende Team gezielt auf den Spieler auf Position I (den designierten Zuspieler) aufschlägt, gibt es bei direktem Punktgewinn (As) 3 Punkte.
        * **Aufgabe Annahme:** Die beiden Annahmespieler (Pos IV und II) müssen fast das komplette Feld in der Annahme abdecken, um ihren Zuspieler zu "verstecken", damit dieser ungestört ans Netz laufen kann.
        """)
