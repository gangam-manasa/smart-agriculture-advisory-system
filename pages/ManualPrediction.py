import streamlit as st


def irrigation(temp, hum, rain):
    if rain > 2:
        return "❌ Not Required"
    elif temp > 32 and hum < 60:
        return "✅ Required"
    return "❌ Not Required"


def heat_stress(temp, hum):
    if temp >= 38 and hum < 40:
        return "Severe"
    elif temp >= 34:
        return "High"
    elif temp >= 30:
        return "Moderate"
    return "Low"


def field_condition(humidity, rainfall):

    if rainfall > 5:
        return "Wet"

    elif rainfall > 1:
        return "Moist"

    elif humidity > 60:
        return "Normal"

    else:
        return "Dry"


def evaporation_risk(temp, hum, wind):
    wind = wind or 0.0
    if temp > 35 and hum < 50 and wind > 2:
        return "High"
    elif temp > 30:
        return "Medium"
    return "Low"


st.title("✍ Manual Prediction")
st.caption("Fields marked with * are required.")

if "form_version" not in st.session_state:
    st.session_state.form_version = 0
if "last_result" not in st.session_state:
    st.session_state.last_result = None

v = st.session_state.form_version

temperature = st.number_input(
    "🌡️ Temperature (°C) *",
    min_value=0.0, max_value=60.0,
    value=None, placeholder="Enter temperature",
    key=f"temp_{v}"
)

humidity = st.number_input(
    "💧 Humidity (%) *",
    min_value=0.0, max_value=100.0,
    value=None, placeholder="Enter humidity",
    key=f"hum_{v}"
)

rainfall = st.number_input(
    "🌧️ Rainfall (mm) *",
    min_value=0.0,
    value=None, placeholder="Enter rainfall",
    key=f"rain_{v}"
)

light_intensity = st.number_input(
    "☀️ Light Intensity (lux)",
    min_value=0.0,
    value=None, placeholder="Optional",
    key=f"light_{v}"
)

wind_speed = st.number_input(
    "💨 Wind Speed (m/s)",
    min_value=0.0,
    value=None, placeholder="Optional",
    key=f"wind_{v}"
)

wind_direction = st.number_input(
    "🧭 Wind Direction (°)",
    min_value=0.0, max_value=360.0,
    value=None, placeholder="Optional",
    key=f"wdir_{v}"
)

pressure = st.number_input(
    "🌬️ Pressure (hPa)",
    min_value=0.0,
    value=None, placeholder="Optional",
    key=f"pres_{v}"
)

if st.button("🚀 Predict", use_container_width=True):

    if temperature is None or humidity is None or rainfall is None:
        st.error("Please fill in Temperature, Humidity, and Rainfall — they're required.")
    else:
        st.session_state.last_result = {
            "irrigation": irrigation(temperature, humidity, rainfall),
            "heat_stress": heat_stress(temperature, humidity),
            "field_condition": field_condition(humidity, rainfall),
            "evaporation_risk": evaporation_risk(temperature, humidity, wind_speed),
        }
        st.session_state.form_version += 1
        st.rerun()

if st.session_state.last_result:
    r = st.session_state.last_result
    st.success(f"💧 Irrigation Recommendation: {r['irrigation']}")
    st.warning(f"🌡️ Heat Stress Level: {r['heat_stress']}")
    st.info(f"🌾  Field Condition: {r['field_condition']}")
    st.info(f"☀️ Evaporation Risk: {r['evaporation_risk']}")

st.markdown("---")

c1, c2, c3 = st.columns(3)

with c1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("pages/Home.py")

with c2:
    if st.button("🚀 Analysis Mode", use_container_width=True):
        st.switch_page("pages/AnalysisMode.py")

with c3:
    if st.button("📂 Dataset Analysis", use_container_width=True):
        st.switch_page("pages/DatasetAnalysis.py")