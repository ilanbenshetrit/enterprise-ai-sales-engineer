"""
Kubeforge About / Origin Story Section
"""

import streamlit as st


def render_about():

    st.markdown(
        """
        <style>
        .kf-section {
            max-width: 950px;
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
        </style>
        <div class="kf-section">
            <div class="kf-section-label">Our Story</div>
            <div class="kf-section-title">From Research Lab to Enterprise Infrastructure</div>
            <div class="kf-section-body">
                <p>Kubeforge was founded in 2019 by a small team of machine learning
                researchers and enterprise infrastructure engineers who had spent years
                building AI systems inside hyperscale cloud providers &mdash; and kept
                watching the same pattern play out: brilliant proof-of-concepts that
                never survived contact with legacy systems, compliance requirements, or
                the operational complexity of a real enterprise.</p>
                <p>We started Kubeforge to close that gap. Not another AI demo. Not
                another chatbot wrapper. A platform engineered from day one to take AI
                out of the sandbox and into production &mdash; inside the messy,
                regulated, mission-critical environments where enterprises actually
                operate.</p>
                <p>Since our first deployment inside a regional financial institution's
                claims processing pipeline, Kubeforge has grown from a three-person
                engineering team into a global partner trusted by enterprises across
                financial services, healthcare, manufacturing, logistics, and the
                public sector.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
