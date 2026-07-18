"""
SixStage Company Page
"""

import streamlit as st

from theme import apply_theme
from components.header import render_header
from components.stats import render_stats
from components.about import render_about
from components.vision import render_vision
from components.careers_content import render_careers_content
from components.footer import render_footer


def render_company():

    apply_theme()

    render_header()

    st.markdown(
        """
        <div class="kf-section" style="text-align:center; margin-bottom:0;">
            <div class="kf-section-label">Company</div>
            <div class="kf-section-title">Building SixStage</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    render_stats()
    render_about()
    render_vision()
    render_careers_content()

    st.markdown(
        """
        <div class="kf-cta">
            <div class="kf-cta-title">Want to Work With Us?</div>
            <div class="kf-cta-desc">
            Whether you are exploring a partnership or a role at SixStage,
            we would like to hear from you.
            </div>
            <a class="kf-cta-button" href="/contact" target="_self">Get in Touch</a>
        </div>
        """,
        unsafe_allow_html=True
    )

    render_footer()
