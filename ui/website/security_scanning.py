"""
Security Platform — Stage 01 Page: Continuous Scanning
"""

import streamlit as st

from theme import apply_theme
from components.header import render_header
from components.stage_scanning import render_stage_scanning
from components.footer import render_footer


def render_security_scanning():

    apply_theme()

    render_header()
    render_stage_scanning()

    st.markdown(
        """
        <div class="kf-cta">
            <div class="kf-cta-title">See How Findings Become Risk Insight</div>
            <div class="kf-cta-desc">
            Raw findings are only the start. Next, KubeForge correlates
            everything into a single posture and risk view.
            </div>
            <a class="kf-cta-button" href="/security-posture" target="_self">
            Continue to Stage 02: Posture &amp; Risk Analysis
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    render_footer()
