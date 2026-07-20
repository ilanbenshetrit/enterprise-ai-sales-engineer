"""
Industry Detail — Shared Renderer

One component, driven by components/industry_data.py, used by all six
industry pages so content and layout can't drift apart.
"""

import streamlit as st

from components.industry_data import INDUSTRIES


def render_industry_detail(slug: str):

    industry = INDUSTRIES[slug]

    points_html = "".join(
        f"""
        <div class="kf-stage-card">
            <div class="kf-card-title">{p['title']}</div>
            <div class="kf-card-desc">{p['desc']}</div>
        </div>
        """
        for p in industry["points"]
    )

    st.markdown(
        f"""
        <a class="kf-stage-back" href="/solutions" target="_self">&larr; Back to Solutions</a>
        <div class="kf-stage-hero">
            <div class="kf-stage-eyebrow">Solutions &middot; {industry['title']}</div>
            <div class="kf-stage-title">
                Built for <span class="gradient-text">{industry['title']}</span>
            </div>
            <div class="kf-stage-desc">
                {industry['desc']}
            </div>
        </div>
        <div class="kf-section">
            <div class="kf-section-label">Where It Fits</div>
            <div class="kf-section-title">How the Six Stages Adapt</div>
            <div class="kf-card-grid">
                {points_html}
            </div>
        </div>
        <div class="kf-mock-panel" style="margin-top:20px;">
            <div class="kf-mock-panel-label">Typical Deal Shape</div>
            <div class="kf-stage-desc" style="text-align:left; max-width:none;">
                {industry['deal_shape']}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
