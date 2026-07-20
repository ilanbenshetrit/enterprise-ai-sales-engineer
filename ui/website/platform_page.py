"""
SixStage Platform Page
"""

import streamlit as st

from theme import apply_theme
from components.header import render_header, render_header_fade
from components.platform_hero import render_platform_hero
from components.capabilities import render_capabilities
from components.footer import render_footer


def render_platform():

    apply_theme()

    render_header()
    render_header_fade()
    render_platform_hero()
    render_capabilities()

    st.markdown(
        """
        <div class="kf-cta">
            <div class="kf-cta-title">Ready to Put This on Your Next Deal?</div>
            <div class="kf-cta-desc">
            Every stage above is running real product code. See it work end
            to end on a live opportunity.
            </div>
            <a class="kf-cta-button" href="/demo" target="_self">View the Live Platform</a>
        </div>
        """,
        unsafe_allow_html=True
    )

    render_footer()
