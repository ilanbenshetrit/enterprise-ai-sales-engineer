"""
SixStage Contact Page
"""

from theme import apply_theme
from components.header import render_header
from components.contact_content import render_contact_content
from components.footer import render_footer


def render_contact():

    apply_theme()

    render_header()
    render_contact_content()
    render_footer()
