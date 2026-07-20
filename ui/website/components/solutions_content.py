"""
SixStage Solutions Page Content
"""

import streamlit as st

from components.industry_data import INDUSTRIES


def render_solutions_content():

    cards_html = "".join(
        f"""
        <a class="kf-stage-card" href="{ind['href']}" target="_self">
            <div class="kf-card-number">{ind['n']}</div>
            <div class="kf-card-title">{ind['title']}</div>
            <div class="kf-card-desc">{ind['desc']}</div>
            <div class="kf-stage-card-link">Explore this industry &rarr;</div>
        </a>
        """
        for ind in INDUSTRIES.values()
    )

    st.markdown(
        f"""
        <div class="kf-section">
            <div class="kf-section-label">Solutions</div>
            <div class="kf-section-title">One Platform, Tailored to Every Industry</div>
            <div class="kf-section-body">
                <p>The same six-stage engine adapts to the constraints,
                compliance frameworks, and buying process of your industry
                &mdash; so every recommendation already speaks the customer's
                language.</p>
            </div>
            <div class="kf-card-grid">
                {cards_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
