"""
Security Platform Page — How It Works Pipeline
"""

import streamlit as st


_STAGES = [
    {
        "n": "01",
        "title": "Continuous Scanning",
        "desc": (
            "Scheduled and on-demand scanners cover Kubernetes clusters, "
            "dependencies, source history, and network exposure &mdash; "
            "running continuously as part of the pipeline, not as a "
            "point-in-time audit."
        ),
        "href": "/security-scanning",
    },
    {
        "n": "02",
        "title": "Posture & Risk Analysis",
        "desc": (
            "Findings are correlated into a data security posture (DSPM) "
            "and cloud security posture (CSPM) view, so teams see risk "
            "ranked by actual exposure, not just a raw findings count."
        ),
        "href": "/security-posture",
    },
    {
        "n": "03",
        "title": "AI Copilot Triage",
        "desc": (
            "An AI copilot lets engineers ask questions about findings in "
            "plain language and get grounded answers &mdash; what changed, "
            "why it matters, and what to fix first."
        ),
        "href": "/security-copilot",
    },
    {
        "n": "04",
        "title": "Alerting & Remediation",
        "desc": (
            "New risk is pushed to the team the moment it's found, with "
            "Slack alerting wired into the same pipeline that triggered "
            "the scan, closing the loop from detection to action."
        ),
        "href": "/security-alerting",
    },
]


def render_security_pipeline():

    cards_html = "".join(
        f"""
        <a class="kf-stage-card" href="{stage['href']}" target="_self">
            <div class="kf-card-number">{stage['n']}</div>
            <div class="kf-card-title">{stage['title']}</div>
            <div class="kf-card-desc">{stage['desc']}</div>
            <div class="kf-stage-card-link">Explore this stage &rarr;</div>
        </a>
        """
        for stage in _STAGES
    )

    st.markdown(
        f"""
        <style>
        .kf-pipeline-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-top: 40px;
        }}
        </style>
        <div class="kf-section">
            <div class="kf-section-label">How It Works</div>
            <div class="kf-section-title">From First Scan to Resolved Risk</div>
            <div class="kf-pipeline-grid">
                {cards_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
