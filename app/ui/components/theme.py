"""
SixStage Product Dashboard Theme

Applies the same dark gradient brand background used on the
marketing site (ui/website/theme.py) to the internal product
dashboard, plus overrides for Streamlit's native widgets (metrics,
inputs, sidebar, buttons, dividers) so they're legible and consistent
on a dark background instead of the framework's default light theme.

Deliberately self-contained (no import from ui/website) since the
two apps can be launched independently and shouldn't depend on each
other's path setup.
"""

import streamlit as st


def apply_dashboard_theme():

    st.markdown(
        """
        <style>
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #0f172a 0%, #312e81 45%, #2563eb 100%);
        }
        [data-testid="stHeader"] {
            background: transparent;
        }
        [data-testid="stSidebar"] {
            background: rgba(15, 23, 42, 0.55);
            border-right: 1px solid rgba(255,255,255,0.08);
        }
        .stApp, .stApp p, .stApp span, .stApp label, .stApp li,
        .stMarkdown, [data-testid="stMetricLabel"] {
            color: rgba(255,255,255,0.85);
        }
        h1, h2, h3, h4, h5,
        [data-testid="stMetricValue"],
        [data-testid="stSidebar"] h1 {
            color: #ffffff !important;
        }
        [data-testid="stCaptionContainer"] {
            color: rgba(255,255,255,0.55) !important;
        }
        hr {
            border-color: rgba(255,255,255,0.12) !important;
        }
        [data-testid="stTextInput"] input,
        [data-testid="stTextArea"] textarea {
            background: rgba(255,255,255,0.06) !important;
            border: 1px solid rgba(255,255,255,0.18) !important;
            color: white !important;
            border-radius: 10px !important;
        }
        button {
            border-radius: 10px !important;
        }
        [kind="formSubmit"], [data-testid="stFormSubmitButton"] button,
        [data-testid="stBaseButton-primary"] {
            background: linear-gradient(90deg, #8b5cf6, #38bdf8) !important;
            color: white !important;
            border: none !important;
        }
        [data-testid="stMetric"] {
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 14px;
            padding: 14px 16px;
        }
        [data-testid="stExpander"] {
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 14px;
        }
        [data-testid="stForm"] {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 16px;
            padding: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
