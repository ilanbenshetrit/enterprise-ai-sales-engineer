"""
Security Platform Page — Where It Runs
"""

import streamlit as st


_DOMAINS = [
    {
        "title": "CI/CD Pipelines",
        "desc": "Scans run as a pipeline stage, not a separate process.",
    },
    {
        "title": "Kubernetes Clusters",
        "desc": "Cluster and workload configuration, continuously checked.",
    },
    {
        "title": "Container Images",
        "desc": "Docker images scanned before and after they reach production.",
    },
    {
        "title": "Cloud Environments",
        "desc": "Configuration and posture tracked across your cloud accounts.",
    },
]


def render_security_domains():

    cards_html = "".join(
        f"""
        <a class="kf-domain-card" href="/security-integrations" target="_self">
            <div class="kf-domain-title">{d['title']}</div>
            <div class="kf-domain-desc">{d['desc']}</div>
            <div class="kf-domain-link">See integration details &rarr;</div>
        </a>
        """
        for d in _DOMAINS
    )

    st.markdown(
        f"""
        <style>
        .kf-domain-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-top: 40px;
        }}
        .kf-domain-card {{
            display: block;
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 14px;
            padding: 22px;
            text-decoration: none;
            color: inherit;
            transition: 0.3s;
        }}
        .kf-domain-card:hover {{
            transform: translateY(-6px);
            border-color: rgba(56,189,248,0.4);
        }}
        .kf-domain-title {{
            font-size: 15px;
            font-weight: 700;
            color: #38bdf8;
            margin-bottom: 8px;
        }}
        .kf-domain-desc {{
            font-size: 14px;
            line-height: 1.6;
            color: rgba(255,255,255,0.68);
        }}
        .kf-domain-link {{
            margin-top: 14px;
            font-size: 12px;
            font-weight: 600;
            color: #38bdf8;
        }}
        </style>
        <div class="kf-panel">
            <div class="kf-section" style="margin-top: 90px; margin-bottom: 90px;">
                <div class="kf-section-label">Where It Runs</div>
                <div class="kf-section-title">Built Into the Systems You Already Use</div>
                <div class="kf-domain-grid">
                    {cards_html}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
