"""
SixStage Security Platform — CI/CD & Cloud Integration Page
"""

import streamlit as st

from theme import apply_theme
from components.header import render_header, render_header_fade
from components.security_integrations_content import render_security_integrations_content
from components.footer import render_footer


def render_security_integrations():

    apply_theme()

    render_header()
    render_header_fade()
    render_security_integrations_content()

    st.markdown(
        """
        <div class="kf-cta">
            <div class="kf-cta-title">Talk to Us About Your Pipeline</div>
            <div class="kf-cta-desc">
            Every environment is wired differently. Tell us how your
            CI/CD, Kubernetes, and cloud setup looks and we will show you
            exactly where SixStage fits.
            </div>
            <a class="kf-cta-button" href="/contact" target="_self">Contact Us</a>
        </div>
        """,
        unsafe_allow_html=True
    )

    render_footer()
