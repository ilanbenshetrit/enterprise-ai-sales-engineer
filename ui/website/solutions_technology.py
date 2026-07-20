"""
Solutions — Technology & SaaS
"""

import streamlit as st

from theme import apply_theme
from components.header import render_header
from components.industry_detail import render_industry_detail
from components.footer import render_footer


def render_solutions_technology():

    apply_theme()

    render_header()
    render_industry_detail("technology")

    st.markdown(
        """
        <div class="kf-cta">
            <div class="kf-cta-title">Talk Through Your Technology Deal</div>
            <div class="kf-cta-desc">Tell us about the integration surface and multi-tenant requirements you're scoping.</div>
            <a class="kf-cta-button" href="/contact" target="_self">Talk to Us</a>
        </div>
        """,
        unsafe_allow_html=True
    )

    render_footer()
