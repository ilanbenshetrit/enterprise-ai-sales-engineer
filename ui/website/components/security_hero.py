"""
Security Platform Page — Intro Banner
"""

import streamlit as st


def render_security_hero():

    st.markdown(
        """
        <div class="kf-platform-hero">
            <div class="kf-platform-eyebrow">Our Flagship Platform</div>
            <div class="kf-platform-title">
                <span class="gradient-text">KubeForge Security Co-Pilot</span>
                for Cloud-Native Infrastructure
            </div>
            <div class="kf-platform-desc">
                Continuous, AI-assisted security for the systems modern
                engineering teams actually run on: CI/CD pipelines,
                Kubernetes clusters, container images, and cloud
                environments. This is where Kubeforge's AI engineering
                work becomes a product &mdash; the same reasoning and
                automation discipline behind our AI Sales Engineer,
                applied to protecting infrastructure.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
