"""
Get Started Page — Self-Serve Tenant Registration
"""

import streamlit as st

from theme import apply_theme
from components.header import render_header, render_header_fade
from components.get_started import render_get_started
from components.footer import render_footer


def render_get_started_page():

    apply_theme()

    render_header()
    render_header_fade()
    render_get_started()

    render_footer()
