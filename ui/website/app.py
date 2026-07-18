"""
SixStage Website Application
"""

import os
import sys

import streamlit as st

# Make the project root importable so pages that reach into the
# actual product code (app.dashboard, app.services, etc.) resolve
# correctly no matter where `streamlit run` is launched from.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

# --- Fix: Streamlit's markdown renderer follows CommonMark, which only
# treats a block as raw HTML if it starts at column 0-3. Every component
# in this site writes its HTML as an indented Python string (for
# readability), which made Streamlit fall back to showing it as a literal
# code block instead of rendering it. Rather than hand-flatten every
# st.markdown(..., unsafe_allow_html=True) call across every component
# file, we normalize indentation once, globally, right here. This affects
# every page in the app (including the embedded product dashboard),
# since `streamlit` is a single shared module object.
_original_markdown = st.markdown


def _flattened_markdown(body, *args, **kwargs):

    if kwargs.get("unsafe_allow_html") and isinstance(body, str) and "\n" in body:
        # Drop blank lines too: components that interpolate other
        # components (e.g. the logo/icon snippets) reintroduce blank
        # lines at runtime that no amount of static source cleanup can
        # catch, and a blank line is exactly what makes Streamlit's
        # markdown parser stop treating the rest as raw HTML.
        body = "\n".join(
            line.strip()
            for line in body.split("\n")
            if line.strip()
        )

    return _original_markdown(body, *args, **kwargs)


st.markdown = _flattened_markdown

from home import render_home
from platform_page import render_platform
from solutions_page import render_solutions
from technology_page import render_technology
from company_page import render_company
from contact_page import render_contact
from security_platform import render_security_platform
from security_integrations import render_security_integrations
from security_scanning import render_security_scanning
from security_posture import render_security_posture
from security_copilot import render_security_copilot
from security_alerting import render_security_alerting
from security_console import render_security_console_page

from app.ui.dashboard import render_dashboard


st.set_page_config(
    page_title="SixStage",
    page_icon="S",
    layout="wide",
    initial_sidebar_state="collapsed"
)

pages = [
    st.Page(render_home, title="SixStage", url_path="home", default=True),
    st.Page(render_security_platform, title="Security Platform", url_path="security"),
    st.Page(render_platform, title="AI Sales Engineer", url_path="platform"),
    st.Page(render_dashboard, title="Live Platform", url_path="demo"),
    st.Page(render_solutions, title="Solutions", url_path="solutions"),
    st.Page(render_technology, title="Technology", url_path="technology"),
    st.Page(render_company, title="Company", url_path="company"),
    st.Page(render_contact, title="Contact", url_path="contact"),
    st.Page(render_security_integrations, title="Security Integrations", url_path="security-integrations"),
    st.Page(render_security_scanning, title="Continuous Scanning", url_path="security-scanning"),
    st.Page(render_security_posture, title="Posture & Risk Analysis", url_path="security-posture"),
    st.Page(render_security_copilot, title="AI Copilot Triage", url_path="security-copilot"),
    st.Page(render_security_alerting, title="Alerting & Remediation", url_path="security-alerting"),
    st.Page(render_security_console_page, title="Live Security Console", url_path="security-console"),
]

nav = st.navigation(pages, position="hidden")
nav.run()
