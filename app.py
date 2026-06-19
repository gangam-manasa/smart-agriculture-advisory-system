import streamlit as st
from utils import add_logo_background

st.set_page_config(
    page_title="Smart Agriculture Advisory System",
    page_icon="🌱",
    layout="wide"
)

add_logo_background()

pg = st.navigation([
    st.Page("pages/Home.py", title="Home", icon="🏠", default=True),
    st.Page("pages/AnalysisMode.py", title="Analysis Mode", icon="🚀"),
    st.Page("pages/DatasetAnalysis.py", title="Dataset Analysis", icon="📂"),
    st.Page("pages/ManualPrediction.py", title="Manual Prediction", icon="✍️"),
    st.Page("pages/About.py", title="About Project", icon="ℹ️"),
])

pg.run()