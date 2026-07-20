"""
Solutions — Financial Services
"""

import streamlit as st

from theme import apply_theme
from components.header import render_header, render_header_fade
from components.industry_detail import render_industry_detail
from components.footer import render_footer


def render_solutions_financial():

    apply_theme()

    render_header()
    render_header_fade()
    render_industry_detail("financial-services")

    st.markdown(
        """
        <div class="kf-cta">
            <div class="kf-cta-title">Talk Through Your Financial Services Deal</div>
            <div class="kf-cta-desc">Tell us about the compliance and architecture constraints you're working within.</div>
            <a class="kf-cta-button" href="/contact" target="_self">Talk to Us</a>
        </div>
        """,
        unsafe_allow_html=True
    )

    render_footer()
