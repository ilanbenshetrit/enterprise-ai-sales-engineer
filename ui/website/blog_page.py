"""
Blog Page
"""

import streamlit as st

from theme import apply_theme
from components.header import render_header, render_header_fade
from components.blog_content import render_blog_content
from components.footer import render_footer


def render_blog():

    apply_theme()

    render_header()
    render_header_fade()
    render_blog_content()

    render_footer()
