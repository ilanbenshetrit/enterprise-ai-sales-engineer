"""
Security Platform — Live Console Page
"""

import streamlit as st

from theme import apply_theme
from components.header import render_header, render_header_fade
from components.security_console import render_security_console
from components.footer import render_footer


def render_security_console_page():

    apply_theme()

    render_header()
    render_header_fade()
    render_security_console()

    st.markdown(
        """
        <div class="kf-cta">
            <div class="kf-cta-title">Questions About Deploying This for Real</div>
            <div class="kf-cta-desc">
            The console above is the real backend running locally. Talk to
            us about deploying it against your actual infrastructure.
            </div>
            <a class="kf-cta-button" href="/contact" target="_self">Contact Us</a>
        </div>
        """,
        unsafe_allow_html=True
    )

    render_footer()
