"""
Kubeforge Global Theme
"""

import streamlit as st


def apply_theme():

    st.markdown(
        """
        <style>

        [data-testid="stAppViewContainer"] {

            background:
            linear-gradient(
                135deg,
                #0f172a 0%,
                #312e81 45%,
                #2563eb 100%
            );

        }


        [data-testid="stHeader"] {

            background:
            transparent;

        }


        .block-container {

            padding-top:
            3rem;

            padding-left:
            5rem;

            padding-right:
            5rem;

        }


        .gradient-text {

            background:
            linear-gradient(
                90deg,
                #c084fc,
                #38bdf8
            );

            -webkit-background-clip:
            text;

            -webkit-text-fill-color:
            transparent;

        }


        </style>
        """,
        unsafe_allow_html=True
    )