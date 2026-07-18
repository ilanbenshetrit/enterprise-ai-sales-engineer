"""
Security Platform Page — Capability Grid
"""

import streamlit as st


_CAPABILITIES = [
    {
        "n": "01",
        "title": "Kubernetes Security Scanning",
        "desc": (
            "Continuous scanning of cluster configuration, workload "
            "permissions, and exposed services against known "
            "misconfiguration patterns."
        ),
    },
    {
        "n": "02",
        "title": "Dependency &amp; Supply Chain Scanning",
        "desc": (
            "Software composition analysis across dependencies and build "
            "pipelines to catch vulnerable or compromised packages before "
            "they ship."
        ),
    },
    {
        "n": "03",
        "title": "Source &amp; Git History Scanning",
        "desc": (
            "Scans repositories and commit history for exposed credentials "
            "and secrets &mdash; not just the current state of the code, "
            "but everything that ever touched it."
        ),
    },
    {
        "n": "04",
        "title": "Network Exposure Scanning",
        "desc": (
            "Maps network-level attack surface across the environment to "
            "flag exposure that configuration reviews alone tend to miss."
        ),
    },
    {
        "n": "05",
        "title": "Data Security Posture (DSPM)",
        "desc": (
            "Discovers and classifies sensitive data across your stores, "
            "and tracks posture over time instead of a single audit "
            "snapshot."
        ),
    },
    {
        "n": "06",
        "title": "Cloud Security Posture (CSPM)",
        "desc": (
            "Continuously checks cloud configuration against compliance "
            "and security baselines across your provider accounts."
        ),
    },
    {
        "n": "07",
        "title": "AI Security Copilot",
        "desc": (
            "A natural-language interface over every finding &mdash; ask "
            "what changed, why it's risky, and what to do about it, and "
            "get an answer grounded in your actual environment."
        ),
    },
    {
        "n": "08",
        "title": "Automated Alerting &amp; Scheduling",
        "desc": (
            "Scans run on a schedule and on pipeline triggers, with new "
            "risk pushed straight to Slack the moment it's detected."
        ),
    },
]


def render_security_capabilities():

    cards_html = "".join(
        f"""
        <div class="kf-card">
            <div class="kf-card-number">{c['n']}</div>
            <div class="kf-card-title">{c['title']}</div>
            <div class="kf-card-desc">{c['desc']}</div>
        </div>
        """
        for c in _CAPABILITIES
    )

    st.markdown(
        f"""
        <div class="kf-section">
            <div class="kf-section-label">Platform Capabilities</div>
            <div class="kf-section-title">Everything Needed to Secure Cloud-Native Delivery</div>
            <div class="kf-card-grid">
                {cards_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
