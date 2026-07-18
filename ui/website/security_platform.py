"""
Kubeforge Security Platform Page
"""

import streamlit as st

from theme import apply_theme
from components.header import render_header
from components.security_hero import render_security_hero
from components.security_pipeline import render_security_pipeline
from components.security_capabilities import render_security_capabilities
from components.security_domains import render_security_domains
from components.footer import render_footer


def render_security_platform():

    apply_theme()

    render_header()
    render_security_hero()
    render_security_pipeline()
    render_security_capabilities()
    render_security_domains()

    st.markdown(
        """
        <div class="kf-cta">
            <div class="kf-cta-title">See KubeForge Secure a Real Pipeline</div>
            <div class="kf-cta-desc">
            Explore how continuous scanning, posture management, and the
            AI copilot fit into your CI/CD, Kubernetes, and cloud
            workflows.
            </div>
            <a class="kf-cta-button" href="/security-integrations" target="_self">
            See CI/CD &amp; Cloud Integration
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    render_footer()
