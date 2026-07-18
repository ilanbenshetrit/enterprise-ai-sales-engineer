"""
Kubeforge Home Page — Flagship Product Band
"""

import streamlit as st


def render_flagship_band():

    st.markdown(
        """
        <div class="kf-panel">
            <div class="kf-section" style="margin-top: 90px; margin-bottom: 90px; text-align: center;">
                <div class="kf-section-label">Our Flagship Platform</div>
                <div class="kf-section-title">
                    <span class="gradient-text">KubeForge Security Co-Pilot</span>
                </div>
                <div class="kf-section-body" style="max-width: 750px; margin: 0 auto;">
                    <p>Everything Kubeforge builds &mdash; agent orchestration,
                    retrieval-grounded reasoning, automated planning &mdash;
                    comes together in our flagship product: an AI-native
                    security platform for CI/CD pipelines, Kubernetes,
                    containers, and cloud. It's the clearest proof of what
                    our AI engineering work is built to do.</p>
                </div>
                <a class="kf-cta-button" href="/security" target="_self"
                   style="margin-top: 10px;">Explore the Security Platform</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
