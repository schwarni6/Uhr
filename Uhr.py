
```python
import streamlit as st
import math

st.set_page_config(
    page_title="Meine Uhr",
    page_icon="⌚",
    layout="wide"
)

st.title("⌚ Meine eigene Armbanduhr")
st.write("Gestalte deine persönliche Armbanduhr.")

# -----------------------------
# Einstellungen
# -----------------------------

st.sidebar.header("🎨 Uhr konfigurieren")

gehäuse = st.sidebar.selectbox(
    "Gehäuse",
    ["Schwarz", "Silber", "Gold", "Roségold", "Blau"]
)

zifferblatt = st.sidebar.selectbox(
    "Zifferblatt",
    ["Weiß", "Schwarz", "Blau", "Grün", "Rot"]
)

armband = st.sidebar.selectbox(
    "Armband",
    ["Schwarz", "Braun", "Blau", "Rot", "Grün"]
)

zeiger = st.sidebar.selectbox(
    "Zeiger",
    ["Weiß", "Schwarz", "Gold"]
)

größe = st.sidebar.slider(
    "Uhrengröße",
    250,
    500,
    350,
    10
)

# -----------------------------
# Farben
# -----------------------------

gehäuse_farben = {
    "Schwarz": "#222222",
    "Silber": "#BFC0C0",
    "Gold": "#D4AF37",
    "Roségold": "#B76E79",
    "Blau": "#244B7A"
}

zifferblatt_farben = {
    "Weiß": "#F5F5F5",
    "Schwarz": "#111111",
    "Blau": "#173A5E",
    "Grün": "#244D3A",
    "Rot": "#6E2424"
}

armband_farben = {
    "Schwarz": "#171717",
    "Braun": "#6B3E26",
    "Blau": "#234A78",
    "Rot": "#7A2424",
    "Grün": "#28513A"
}

zeiger_farben = {
    "Weiß": "#FFFFFF",
    "Schwarz": "#111111",
    "Gold": "#D4AF37"
}

# -----------------------------
# CSS + Uhr
# -----------------------------

gehäuse_farbe = gehäuse_farben[gehäuse]
zifferblatt_farbe = zifferblatt_farben[zifferblatt]
armband_farbe = armband_farben[armband]
zeiger_farbe = zeiger_farben[zeiger]

st.markdown(
    f"""
    <style>

    .watch-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 600px;
    }}

    .watch {{
        position: relative;
        width: {größe}px;
        height: {größe}px;
    }}

    .strap {{
        position: absolute;
        left: 35%;
        top: -35%;
        width: 30%;
        height: 170%;
        background: {armband_farbe};
        border-radius: 30px;
        z-index: 1;
    }}

    .case {{
        position: absolute;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        background: {gehäuse_farbe};
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 2;
        box-shadow:
            0 10px 30px rgba(0,0,0,0.35),
            inset 0 0 10px rgba(255,255,255,0.25);
    }}

    .dial {{
        position: relative;
        width: 88%;
        height: 88%;
        border-radius: 50%;
        background: {zifferblatt_farbe};
        border: 3px solid {gehäuse_farbe};
    }}

    .number {{
        position: absolute;
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: flex-start;
        padding-top: 5%;
        font-size: 22px;
        font-weight: bold;
        color: {zeiger_farbe};
        box-sizing: border-box;
    }}

    .n3 {{
        transform: rotate(90deg);
    }}

    .n6 {{
        transform: rotate(180deg);
    }}

    .n9 {{
        transform: rotate(270deg);
    }}

    .n3 span {{
        transform: rotate(-90deg);
    }}

    .n6 span {{
        transform: rotate(-180deg);
    }}

    .n9 span {{
        transform: rotate(-270deg);
    }}

    .hand {{
        position: absolute;
        left: 50%;
        bottom: 50%;
        transform-origin: bottom center;
        background: {zeiger_farbe};
        border-radius: 5px;
    }}

    .hour {{
        width: 7px;
        height: 28%;
        transform: translateX(-50%) rotate(135deg);
    }}

    .minute {{
        width: 5px;
        height: 38%;
        transform: translateX(-50%) rotate(45deg);
    }}

    .second {{
        width: 2px;
        height: 40%;
        background: #D33;
        transform: translateX(-50%) rotate(210deg);
    }}

    .center {{
        position: absolute;
        left: 50%;
        top: 50%;
        width: 16px;
        height: 16px;
        background: {zeiger_farbe};
        border-radius: 50%;
        transform: translate(-50%, -50%);
    }}

    </style>

    <div class="watch-container">
        <div class="watch">

            <div class="strap"></div>

            <div class="case">

                <div class="dial">

                    <div class="number">
                        <span>12</span>
                    </div>

                    <div class="number n3">
                        <span>3</span>
                    </div>

                    <div class="number n6">
                        <span>6</span>
                    </div>

                    <div class="number n9">
                        <span>9</span>
                    </div>

                    <div class="hand hour"></div>
                    <div class="hand minute"></div>
                    <div class="hand second"></div>

                    <div class="center"></div>

                </div>

            </div>

        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Zusammenfassung
# -----------------------------

st.subheader("Deine Konfiguration")

col1, col2, col3 = st.columns(3)

with col1:
    st.write(f"**Gehäuse:** {gehäuse}")
    st.write(f"**Zifferblatt:** {zifferblatt}")

with col2:
    st.write(f"**Armband:** {armband}")
    st.write(f"**Zeiger:** {zeiger}")

with col3:
    st.write(f"**Größe:** {größe}px")

st.success("Deine Uhr wurde erfolgreich konfiguriert! 🎉")
```
