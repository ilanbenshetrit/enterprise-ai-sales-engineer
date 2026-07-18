"""
Kubeforge Platform Page
"""

import streamlit as st

from theme import apply_theme
from components.header import render_header
from components.platform_hero import render_platform_hero
from components.capabilities import render_capabilities
from components.footer import render_footer


def render_platform():

    apply_theme()

    render_header()
    render_platform_hero()
    render_capabilities()

    st.markdown(
        """
        <style>
        .kf-cta {
            text-align: center;
            max-width: 700px;
            margin: 90px auto 0;
        }
        .kf-cta-title {
            font-size: 30px;
            font-weight: 800;
            color: white;
            margin-bottom: 18px;
        }
        .kf-cta-desc {
            font-size: 16px;
            color: rgba(255,255,255,0.75);
            margin-bottom: 30px;
            line-height: 1.75;
        }
        </style>

        <div class="kf-cta" style="margin-top:90px;">
            <div class="kf-cta-title">Ready to Put This on Your Next Deal?</div>
            <div class="kf-cta-desc">
            Talk to our team about bringing the Kubeforge platform into
            your sales engineering workflow.
            </div>
            <a class="kf-cta-button" href="/" target="_self"
               style="text-decoration:none; display:inline-block; padding:15px 38px;
               border-radius:14px; font-size:17px; font-weight:600; color:white;
               background:linear-gradient(90deg,#8b5cf6,#38bdf8); margin-bottom:60px;">
               Back to Home
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    render_footer()
