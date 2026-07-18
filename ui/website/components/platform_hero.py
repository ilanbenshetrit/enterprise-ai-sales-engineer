"""
Kubeforge Platform Page — Intro Banner
"""

import streamlit as st


def render_platform_hero():

    st.markdown(
        """
        <style>
        .kf-platform-hero {
            text-align: center;
            padding: 60px 20px 20px;
            max-width: 900px;
            margin: 0 auto;
        }
        .kf-platform-eyebrow {
            color: #38bdf8;
            font-size: 14px;
            font-weight: 700;
            letter-spacing: 3px;
            text-transform: uppercase;
            margin-bottom: 18px;
        }
        .kf-platform-title {
            font-size: 52px;
            font-weight: 800;
            color: white;
            line-height: 1.15;
            margin-bottom: 24px;
        }
        .kf-platform-desc {
            font-size: 19px;
            line-height: 1.7;
            color: rgba(255,255,255,0.8);
        }
        </style>
        <div class="kf-platform-hero">
            <div class="kf-platform-eyebrow">The Kubeforge Platform</div>
            <div class="kf-platform-title">
                One AI engine.
                <span class="gradient-text">Six stages</span>
                of enterprise sales engineering.
            </div>
            <div class="kf-platform-desc">
                From the first signal in a CRM record to a delivered solution
                package, Kubeforge's platform is already running the full
                technical sales workflow &mdash; so your engineers spend their
                time on judgment calls, not busywork.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
