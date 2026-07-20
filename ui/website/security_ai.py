"""
Security Platform — Stage 11 Page: AI & Identity Security
"""

import streamlit as st

from theme import apply_theme
from components.header import render_header, render_header_fade
from components.stage_ai_security import render_stage_ai_security
from components.footer import render_footer


def render_security_ai():

    apply_theme()

    render_header()
    render_header_fade()
    render_stage_ai_security()

    st.markdown(
        """
        <div class="kf-cta">
            <div class="kf-cta-title">See These Scanners Run on Real Findings</div>
            <div class="kf-cta-desc">
            The AI Workload, NHI, and MCP scanners are live in the actual
            product, not a mockup. Run them yourself in the console.
            </div>
            <a class="kf-cta-button" href="/security-console" target="_self">
            Open the Live Security Console
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    render_footer()
