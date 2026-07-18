"""
Security Platform — Stage 03 Page: AI Copilot Triage
"""

import streamlit as st

from theme import apply_theme
from components.header import render_header
from components.stage_copilot import render_stage_copilot
from components.footer import render_footer


def render_security_copilot():

    apply_theme()

    render_header()
    render_stage_copilot()

    st.markdown(
        """
        <div class="kf-cta">
            <div class="kf-cta-title">See How Triage Becomes Action</div>
            <div class="kf-cta-desc">
            An answer is only useful if it reaches the team. Next, alerts
            and remediation close the loop.
            </div>
            <a class="kf-cta-button" href="/security-alerting" target="_self">
            Continue to Stage 04: Alerting &amp; Remediation
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    render_footer()
