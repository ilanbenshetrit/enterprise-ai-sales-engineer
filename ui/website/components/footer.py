"""
Kubeforge Website Footer
"""

import streamlit as st

from components.logo import kf_logo_lockup


def render_footer():

    st.divider()

    st.markdown(
        f"""
        <div style="text-align:center; padding:20px 40px 40px;">
            <div style="display:flex; justify-content:center; margin-bottom:16px;">
                {kf_logo_lockup(size=32, wordmark_size="22px")}
            </div>
            <p style="color:#94a3b8; font-size:16px; margin:0 0 16px;">
            AI Engineering &amp; Cloud-Native Security
            </p>
            <p style="color:#94a3b8; font-size:15px;">
            <a href="/security" target="_self" style="color:#94a3b8; text-decoration:none;">Security Platform</a>
            &nbsp;|&nbsp;
            <a href="/platform" target="_self" style="color:#94a3b8; text-decoration:none;">AI Sales Engineer</a>
            &nbsp;|&nbsp;
            <a href="/company" target="_self" style="color:#94a3b8; text-decoration:none;">About Us</a>
            &nbsp;|&nbsp;
            <a href="/contact" target="_self" style="color:#94a3b8; text-decoration:none;">Contact</a>
            &nbsp;|&nbsp;
            <a href="/company" target="_self" style="color:#94a3b8; text-decoration:none;">Careers</a>
            </p>
            <p style="color:#64748b; font-size:14px; margin-top:16px;">
            &copy; 2026 Kubeforge. All rights reserved.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
