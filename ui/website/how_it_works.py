"""
How It Works Page — Become a SixStage Customer
"""

import streamlit as st

from theme import apply_theme
from components.header import render_header, render_header_fade
from components.how_it_works import render_how_it_works
from components.footer import render_footer


def render_how_it_works_page():

    apply_theme()

    render_header()
    render_header_fade()
    render_how_it_works()

    render_footer()
