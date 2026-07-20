"""
Docs Page
"""

import streamlit as st

from theme import apply_theme
from components.header import render_header, render_header_fade
from components.docs_content import render_docs_content
from components.footer import render_footer


def render_docs():

    apply_theme()

    render_header()
    render_header_fade()
    render_docs_content()

    render_footer()
