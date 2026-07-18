"""
SixStage Global Theme
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


        .kf-tagline {
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 3px;
            text-transform: uppercase;
            background: linear-gradient(90deg, #c084fc, #38bdf8, #34d399);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .gradient-text {

            background:
            linear-gradient(
                90deg,
                #c084fc,
                #38bdf8,
                #34d399
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
            background: linear-gradient(90deg, #c084fc, #38bdf8, #34d399);
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
            background: linear-gradient(90deg, #8b5cf6, #38bdf8, #34d399);
            transition: 0.3s;
            margin-bottom: 80px;
            text-decoration: none;
        }
        .kf-cta-button:hover {
            transform: translateY(-6px);
            box-shadow: 0 20px 40px rgba(56,189,248,0.35);
        }

        /* Stage detail pages (security pipeline drill-down) */

        .kf-stage-hero {
            text-align: center;
            padding: 60px 20px 20px;
            max-width: 900px;
            margin: 0 auto;
        }
        .kf-stage-back {
            display: inline-block;
            color: #38bdf8;
            font-size: 14px;
            font-weight: 600;
            text-decoration: none;
            margin-bottom: 28px;
        }
        .kf-stage-back:hover {
            text-decoration: underline;
        }
        .kf-stage-eyebrow {
            color: #38bdf8;
            font-size: 14px;
            font-weight: 700;
            letter-spacing: 3px;
            text-transform: uppercase;
            margin-bottom: 18px;
        }
        .kf-stage-title {
            font-size: 46px;
            font-weight: 800;
            color: white;
            line-height: 1.2;
            margin-bottom: 22px;
        }
        .kf-stage-desc {
            font-size: 18px;
            line-height: 1.75;
            color: rgba(255,255,255,0.8);
        }

        /* Clickable stage card (pipeline -> detail page) */

        .kf-stage-card {
            display: block;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 18px;
            padding: 28px;
            transition: 0.3s;
            text-decoration: none;
            color: inherit;
        }
        .kf-stage-card:hover {
            transform: translateY(-6px);
            border-color: rgba(56,189,248,0.4);
        }
        .kf-stage-card-link {
            margin-top: 16px;
            font-size: 13px;
            font-weight: 600;
            color: #38bdf8;
        }

        /* Mock product panel (sample output shown on stage detail pages) */

        .kf-mock-panel {
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 18px;
            padding: 8px 28px;
            margin-top: 36px;
        }
        .kf-mock-panel-label {
            color: #38bdf8;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
            padding: 18px 0 10px;
        }
        .kf-mock-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 16px;
            padding: 16px 0;
            border-top: 1px solid rgba(255,255,255,0.08);
        }
        .kf-mock-main {
            font-size: 15px;
            font-weight: 600;
            color: white;
            margin-bottom: 4px;
        }
        .kf-mock-sub {
            font-size: 13px;
            color: rgba(255,255,255,0.6);
        }
        .kf-tag {
            flex-shrink: 0;
            font-size: 12px;
            font-weight: 700;
            padding: 6px 14px;
            border-radius: 999px;
            white-space: nowrap;
        }
        .kf-tag-purple {
            color: #e9d5ff;
            background: rgba(192,132,252,0.18);
            border: 1px solid rgba(192,132,252,0.4);
        }
        .kf-tag-blue {
            color: #bae6fd;
            background: rgba(56,189,248,0.15);
            border: 1px solid rgba(56,189,248,0.4);
        }
        .kf-tag-muted {
            color: rgba(255,255,255,0.65);
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.15);
        }

        /* Score cards (posture stage) */

        .kf-score-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-top: 36px;
        }
        .kf-score-card {
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 18px;
            padding: 26px 22px;
            text-align: center;
        }
        .kf-score-value {
            font-size: 36px;
            font-weight: 800;
            background: linear-gradient(90deg, #c084fc, #38bdf8, #34d399);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 8px;
            line-height: 1;
        }
        .kf-score-label {
            font-size: 13px;
            font-weight: 600;
            color: rgba(255,255,255,0.68);
        }

        /* AI copilot chat mock (copilot stage) */

        .kf-chat-panel {
            margin-top: 36px;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }
        .kf-chat-bubble {
            max-width: 72%;
            padding: 16px 20px;
            border-radius: 16px;
            font-size: 15px;
            line-height: 1.65;
        }
        .kf-chat-user {
            align-self: flex-end;
            background: linear-gradient(90deg, #8b5cf6, #38bdf8, #34d399);
            color: white;
            border-bottom-right-radius: 4px;
        }
        .kf-chat-ai {
            align-self: flex-start;
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.1);
            color: rgba(255,255,255,0.88);
            border-bottom-left-radius: 4px;
        }

        /* Alert log mock (alerting stage) */

        .kf-alert-list {
            margin-top: 36px;
            display: flex;
            flex-direction: column;
            gap: 14px;
        }
        .kf-alert-item {
            display: flex;
            gap: 16px;
            align-items: flex-start;
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.1);
            border-left: 3px solid #38bdf8;
            border-radius: 12px;
            padding: 18px 22px;
        }
        .kf-alert-time {
            flex-shrink: 0;
            font-size: 13px;
            font-weight: 600;
            color: #38bdf8;
            width: 90px;
        }
        .kf-alert-text {
            font-size: 14px;
            line-height: 1.65;
            color: rgba(255,255,255,0.85);
        }

        </style>
        """,
        unsafe_allow_html=True
    )