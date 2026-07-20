"""
Security Platform — Stage 02 Page: Posture & Risk Analysis
"""

import streamlit as st

from theme import apply_theme
from components.header import render_header, render_header_fade
from components.stage_posture import render_stage_posture
from components.footer import render_footer


def render_security_posture():

    apply_theme()

    render_header()
    render_header_fade()
    render_stage_posture()

    st.markdown(
        """
        <div class="kf-cta">
            <div class="kf-cta-title">See How Posture Becomes an Answer</div>
            <div class="kf-cta-desc">
            A score is a starting point. Next, the AI copilot turns posture
            data into plain-language answers engineers can act on.
            </div>
            <a class="kf-cta-button" href="/security-copilot" target="_self">
            Continue to Stage 03: AI Copilot Triage
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    render_footer()
