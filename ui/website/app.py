"""
Kubeforge Website Application
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

from home import render_home
from platform_page import render_platform
from solutions_page import render_solutions
from technology_page import render_technology
from company_page import render_company
from contact_page import render_contact

from app.ui.dashboard import render_dashboard


st.set_page_config(
    page_title="Kubeforge",
    page_icon="K",
    layout="wide",
    initial_sidebar_state="collapsed"
)

pages = [
    st.Page(render_home, title="Kubeforge", url_path="home", default=True),
    st.Page(render_platform, title="Platform", url_path="platform"),
    st.Page(render_dashboard, title="Live Platform", url_path="demo"),
    st.Page(render_solutions, title="Solutions", url_path="solutions"),
    st.Page(render_technology, title="Technology", url_path="technology"),
    st.Page(render_company, title="Company", url_path="company"),
    st.Page(render_contact, title="Contact", url_path="contact"),
]

nav = st.navigation(pages, position="hidden")
nav.run()
