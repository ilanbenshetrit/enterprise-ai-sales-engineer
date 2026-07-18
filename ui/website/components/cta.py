"""
Kubeforge Closing CTA Section
"""

import streamlit as st


def render_cta():

    st.markdown(
        """
        <style>
        .kf-cta {
            text-align: center;
            max-width: 800px;
            margin: 110px auto 40px;
        }
        .kf-cta-title {
            font-size: 34px;
            font-weight: 800;
            color: white;
            margin-bottom: 20px;
        }
        .kf-cta-desc {
            font-size: 17px;
            color: rgba(255,255,255,0.75);
            margin-bottom: 36px;
            line-height: 1.75;
        }
        .kf-cta-button {
            display: inline-block;
            padding: 15px 38px;
            border-radius: 14px;
            font-size: 17px;
            font-weight: 600;
            color: white;
            background: linear-gradient(90deg, #8b5cf6, #38bdf8, #34d399);
            transition: 0.3s;
            margin-bottom: 80px;
            text-decoration: none;
        }
        .kf-cta-button:hover {
            transform: translateY(-6px);
            box-shadow: 0 20px 40px rgba(56,189,248,0.35);
        }
        </style>
        <div class="kf-cta">
            <div class="kf-cta-title">See the Platform Behind the Story</div>
            <div class="kf-cta-desc">Kubeforge's automation platform is already live
            inside enterprise environments worldwide. Explore how our AI engine
            analyzes opportunities, architects solutions, and plans delivery
            &mdash; end to end.</div>
            <a class="kf-cta-button" href="/platform" target="_self">Explore the Platform</a>
        </div>
        """,
        unsafe_allow_html=True
    )
