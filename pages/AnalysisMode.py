import streamlit as st

st.title("🚀 Analysis Mode")

st.write(
    "Choose how you want to analyze the data."
)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.success("""
# ✍ Manual Prediction

Enter weather parameters manually and receive agricultural recommendations.
""")

    if st.button(
        "Go to Manual Prediction",
        use_container_width=True
    ):
        st.switch_page("pages/ManualPrediction.py")

with col2:
    st.info("""
# 📂 Dataset Analysis

Upload .xlsv Data File and visualize trends and analytics.
""")

    if st.button(
        "Go to Dataset Analysis",
        use_container_width=True
    ):
        st.switch_page("pages/DatasetAnalysis.py")

st.markdown("---")

col3, col4 = st.columns(2)

with col3:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("pages/Home.py")

with col4:
    if st.button("About Project", use_container_width=True):
        st.switch_page("pages/About.py")