"""
Security Platform — Stage 04 Page: Alerting & Remediation
"""

import streamlit as st

from theme import apply_theme
from components.header import render_header, render_header_fade
from components.stage_alerting import render_stage_alerting
from components.footer import render_footer


def render_security_alerting():

    apply_theme()

    render_header()
    render_header_fade()
    render_stage_alerting()

    st.markdown(
        """
        <div class="kf-cta">
            <div class="kf-cta-title">See SixStage Fit Your Pipeline</div>
            <div class="kf-cta-desc">
            You've seen all four stages. Now see exactly how SixStage
            connects into your CI/CD, Kubernetes, and cloud environment.
            </div>
            <a class="kf-cta-button" href="/security-integrations" target="_self">
            See CI/CD &amp; Cloud Integration
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    render_footer()
