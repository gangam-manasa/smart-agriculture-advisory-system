import streamlit as st
import base64


@st.cache_data
def _get_logo_base64(path: str) -> str:
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()


def add_logo_background(opacity=0.12):
    encoded = _get_logo_base64("static/images/sbi_arisa_logo.png")
    overlay = 1 - opacity

    st.markdown(
        f"""
        <style>

        [data-testid="stAppViewContainer"] {{
            background-color: #f7fff7;

            background-image:
                linear-gradient(
                    rgba(247,255,247,{overlay}),
                    rgba(247,255,247,{overlay})
                ),
                url("data:image/png;base64,{encoded}");

            background-repeat: no-repeat;
            background-position: center;
            background-size: 600px;
            background-attachment: fixed;
        }}

        [data-testid="stHeader"] {{
            background: rgba(0,0,0,0);
        }}

        h1, h2, h3 {{
            color: #1b5e20;
        }}

        @keyframes fadeInPage {{
            from {{ opacity: 0; transform: translateY(6px); }}
            to   {{ opacity: 1; transform: translateY(0); }}
        }}

        [data-testid="stAppViewContainer"] .main .block-container {{
            animation: fadeInPage 0.35s ease-out;
        }}

        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, #1b5e20 0%, #2e7d32 60%, #388e3c 100%);
            border-right: 1px solid #145a1c;
        }}

        [data-testid="stSidebar"] * {{
            color: #f1f8e9 !important;
        }}

        [data-testid="stSidebarNav"] {{
            padding-top: 10px;
        }}

        [data-testid="stSidebarNav"] a {{
            border-radius: 10px;
            margin: 3px 10px;
            padding: 10px 14px;
            transition: background-color 0.2s ease, transform 0.15s ease;
        }}

        [data-testid="stSidebarNav"] a:hover {{
            background-color: rgba(255,255,255,0.18);
            transform: translateX(2px);
        }}

        [data-testid="stSidebarNav"] a[aria-current="page"] {{
            background-color: rgba(255,255,255,0.28);
            font-weight: 700;
            border-left: 4px solid #ffeb3b;
        }}

        [data-testid="stSidebarNav"]::after {{
            content: "";
            display: block;
            margin: 10px 16px 6px 16px;
            border-bottom: 1px solid rgba(255,255,255,0.25);
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

    with st.sidebar:
        st.markdown(
            f"""
            <div style="text-align:center; padding-top: 8px;">
                <img src="data:image/png;base64,{encoded}"
                     style="width:70px; border-radius:8px; margin-bottom:6px;" />
                <div style="font-size:15px; font-weight:700; color:#f1f8e9;">
                    🌱 Smart Agriculture
                </div>
                <div style="font-size:12px; opacity:0.9; color:#e8f5e9; margin-top:2px;">
                    Developed by Gangam Manasa
                </div>
                <div style="font-size:11px; opacity:0.75; color:#e8f5e9; margin-top:2px;">
                    SBI ARISA Lab
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )