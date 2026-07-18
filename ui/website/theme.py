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

        /* Shared section/CTA primitives reused across pages */

        .kf-section {
            max-width: 1050px;
            margin: 40px auto 100px;
        }
        .kf-section-label {
            color: #38bdf8;
            font-size: 14px;
            font-weight: 700;
            letter-spacing: 3px;
            text-transform: uppercase;
            margin-bottom: 16px;
        }
        .kf-section-title {
            font-size: 38px;
            font-weight: 800;
            color: white;
            margin-bottom: 28px;
            line-height: 1.25;
        }
        .kf-section-body {
            font-size: 18px;
            line-height: 1.85;
            color: rgba(255,255,255,0.8);
        }
        .kf-section-body p {
            margin-bottom: 20px;
        }
        .kf-panel {
            background: rgba(255,255,255,0.03);
            border-top: 1px solid rgba(255,255,255,0.08);
            border-bottom: 1px solid rgba(255,255,255,0.08);
        }
        .kf-card-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 22px;
            margin-top: 40px;
        }
        .kf-card {
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 18px;
            padding: 28px;
            transition: 0.3s;
        }
        .kf-card:hover {
            transform: translateY(-6px);
            border-color: rgba(56,189,248,0.4);
        }
        .kf-card-number {
            font-size: 34px;
            font-weight: 800;
            background: linear-gradient(90deg, #c084fc, #38bdf8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 14px;
            line-height: 1;
        }
        .kf-card-title {
            font-size: 18px;
            font-weight: 700;
            color: white;
            margin-bottom: 10px;
        }
        .kf-card-desc {
            font-size: 14px;
            line-height: 1.7;
            color: rgba(255,255,255,0.68);
        }
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
        .kf-cta-button {
            display: inline-block;
            padding: 15px 38px;
            border-radius: 14px;
            font-size: 17px;
            font-weight: 600;
            color: white;
            background: linear-gradient(90deg, #8b5cf6, #38bdf8);
            transition: 0.3s;
            margin-bottom: 80px;
            text-decoration: none;
        }
        .kf-cta-button:hover {
            transform: translateY(-6px);
            box-shadow: 0 20px 40px rgba(56,189,248,0.35);
        }

        </style>
        """,
        unsafe_allow_html=True
    )