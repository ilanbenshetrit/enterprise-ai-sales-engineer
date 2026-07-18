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
            background: linear-gradient(90deg, #c084fc, #38bdf8, #34d399);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .kf-header {{
            width: 100%;
            display: grid;
            grid-template-columns: 1fr auto 1fr;
            align-items: center;
            padding: 20px 0px;
            margin-bottom: 60px;
        }}
        .kf-header-logo {{
            grid-column: 1;
            justify-self: start;
        }}
        .kf-menu {{
            grid-column: 2;
            justify-self: center;
            display: flex;
            gap: 38px;
            align-items: center;
            perspective: 600px;
        }}
        .kf-header-spacer {{
            grid-column: 3;
        }}
        .kf-item {{
            color: rgba(255,255,255,0.85);
            font-size: 15px;
            font-weight: 600;
            text-decoration: none;
            display: inline-block;
            padding: 6px 2px;
            text-shadow:
                1px 1px 0 rgba(192,132,252,0.35),
                2px 2px 0 rgba(56,189,248,0.25),
                3px 3px 6px rgba(0,0,0,0.25);
            transition: transform 0.25s ease, color 0.25s ease, text-shadow 0.25s ease;
        }}
        .kf-item:hover {{
            color: white;
            transform: scale(1.18) translateY(-3px);
            text-shadow:
                1px 1px 0 rgba(192,132,252,0.6),
                2px 2px 0 rgba(56,189,248,0.5),
                3px 3px 0 rgba(52,211,153,0.4),
                4px 6px 10px rgba(0,0,0,0.35);
        }}
        </style>
        <div class="kf-header">
            <div class="kf-header-logo">{kf_logo_lockup()}</div>
            <div class="kf-menu">
                <a class="kf-item" href="/security" target="_self">Security Platform</a>
                <a class="kf-item" href="/platform" target="_self">AI Sales Engineer</a>
                <a class="kf-item" href="/solutions" target="_self">Solutions</a>
                <a class="kf-item" href="/technology" target="_self">Technology</a>
                <a class="kf-item" href="/company" target="_self">Company</a>
                <a class="kf-item" href="/contact" target="_self">Contact</a>
            </div>
            <div class="kf-header-spacer"></div>
        </div>
        """,
        unsafe_allow_html=True
    )
