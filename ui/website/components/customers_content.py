"""
Customers Page Content — Honest Early-Stage Placeholder

No fabricated logos or testimonials. SixStage is early; this page says
so plainly and routes interested visitors to become the next case study.
"""

import streamlit as st


def render_customers_content():

    st.markdown(
        """
        <div class="kf-stage-hero">
            <div class="kf-stage-eyebrow">Customers</div>
            <div class="kf-stage-title">
                We're <span class="gradient-text">Early</span> — By Design
            </div>
            <div class="kf-stage-desc">
                SixStage is a young platform. We'd rather tell you that
                plainly than paper over it with logos that aren't real.
                The product in the Live Console is the actual thing our
                first customers will run &mdash; not a demo built for
                this page.
            </div>
        </div>
        <div class="kf-mock-panel" style="margin-top:20px; text-align:center; padding:36px;">
            <div class="kf-mock-panel-label" style="padding:0 0 10px;">Want to Be Our First Case Study?</div>
            <div class="kf-stage-desc" style="max-width:520px; margin:0 auto;">
                Early customers get direct access to the team building the
                product, input on the roadmap, and founder-era pricing.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
