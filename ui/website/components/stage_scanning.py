"""
Security Platform — Stage 01 Detail: Continuous Scanning
"""

import streamlit as st


_SCANNERS = [
    {
        "n": "01",
        "title": "Kubernetes Security Scanning",
        "desc": (
            "Cluster configuration, workload permissions, and exposed "
            "services checked continuously against known misconfiguration "
            "patterns."
        ),
    },
    {
        "n": "02",
        "title": "Dependency & Supply Chain Scanning",
        "desc": (
            "Software composition analysis across dependencies and build "
            "pipelines, catching vulnerable or compromised packages before "
            "they ship."
        ),
    },
    {
        "n": "03",
        "title": "Source & Git History Scanning",
        "desc": (
            "Repositories and full commit history scanned for exposed "
            "credentials and secrets &mdash; not just the current state of "
            "the code."
        ),
    },
    {
        "n": "04",
        "title": "Network Exposure Scanning",
        "desc": (
            "Network-level attack surface mapped across the environment to "
            "flag exposure that configuration review alone tends to miss."
        ),
    },
]

_FINDINGS = [
    {
        "main": "prod-cluster-eks &middot; workload/payments-api",
        "sub": "Kubernetes Security Scanning &middot; excessive RBAC permissions",
        "tag": "New",
        "tag_class": "kf-tag-blue",
    },
    {
        "main": "requirements.txt &middot; urllib3==1.26.4",
        "sub": "Dependency Scanning &middot; known CVE in a transitive dependency",
        "tag": "Reviewed",
        "tag_class": "kf-tag-purple",
    },
    {
        "main": "infra/terraform &middot; commit a3f9e21",
        "sub": "Git History Scanning &middot; credential pattern in an old commit",
        "tag": "Reviewed",
        "tag_class": "kf-tag-purple",
    },
    {
        "main": "staging-vpc &middot; load-balancer-01",
        "sub": "Network Exposure Scanning &middot; publicly reachable admin port",
        "tag": "New",
        "tag_class": "kf-tag-blue",
    },
]


def render_stage_scanning():

    cards_html = "".join(
        f"""
        <a class="kf-stage-card" href="/security-posture" target="_self">
            <div class="kf-card-number">{s['n']}</div>
            <div class="kf-card-title">{s['title']}</div>
            <div class="kf-card-desc">{s['desc']}</div>
            <div class="kf-stage-card-link">See how findings are scored &rarr;</div>
        </a>
        """
        for s in _SCANNERS
    )

    rows_html = "".join(
        f"""
        <div class="kf-mock-row">
            <div>
                <div class="kf-mock-main">{f['main']}</div>
                <div class="kf-mock-sub">{f['sub']}</div>
            </div>
            <div class="kf-tag {f['tag_class']}">{f['tag']}</div>
        </div>
        """
        for f in _FINDINGS
    )

    st.markdown(
        f"""
        <a class="kf-stage-back" href="/security" target="_self">&larr; Back to Security Platform</a>
        <div class="kf-stage-hero">
            <div class="kf-stage-eyebrow">Stage 01 &middot; Continuous Scanning</div>
            <div class="kf-stage-title">
                Four scanners, <span class="gradient-text">one continuous view</span>
            </div>
            <div class="kf-stage-desc">
                KubeForge runs on a schedule and on every pipeline trigger,
                covering the surfaces where risk actually shows up:
                Kubernetes, dependencies, source history, and network
                exposure. Nothing waits for a quarterly audit.
            </div>
        </div>
        <div class="kf-section">
            <div class="kf-card-grid">
                {cards_html}
            </div>
            <div class="kf-mock-panel">
                <div class="kf-mock-panel-label">Sample Findings</div>
                {rows_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
