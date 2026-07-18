"""
Security Platform — CI/CD & Cloud Integration Page Content
"""

import streamlit as st


_INTEGRATIONS = [
    {
        "title": "CI/CD Pipelines",
        "desc": (
            "SixStage plugs into your existing pipeline as a stage, not a "
            "separate tool teams have to remember to run. Scans trigger on "
            "every build, and a pipeline can be configured to fail on "
            "newly introduced critical risk &mdash; the same gate teams "
            "already use for tests and linting."
        ),
    },
    {
        "title": "Kubernetes Clusters",
        "desc": (
            "Cluster configuration, workload permissions, and exposed "
            "services are scanned continuously against known "
            "misconfiguration patterns, so drift gets caught between "
            "deploys, not during an incident."
        ),
    },
    {
        "title": "Container Images",
        "desc": (
            "Every image is scanned before it reaches a registry and again "
            "before it reaches production, catching vulnerable base images "
            "and packages introduced anywhere in the build chain."
        ),
    },
    {
        "title": "Cloud Environments",
        "desc": (
            "Cloud account configuration is checked continuously against "
            "compliance and security baselines, giving teams a live "
            "posture view instead of a point-in-time audit."
        ),
    },
]


def render_security_integrations_content():

    cards_html = "".join(
        f"""
        <a class="kf-stage-card" href="/contact" target="_self">
            <div class="kf-card-title">{item['title']}</div>
            <div class="kf-card-desc">{item['desc']}</div>
            <div class="kf-stage-card-link">Talk to us about this &rarr;</div>
        </a>
        """
        for item in _INTEGRATIONS
    )

    st.markdown(
        f"""
        <style>
        .kf-integration-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 22px;
            margin-top: 40px;
        }}
        </style>
        <div class="kf-section">
            <div class="kf-section-label">Integration</div>
            <div class="kf-section-title">Security That Moves at the Speed of Your Pipeline</div>
            <div class="kf-section-body">
                <p>SixStage is designed to sit inside the systems your
                engineering team already runs &mdash; not as a dashboard
                you check once a quarter, but as a continuous layer across
                four surfaces:</p>
            </div>
            <div class="kf-integration-grid">
                {cards_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
