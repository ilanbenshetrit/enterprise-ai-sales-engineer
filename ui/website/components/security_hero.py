"""
Security Platform Page — Intro Banner
"""

import streamlit as st


def render_security_hero():

    st.markdown(
        """
        <style>
        .kf-security-hero {
            text-align: center;
            padding: 60px 20px 20px;
            max-width: 900px;
            margin: 0 auto;
        }
        .kf-security-eyebrow {
            color: #38bdf8;
            font-size: 14px;
            font-weight: 700;
            letter-spacing: 3px;
            text-transform: uppercase;
            margin-bottom: 18px;
        }
        .kf-security-title {
            font-size: 52px;
            font-weight: 800;
            color: white;
            line-height: 1.15;
            margin-bottom: 24px;
        }
        .kf-security-desc {
            font-size: 19px;
            line-height: 1.7;
            color: rgba(255,255,255,0.8);
        }
        </style>
        <div class="kf-security-hero">
            <div class="kf-security-eyebrow">Our Flagship Platform</div>
            <div class="kf-security-title">
                <span class="gradient-text">KubeForge Security Co-Pilot</span>
                for Cloud-Native Infrastructure
            </div>
            <div class="kf-security-desc">
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
