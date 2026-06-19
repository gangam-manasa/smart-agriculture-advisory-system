import streamlit as st

# ===== Page-specific styling =====
st.markdown("""
<style>

.hero-banner {
    background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 50%, #66bb6a 100%);
    border-radius: 18px;
    padding: 36px 30px;
    text-align: center;
    color: white;
    margin-bottom: 26px;
    box-shadow: 0 8px 24px rgba(27, 94, 32, 0.25);
}

.hero-banner h1 {
    color: white !important;
    font-size: 2.4rem;
    margin-bottom: 6px;
}

.hero-banner p {
    color: #e8f5e9;
    font-size: 1.05rem;
    margin: 0;
}

.feature-card {
    background: white;
    border-radius: 14px;
    padding: 22px 18px;
    text-align: center;
    border: 1px solid #e0f2e1;
    box-shadow: 0 3px 10px rgba(0,0,0,0.05);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    height: 100%;
}

.feature-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 10px 22px rgba(27, 94, 32, 0.18);
}

.feature-card .emoji {
    font-size: 2.2rem;
    margin-bottom: 8px;
    display: block;
}

.feature-card h4 {
    color: #1b5e20;
    margin-bottom: 6px;
}

.feature-card p {
    color: #555;
    font-size: 0.88rem;
    margin: 0;
}

.stat-pill {
    background: #f1f8e9;
    border-radius: 12px;
    padding: 16px 10px;
    text-align: center;
    border: 1px solid #c8e6c9;
}

.stat-pill .num {
    font-size: 1.6rem;
    font-weight: 800;
    color: #1b5e20;
}

.stat-pill .label {
    font-size: 0.78rem;
    color: #444;
}

.dev-card {
    background: linear-gradient(135deg, #f1f8e9, #ffffff);
    border-radius: 16px;
    padding: 24px;
    border: 1px solid #c8e6c9;
    display: flex;
    align-items: center;
    gap: 18px;
}

.dev-avatar {
    min-width: 64px;
    height: 64px;
    border-radius: 50%;
    background: linear-gradient(135deg, #2e7d32, #66bb6a);
    color: white;
    font-weight: 800;
    font-size: 1.3rem;
    display: flex;
    align-items: center;
    justify-content: center;
}

.dev-info h4 {
    margin: 0;
    color: #1b5e20;
}

.dev-info p {
    margin: 2px 0 0 0;
    color: #555;
    font-size: 0.88rem;
}

</style>
""", unsafe_allow_html=True)

# ===== Hero Banner =====
st.markdown("""
<div class="hero-banner">
    <h1>🌱 Smart Agriculture Advisory System</h1>
    <p>AI-Powered Weather Analytics &amp; Irrigation Recommendation Platform</p>
</div>
""", unsafe_allow_html=True)

# ===== Hero Image =====
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    st.image("static/images/hero_image.png", width=800)

st.markdown("<br>", unsafe_allow_html=True)

# ===== Stats strip =====
s1, s2, s3, s4 = st.columns(4)

stat_data = [
    ("4", "Smart Modules"),
    ("Real-Time", "Weather Analysis"),
    ("PDF", "Exportable Reports"),
    ("100%", "Data-Driven Insights"),
]

for col, (num, label) in zip((s1, s2, s3, s4), stat_data):
    with col:
        st.markdown(f"""
        <div class="stat-pill">
            <div class="num">{num}</div>
            <div class="label">{label}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== Feature Cards =====
st.markdown("### 🚜 What This Platform Offers")
st.write("")

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""
    <div class="feature-card">
        <span class="emoji">💧</span>
        <h4>Irrigation Recommendation</h4>
        <p>Know exactly when your field needs water based on live conditions.</p>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="feature-card">
        <span class="emoji">🌱</span>
        <h4>Crop Health & Stress Assessment</h4>
        <p>Detect crop stress risk early using temperature &amp; humidity patterns.</p>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="feature-card">
        <span class="emoji">☀️</span>
        <h4>Evaporation Risk</h4>
        <p>Estimate moisture loss risk to plan irrigation more efficiently.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

f4, f5 = st.columns(2)

with f4:
    st.markdown("""
    <div class="feature-card">
        <span class="emoji">🌾</span>
        <h4>Field Condition</h4>
        <p>Assess field moisture conditions using weather and rainfall data.</p>
    </div>
    """, unsafe_allow_html=True)

with f5:
    st.markdown("""
    <div class="feature-card">
        <span class="emoji">📊</span>
        <h4>Weather Analytics Dashboard</h4>
        <p>Upload sensor data and visualize trends across your entire dataset.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")

# ===== About snippet =====
st.subheader("🌾 About the Project")

st.write("""
The Smart Agriculture Advisory System is a web-based agricultural decision support
platform built using real weather station data collected during an internship at
**SBI ARISA Lab**. It combines live sensor readings with rule-based agronomic logic
to help farmers and researchers make faster, more confident decisions on irrigation,
heat stress, and water planning.
""")

st.markdown("---")

# ===== Developer Card =====
st.subheader("👩‍💻 Developed By")

st.markdown("""
<div class="dev-card">
    <div class="dev-avatar">MG</div>
    <div class="dev-info">
        <h4>Gangam Manasa</h4>
        <p>🎓 B.Tech in Computer Science and Engineering (CSE)</p>
        <p>🏢 SBI ARISA Lab</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ===== Navigation Buttons =====
b1, b2, b3 = st.columns(3)

with b1:
    if st.button("🚀 Start Analysis", use_container_width=True):
        st.switch_page("pages/AnalysisMode.py")

with b2:
    if st.button("📊 Dataset Analysis", use_container_width=True):
        st.switch_page("pages/DatasetAnalysis.py")

with b3:
    if st.button("ℹ️ About Project", use_container_width=True):
        st.switch_page("pages/About.py")

st.markdown("---")

st.success("🌱 Smart Farming Through Intelligent Weather Analytics")