"""
SixStage Company Page — Careers Teaser
"""

import streamlit as st


def render_careers_content():

    st.markdown(
        """
        <div class="kf-panel">
            <div class="kf-section" style="margin-top: 90px; margin-bottom: 90px;">
                <div class="kf-section-label">Careers</div>
                <div class="kf-section-title">Build the Infrastructure Layer for Enterprise AI</div>
                <div class="kf-section-body">
                    <p>We are a small, senior team by design &mdash; engineers
                    and researchers who would rather ship one production
                    system than ten demos. If that sounds like how you like
                    to work, we would like to hear from you.</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
