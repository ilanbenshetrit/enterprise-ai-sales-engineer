"""
Kubeforge Corporate Header
"""

import streamlit as st

from components.logo import kf_logo_lockup


def render_header():

    st.markdown(
        f"""
        <style>
        .kf-logo {{
            font-weight: 800;
            letter-spacing: -1px;
            background: linear-gradient(90deg, #c084fc, #38bdf8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .kf-header {{
            width: 100%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0px;
            margin-bottom: 60px;
        }}
        .kf-menu {{
            display: flex;
            gap: 15px;
            align-items: center;
        }}
        .kf-item {{
            color: white;
            padding: 12px 18px;
            border-radius: 12px;
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.15);
            transition: 0.3s;
            text-decoration: none;
            display: inline-block;
        }}
        .kf-item:hover {{
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(56,189,248,0.35);
        }}
        </style>
        <div class="kf-header">
            {kf_logo_lockup()}
            <div class="kf-menu">
                <a class="kf-item" href="/platform" target="_self">Platform</a>
                <a class="kf-item" href="/solutions" target="_self">Solutions</a>
                <a class="kf-item" href="/technology" target="_self">Technology</a>
                <a class="kf-item" href="/company" target="_self">Company</a>
                <a class="kf-item" href="/contact" target="_self">Contact</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
