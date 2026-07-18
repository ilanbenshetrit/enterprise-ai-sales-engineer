"""
Kubeforge Vision Section
"""

import streamlit as st


def render_vision():

    st.markdown(
        """
        <style>
        .kf-panel {
            background: rgba(255,255,255,0.03);
            border-top: 1px solid rgba(255,255,255,0.08);
            border-bottom: 1px solid rgba(255,255,255,0.08);
        }
        </style>

        <div class="kf-panel">
            <div class="kf-section" style="margin-top: 90px; margin-bottom: 90px;">
                <div class="kf-section-label">Our Vision</div>
                <div class="kf-section-title">AI as Infrastructure, Not Experiment</div>
                <div class="kf-section-body">
                    <p>We believe the next decade of enterprise value creation will be
                    won or lost on a single capability: the ability to turn AI from an
                    experiment into infrastructure. Not AI as a feature bolted onto
                    existing software &mdash; AI as the operating layer that plans,
                    decides, and acts across an organization's most important
                    processes.</p>

                    <p>Our vision is a world where every enterprise, regardless of
                    industry or technical maturity, can deploy autonomous AI systems
                    with the same confidence, security, and control they expect from
                    their core infrastructure. We are building the tooling, the
                    architecture patterns, and the governance layer to make that
                    possible &mdash; one production deployment at a time.</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
