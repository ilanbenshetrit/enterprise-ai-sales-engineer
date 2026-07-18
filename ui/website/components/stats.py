"""
Kubeforge Stats Bar
"""

import streamlit as st


def render_stats():

    st.markdown(
        """
        <style>
        .kf-stats {
            display: flex;
            justify-content: center;
            gap: 70px;
            padding: 50px 20px 90px;
            flex-wrap: wrap;
        }
        .kf-stat { text-align: center; }
        .kf-stat-number {
            font-size: 42px;
            font-weight: 800;
            background: linear-gradient(90deg, #c084fc, #38bdf8, #34d399);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .kf-stat-label {
            color: rgba(255,255,255,0.65);
            font-size: 14px;
            margin-top: 6px;
            letter-spacing: 1px;
            text-transform: uppercase;
        }
        </style>
        <div class="kf-stats">
            <div class="kf-stat">
                <div class="kf-stat-number">50+</div>
                <div class="kf-stat-label">Enterprise Deployments</div>
            </div>
            <div class="kf-stat">
                <div class="kf-stat-number">12</div>
                <div class="kf-stat-label">Industries Served</div>
            </div>
            <div class="kf-stat">
                <div class="kf-stat-number">3.5M+</div>
                <div class="kf-stat-label">Hours Automated Annually</div>
            </div>
            <div class="kf-stat">
                <div class="kf-stat-number">99.98%</div>
                <div class="kf-stat-label">Platform Uptime</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
