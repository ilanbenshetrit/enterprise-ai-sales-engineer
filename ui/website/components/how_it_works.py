"""
How to Become a SixStage Customer — Hybrid SaaS Explainer

Explains the Hybrid SaaS delivery model (cloud control plane + on-premise
agent) and walks through the actual customer journey from registration
to a live, isolated workspace, using the real Stage 12 tenant API.
"""

import streamlit as st


_JOURNEY = [
    {
        "n": "01",
        "title": "Register Your Organization",
        "desc": (
            "Give us your organization name, work email, and plan. Takes "
            "one form &mdash; no credit card required today."
        ),
        "href": "/get-started",
    },
    {
        "n": "02",
        "title": "Get Your API Key Instantly",
        "desc": (
            "Your tenant is created immediately and you receive a live "
            "API key. It's hashed server-side and shown to you exactly "
            "once, so save it right away."
        ),
        "href": "/get-started",
    },
    {
        "n": "03",
        "title": "Connect Your Environment",
        "desc": (
            "Point the on-premise agent at your Kubernetes clusters, "
            "repos, and network using your API key. Scans run locally, "
            "on your infrastructure."
        ),
        "href": "/security-scanning",
    },
    {
        "n": "04",
        "title": "Access Your Live Dashboard",
        "desc": (
            "Findings, posture, and the AI Co-Pilot are all waiting for "
            "you in your own isolated workspace &mdash; the same UI our "
            "team uses internally."
        ),
        "href": "/security-console",
    },
]


def render_how_it_works():

    st.markdown(
        """
        <div class="kf-stage-hero">
            <div class="kf-stage-eyebrow">Become a Customer</div>
            <div class="kf-stage-title">
                How to Become a <span class="gradient-text">SixStage Customer</span>
            </div>
            <div class="kf-stage-desc">
                SixStage runs as a Hybrid SaaS: a cloud control plane you
                access instantly, paired with an on-premise agent that
                keeps your actual code and infrastructure data where it
                belongs &mdash; with you.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="kf-section">
            <div class="kf-section-label">The Hybrid Model</div>
            <div class="kf-section-title">Two Places, One Clear Boundary</div>
            <div class="kf-score-grid" style="grid-template-columns: repeat(2, 1fr); margin-top:36px;">
                <div class="kf-score-card" style="text-align:left;">
                    <span class="kf-tag kf-tag-blue" style="display:inline-block; margin-bottom:14px;">In Our Cloud</span>
                    <div style="font-size:17px; font-weight:800; color:white; margin-bottom:10px;">SaaS Control Plane</div>
                    <div style="font-size:14px; color:rgba(255,255,255,0.75); line-height:1.9;">
                        Dashboard &middot; AI Co-Pilot &middot; Billing &middot;
                        Reports &middot; Alerts &middot; License &amp; tenant
                        management
                    </div>
                </div>
                <div class="kf-score-card" style="text-align:left;">
                    <span class="kf-tag kf-tag-purple" style="display:inline-block; margin-bottom:14px;">On Your Infrastructure</span>
                    <div style="font-size:17px; font-weight:800; color:white; margin-bottom:10px;">On-Premise Agent</div>
                    <div style="font-size:14px; color:rgba(255,255,255,0.75); line-height:1.9;">
                        Kubernetes &middot; file &amp; secrets scanning &middot;
                        network exposure &middot; dependency &amp; CVE
                        scanning &mdash; only findings leave your environment
                    </div>
                </div>
            </div>
            <div class="kf-mock-panel" style="margin-top:28px; text-align:center;">
                <div style="font-size:14px; color:rgba(255,255,255,0.85); line-height:1.7;">
                    &#128274;&nbsp; Your source code, secrets, and raw
                    infrastructure data <b>never leave your environment</b>.
                    Only structured, encrypted security findings are sent
                    to the cloud.
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    cards_html = "".join(
        f"""
        <a class="kf-stage-card" href="{step['href']}" target="_self">
            <div class="kf-card-number">{step['n']}</div>
            <div class="kf-card-title">{step['title']}</div>
            <div class="kf-card-desc">{step['desc']}</div>
            <div class="kf-stage-card-link">Go &rarr;</div>
        </a>
        """
        for step in _JOURNEY
    )

    st.markdown(
        f"""
        <div class="kf-section" style="margin-top:70px;">
            <div class="kf-section-label">Your Path</div>
            <div class="kf-section-title">From Sign-Up to a Live Workspace</div>
            <div class="kf-card-grid" style="margin-top:36px;">
                {cards_html}
            </div>
        </div>
        <div class="kf-cta">
            <div class="kf-cta-title">Ready to See It Running on Your Own Data?</div>
            <div class="kf-cta-desc">
            Create your workspace now &mdash; it takes one form and you're
            issued a live API key immediately.
            </div>
            <a class="kf-cta-button" href="/get-started" target="_self">Get Started</a>
        </div>
        """,
        unsafe_allow_html=True
    )
