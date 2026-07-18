"""
Kubeforge Website Application
"""

import streamlit as st

from home import render_home
from platform_page import render_platform


st.set_page_config(
    page_title="Kubeforge",
    page_icon="K",
    layout="wide",
    initial_sidebar_state="collapsed"
)

pages = [
    st.Page(render_home, title="Kubeforge", url_path="home", default=True),
    st.Page(render_platform, title="Platform", url_path="platform"),
]

nav = st.navigation(pages, position="hidden")
nav.run()
