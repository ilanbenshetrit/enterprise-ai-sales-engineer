"""
Solutions — Manufacturing & Supply Chain
"""

import streamlit as st

from theme import apply_theme
from components.header import render_header
from components.industry_detail import render_industry_detail
from components.footer import render_footer


def render_solutions_manufacturing():

    apply_theme()

    render_header()
    render_industry_detail("manufacturing")

    st.markdown(
        """
        <div class="kf-cta">
            <div class="kf-cta-title">Talk Through Your Manufacturing Deal</div>
            <div class="kf-cta-desc">Tell us about the OT/IT boundary and integration constraints you're working within.</div>
            <a class="kf-cta-button" href="/contact" target="_self">Talk to Us</a>
        </div>
        """,
        unsafe_allow_html=True
    )

    render_footer()
