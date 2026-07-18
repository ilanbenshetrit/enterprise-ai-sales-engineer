"""
Kubeforge Home Page — Signature Mark

A quiet branding moment placed roughly midway down the home page: the
company name rendered in an elegant script, like a signature, using
all three of the site's accent colors. Not a headline — a pause.
"""

import streamlit as st


def render_signature():

    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Alex+Brush&display=swap');
        .kf-signature-wrap {
            text-align: center;
            padding: 50px 20px;
        }
        .kf-signature {
            font-family: 'Alex Brush', cursive;
            font-size: 68px;
            font-weight: 400;
            line-height: 1;
            background: linear-gradient(90deg, #c084fc, #38bdf8, #34d399);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: inline-block;
        }
        </style>
        <div class="kf-signature-wrap">
            <span class="kf-signature">Kubeforge</span>
        </div>
        """,
        unsafe_allow_html=True
    )
