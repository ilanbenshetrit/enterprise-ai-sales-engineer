"""
Security Platform — Stage 04 Detail: Alerting & Remediation
"""

import streamlit as st


_ALERTS = [
    {
        "time": "2 min ago",
        "text": (
            "<b>Critical &middot; RBAC</b> &mdash; over-permissioned role "
            "detected on <b>payments-api</b> in prod-cluster-eks. Posted to "
            "#security-alerts."
        ),
    },
    {
        "time": "41 min ago",
        "text": (
            "<b>Scheduled scan complete</b> &mdash; supply chain scan "
            "finished for 14 repositories, 2 new dependency findings."
        ),
    },
    {
        "time": "3 hr ago",
        "text": (
            "<b>Remediated</b> &mdash; exposed admin port on "
            "load-balancer-01 closed and re-scanned clean."
        ),
    },
    {
        "time": "yesterday",
        "text": (
            "<b>Pipeline gate</b> &mdash; build #4021 blocked after a "
            "critical CVE was introduced in a new dependency."
        ),
    },
]

_AREAS = [
    {
        "n": "01",
        "title": "Scheduled Scans",
        "desc": (
            "Scans run on a recurring schedule in the background, so "
            "posture stays current even between deploys."
        ),
    },
    {
        "n": "02",
        "title": "Instant Slack Alerts",
        "desc": (
            "New risk is pushed straight to the team's existing channels "
            "the moment it's detected &mdash; no separate dashboard to "
            "remember to check."
        ),
    },
    {
        "n": "03",
        "title": "Pipeline Gating",
        "desc": (
            "Builds can be configured to fail on newly introduced critical "
            "risk, the same gate teams already use for tests and linting."
        ),
    },
    {
        "n": "04",
        "title": "Remediation & Audit Trail",
        "desc": (
            "Every finding, alert, and fix is tracked end to end, giving "
            "teams a clear record of what was found and what was done "
            "about it."
        ),
    },
]


def render_stage_alerting():

    alerts_html = "".join(
        f"""
        <div class="kf-alert-item">
            <div class="kf-alert-time">{a['time']}</div>
            <div class="kf-alert-text">{a['text']}</div>
        </div>
        """
        for a in _ALERTS
    )

    cards_html = "".join(
        f"""
        <a class="kf-stage-card" href="/security-integrations" target="_self">
            <div class="kf-card-number">{a['n']}</div>
            <div class="kf-card-title">{a['title']}</div>
            <div class="kf-card-desc">{a['desc']}</div>
            <div class="kf-stage-card-link">See it wired into your pipeline &rarr;</div>
        </a>
        """
        for a in _AREAS
    )

    st.markdown(
        f"""
        <a class="kf-stage-back" href="/security" target="_self">&larr; Back to Security Platform</a>
        <div class="kf-stage-hero">
            <div class="kf-stage-eyebrow">Stage 04 &middot; Alerting &amp; Remediation</div>
            <div class="kf-stage-title">
                From detection to <span class="gradient-text">action, closed loop</span>
            </div>
            <div class="kf-stage-desc">
                Findings don't sit in a dashboard waiting to be noticed.
                SixStage pushes risk to the team the moment it's found,
                and can gate a pipeline outright when the risk is critical.
            </div>
        </div>
        <div class="kf-section">
            <div class="kf-alert-list">
                {alerts_html}
            </div>
            <div class="kf-card-grid" style="margin-top: 60px;">
                {cards_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
