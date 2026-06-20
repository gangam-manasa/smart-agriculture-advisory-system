import pandas as pd
import streamlit as st

st.title("📝 Feedback & Reviews")

st.write(
    "We value your feedback! Share your experience and suggestions to help improve the platform."
)

st.link_button(
    "🌱 Submit Feedback",
    "https://forms.gle/5mkpaGqkBFJUxveg6"
)

st.markdown("---")

SHEET_ID = "1dXIQZBh4z6PUjTKyRbVTKIMG-f5iko0F-waQPCwYjsQ"

csv_url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"

try:
    df = pd.read_csv(csv_url)

    st.subheader("⭐ Community Reviews")

    st.write(f"Total Responses: {len(df)}")

    st.dataframe(df)

except Exception as e:
    st.error("Unable to load reviews.")
    st.exception(e)
