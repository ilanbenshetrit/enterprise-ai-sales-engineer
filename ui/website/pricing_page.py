"""
Pricing Page
"""

import streamlit as st

from theme import apply_theme
from components.header import render_header
from components.pricing_content import render_pricing_content
from components.footer import render_footer


def render_pricing():

    apply_theme()

    render_header()
    render_pricing_content()

    render_footer()
