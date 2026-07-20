"""
Customers Page
"""

import streamlit as st

from theme import apply_theme
from components.header import render_header, render_header_fade
from components.customers_content import render_customers_content
from components.footer import render_footer


def render_customers():

    apply_theme()

    render_header()
    render_header_fade()
    render_customers_content()

    render_footer()
