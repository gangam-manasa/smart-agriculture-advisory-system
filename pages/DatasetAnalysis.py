import io

import pandas as pd
import plotly.express as px
import streamlit as st
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
)

st.title("Weather Station Data Analysis")

uploaded_file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx"]
)

LOGO_PATH = "static/images/sbi_arisa_logo.png"


def build_pdf_report(stats: dict, figs: dict) -> bytes:
    buffer = io.BytesIO()
    page_width, page_height = letter

    doc = SimpleDocTemplate(
        buffer, pagesize=letter,
        topMargin=1.0 * inch, bottomMargin=0.7 * inch,
        leftMargin=0.6 * inch, rightMargin=0.6 * inch
    )

    def draw_page_decorations(canvas, doc_):
        canvas.saveState()

        try:
            canvas.setFillAlpha(0.07)
            wm_size = 4.5 * inch
            canvas.drawImage(
                LOGO_PATH,
                (page_width - wm_size) / 2,
                (page_height - wm_size) / 2,
                width=wm_size, height=wm_size,
                mask="auto", preserveAspectRatio=True
            )
        except Exception:
            pass
        canvas.setFillAlpha(1)

        header_y = page_height - 0.55 * inch

        canvas.setFont("Helvetica-Bold", 9)
        canvas.setFillColor(colors.HexColor("#1b5e20"))
        canvas.drawString(0.6 * inch, header_y, "SBI ARISA Lab")

        canvas.setFont("Helvetica", 9)
        canvas.setFillColor(colors.HexColor("#333333"))
        canvas.drawRightString(page_width - 0.6 * inch, header_y, "Developed by Gangam Manasa")

        canvas.setStrokeColor(colors.HexColor("#c8e6c9"))
        canvas.setLineWidth(0.7)
        canvas.line(0.6 * inch, header_y - 6, page_width - 0.6 * inch, header_y - 6)

        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#888888"))
        canvas.drawCentredString(page_width / 2, 0.4 * inch, f"Page {doc_.page}")

        canvas.restoreState()

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "ReportTitle", parent=styles["Title"],
        textColor=colors.HexColor("#1b5e20"), fontSize=20
    )
    section_style = ParagraphStyle(
        "Section", parent=styles["Heading2"],
        textColor=colors.HexColor("#1b5e20"), spaceBefore=14
    )

    story = []

    story.append(Paragraph("🌱 Smart Agriculture Advisory System", title_style))
    story.append(Paragraph("Uploaded DataSet Statistics Report", styles["Heading3"]))
    story.append(Spacer(1, 16))

    story.append(Paragraph("Summary Statistics", section_style))
    table_data = [["Metric", "Value"]] + [[k, str(v)] for k, v in stats.items()]

    stats_table = Table(table_data, colWidths=[3 * inch, 2.5 * inch])
    stats_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2e7d32")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#c8e6c9")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f1f8e9")]),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(stats_table)
    story.append(Spacer(1, 20))

    story.append(Paragraph("Trend Charts", section_style))

    for title, fig in figs.items():
        story.append(Paragraph(title, styles["Heading4"]))
        try:
            png_bytes = fig.to_image(format="png", width=900, height=420, scale=2)
            img = Image(io.BytesIO(png_bytes), width=6.0 * inch, height=2.8 * inch)
            story.append(img)
        except Exception:
            story.append(Paragraph(
                "(Chart image unavailable — kaleido package not installed)",
                styles["Italic"]
            ))
        story.append(Spacer(1, 14))

    doc.build(story, onFirstPage=draw_page_decorations, onLaterPages=draw_page_decorations)
    return buffer.getvalue()


if uploaded_file is not None:

    df = pd.read_excel(uploaded_file)

    st.success("File Uploaded Successfully ✅")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Summary Statistics")

    avg_temp = df["Ambient Temperature (°C)"].mean()
    avg_humidity = df["Relative Humidity (%)"].mean()
    total_rainfall = df["Rainfall (mm)"].sum()
    avg_light = df["Light Intensity (lux)"].mean()

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Records", len(df))
    col2.metric("Avg Temp", f"{avg_temp:.2f}°C")
    col3.metric("Avg Humidity", f"{avg_humidity:.2f}%")
    col4.metric("Rainfall", f"{total_rainfall:.2f} mm")
    col5.metric("Avg Light", f"{avg_light:.2f} lux")

    st.subheader("Temperature Trend")
    temp_fig = px.line(df.head(500), y="Ambient Temperature (°C)")
    st.plotly_chart(temp_fig, use_container_width=True)

    st.subheader("Humidity Trend")
    humidity_fig = px.line(df.head(500), y="Relative Humidity (%)")
    st.plotly_chart(humidity_fig, use_container_width=True)

    st.subheader("Rainfall Trend")
    rainfall_fig = px.line(df.head(500), y="Rainfall (mm)")
    st.plotly_chart(rainfall_fig, use_container_width=True)

    st.subheader("Light Intensity Trend")
    light_fig = px.line(df.head(500), y="Light Intensity (lux)")
    st.plotly_chart(light_fig, use_container_width=True)

    st.markdown("---")
    st.subheader("📥 Download Report")

    stats = {
        "Total Records": len(df),
        "Average Temperature (°C)": round(avg_temp, 2),
        "Average Humidity (%)": round(avg_humidity, 2),
        "Total Rainfall (mm)": round(total_rainfall, 2),
        "Average Light Intensity (lux)": round(avg_light, 2),
    }

    figs = {
        "Temperature Trend": temp_fig,
        "Humidity Trend": humidity_fig,
        "Rainfall Trend": rainfall_fig,
        "Light Intensity Trend": light_fig,
    }

    if st.button("🛠️ Prepare PDF Report", use_container_width=True):
        with st.spinner("Preparing your PDF report..."):
            st.session_state.stats_pdf = build_pdf_report(stats, figs)
        st.success("Report ready! Use the button below to download.")

    if "stats_pdf" in st.session_state:
        st.download_button(
            label="⬇️ Download PDF Report",
            data=st.session_state.stats_pdf,
            file_name="agri_statistics_report.pdf",
            mime="application/pdf",
            use_container_width=True
        )

st.markdown("---")

c1, c2, c3 = st.columns(3)

with c1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("pages/Home.py")

with c2:
    if st.button("🚀 Analysis Mode", use_container_width=True):
        st.switch_page("pages/AnalysisMode.py")

with c3:
    if st.button("✍ Manual Prediction", use_container_width=True):
        st.switch_page("pages/ManualPrediction.py")
