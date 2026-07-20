"""
SixStage Solutions Page
"""

import streamlit as st

from theme import apply_theme
from components.header import render_header, render_header_fade
from components.solutions_content import render_solutions_content
from components.footer import render_footer


def render_solutions():

    apply_theme()

    render_header()
    render_header_fade()
    render_solutions_content()

    st.markdown(
        """
        <div class="kf-cta">
            <div class="kf-cta-title">Not Sure Where to Start?</div>
            <div class="kf-cta-desc">
            Tell us about your industry and we will show you exactly where
            SixStage fits into your sales engineering workflow.
            </div>
            <a class="kf-cta-button" href="/contact" target="_self">Talk to Us</a>
        </div>
        """,
        unsafe_allow_html=True
    )

    render_footer()
