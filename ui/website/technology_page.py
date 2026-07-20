"""
SixStage Technology Page
"""

import streamlit as st

from theme import apply_theme
from components.header import render_header, render_header_fade
from components.technology_content import render_technology_content
from components.footer import render_footer


def render_technology():

    apply_theme()

    render_header()
    render_header_fade()
    render_technology_content()

    st.markdown(
        """
        <div class="kf-cta">
            <div class="kf-cta-title">See the Engine Run</div>
            <div class="kf-cta-desc">
            The clearest way to understand the architecture is to watch it
            work on a real opportunity.
            </div>
            <a class="kf-cta-button" href="/demo" target="_self">View the Live Platform</a>
        </div>
        """,
        unsafe_allow_html=True
    )

    render_footer()
