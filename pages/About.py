import streamlit as st

# ===== Page-specific styling =====
st.markdown("""
<style>

.about-banner {
    background: linear-gradient(135deg, #1b5e20 0%, #388e3c 100%);
    border-radius: 18px;
    padding: 34px 28px;
    color: white;
    text-align: center;
    margin-bottom: 24px;
    box-shadow: 0 8px 24px rgba(27, 94, 32, 0.25);
}

.about-banner h1 {
    color: white !important;
    margin-bottom: 4px;
}

.about-banner p {
    color: #e8f5e9;
    margin: 0;
}

.info-card {
    background: white;
    border-radius: 14px;
    padding: 20px 22px;
    border-left: 5px solid #2e7d32;
    box-shadow: 0 3px 10px rgba(0,0,0,0.05);
    margin-bottom: 18px;
}

.info-card h4 {
    color: #1b5e20;
    margin-top: 0;
}

.badge {
    display: inline-block;
    background: #e8f5e9;
    color: #1b5e20;
    border: 1px solid #a5d6a7;
    border-radius: 20px;
    padding: 6px 16px;
    margin: 4px 6px 4px 0;
    font-size: 0.85rem;
    font-weight: 600;
}

.dev-card {
    background: linear-gradient(135deg, #f1f8e9, #ffffff);
    border-radius: 16px;
    padding: 26px;
    border: 1px solid #c8e6c9;
    display: flex;
    align-items: center;
    gap: 20px;
}

.dev-avatar {
    min-width: 72px;
    height: 72px;
    border-radius: 50%;
    background: linear-gradient(135deg, #2e7d32, #66bb6a);
    color: white;
    font-weight: 800;
    font-size: 1.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
}

.dev-info h4 {
    margin: 0;
    color: #1b5e20;
    font-size: 1.2rem;
}

.dev-info p {
    margin: 3px 0 0 0;
    color: #555;
    font-size: 0.9rem;
}

</style>
""", unsafe_allow_html=True)

# ===== Banner =====
st.markdown("""
<div class="about-banner">
    <h1>ℹ️ About the Project</h1>
    <p>The story, the data, and the tech behind the Smart Agriculture Advisory System</p>
</div>
""", unsafe_allow_html=True)

# ===== Mission =====
st.markdown("""
<div class="info-card">
    <h4>🎯 Objective</h4>
    <p>To provide intelligent, data-backed agricultural recommendations using
    real weather station readings — helping turn raw sensor data into clear,
    actionable decisions on irrigation, crop health, and water planning.</p>
</div>
""", unsafe_allow_html=True)

# ===== What it offers =====
st.markdown("""
<div class="info-card">
    <h4>🌾 What the Platform Offers</h4>
    <p>
    💧 Irrigation Recommendation &nbsp;•&nbsp;
    🌱 Crop Health & Stress Assessment &nbsp;•&nbsp;
    🌾 Field condition &nbsp;•&nbsp;
    ☀️ Evaporation Risk Assessment &nbsp;•&nbsp;
    📊 Weather Analytics Dashboard
    </p>
</div>
""", unsafe_allow_html=True)

# ===== Tech stack =====
st.markdown("""
<div class="info-card">
    <h4>🛠️ Built With</h4>
    <span class="badge">Python</span>
    <span class="badge">Streamlit</span>
    <span class="badge">Pandas</span>
    <span class="badge">Plotly</span>
    <span class="badge">Scikit-Learn</span>
    <span class="badge">ReportLab</span>
</div>
""", unsafe_allow_html=True)

# ===== Dataset =====
st.markdown("""
<div class="info-card">
    <h4>📂 Dataset</h4>
    <p>Real weather station sensor data — capturing ambient temperature, relative humidity, rainfall, and light intensity
    readings collected during the internship.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ===== Developer Card =====
st.subheader("👩‍💻 Developed By")

st.markdown("""
<div class="dev-card">
    <div class="dev-avatar">MG</div>
    <div class="dev-info">
        <h4>Gangam Manasa</h4>
        <p>🎓 B.Tech in Computer Science and Engineering (CSE)</p>
        <p>🏢 Internship: SBI ARISA Lab</p>
    </div>
</div>
""", unsafe_allow_html=True)

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