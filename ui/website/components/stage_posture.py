"""
Security Platform — Stage 02 Detail: Posture & Risk Analysis
"""

import streamlit as st


_SCORES = [
    {"value": "82", "label": "Cloud Posture (CSPM)"},
    {"value": "91", "label": "Data Exposure (DSPM)"},
    {"value": "76", "label": "Kubernetes Hardening"},
    {"value": "88", "label": "Supply Chain Health"},
]

_AREAS = [
    {
        "n": "01",
        "title": "Data Security Posture (DSPM)",
        "desc": (
            "Discovers and classifies sensitive data across your stores, "
            "and tracks how that posture moves over time instead of a "
            "single point-in-time audit."
        ),
    },
    {
        "n": "02",
        "title": "Cloud Security Posture (CSPM)",
        "desc": (
            "Cloud account configuration checked continuously against "
            "compliance and security baselines across every provider "
            "account in scope."
        ),
    },
    {
        "n": "03",
        "title": "Risk Correlation",
        "desc": (
            "Findings from every scanner are correlated rather than listed "
            "in isolation, so a chain of small issues that adds up to real "
            "exposure doesn't get missed."
        ),
    },
    {
        "n": "04",
        "title": "Historical Trend",
        "desc": (
            "Posture scores are tracked over time, so teams can see "
            "whether risk is trending up or down, not just where it "
            "stands today."
        ),
    },
]


def render_stage_posture():

    scores_html = "".join(
        f"""
        <div class="kf-score-card">
            <div class="kf-score-value">{s['value']}</div>
            <div class="kf-score-label">{s['label']}</div>
        </div>
        """
        for s in _SCORES
    )

    cards_html = "".join(
        f"""
        <a class="kf-stage-card" href="/security-copilot" target="_self">
            <div class="kf-card-number">{a['n']}</div>
            <div class="kf-card-title">{a['title']}</div>
            <div class="kf-card-desc">{a['desc']}</div>
            <div class="kf-stage-card-link">See how the copilot uses this &rarr;</div>
        </a>
        """
        for a in _AREAS
    )

    st.markdown(
        f"""
        <a class="kf-stage-back" href="/security" target="_self">&larr; Back to Security Platform</a>
        <div class="kf-stage-hero">
            <div class="kf-stage-eyebrow">Stage 02 &middot; Posture &amp; Risk Analysis</div>
            <div class="kf-stage-title">
                From findings to a <span class="gradient-text">single posture score</span>
            </div>
            <div class="kf-stage-desc">
                Every scan feeds a running DSPM and CSPM view, so risk is
                ranked by actual exposure &mdash; not by how many findings a
                scanner happened to produce.
            </div>
        </div>
        <div class="kf-section">
            <div class="kf-score-grid">
                {scores_html}
            </div>
            <div class="kf-card-grid" style="margin-top: 60px;">
                {cards_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
