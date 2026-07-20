"""
Pricing Page Content — Full 3-Tier Breakdown
"""

import streamlit as st


_PLANS = [
    {
        "name": "Starter",
        "price": "$49",
        "period": "/month",
        "desc": "For a single team getting continuous scanning in place.",
        "features": [
            "1 environment",
            "3 users",
            "Full dashboard",
            "Monthly report",
            "Continuous scanning (K8s, deps, secrets, network)",
        ],
    },
    {
        "name": "Professional",
        "price": "$149",
        "period": "/month",
        "desc": "For teams that need posture, AI triage, and real-time alerts.",
        "features": [
            "3 environments",
            "10 users",
            "AI Co-Pilot",
            "Slack alerts",
            "Everything in Starter",
        ],
        "featured": True,
    },
    {
        "name": "Enterprise",
        "price": "Custom",
        "period": "",
        "desc": "For organizations with compliance, scale, or SSO requirements.",
        "features": [
            "Unlimited environments",
            "SSO (SAML / OIDC)",
            "SLA & priority support",
            "Self-hosted option",
            "Everything in Professional",
        ],
    },
]


def render_pricing_content():

    cards_html = "".join(
        f"""
        <div class="kf-score-card" style="text-align:left; {'border-color: rgba(56,189,248,0.5); background: rgba(56,189,248,0.06);' if p.get('featured') else ''}">
            {'<div class="kf-tag kf-tag-blue" style="display:inline-block; margin-bottom:12px;">Most Popular</div>' if p.get('featured') else ''}
            <div style="font-size:19px; font-weight:800; color:white; margin-bottom:6px;">{p['name']}</div>
            <div style="font-size:13px; color:rgba(255,255,255,0.6); margin-bottom:18px; line-height:1.5;">{p['desc']}</div>
            <div style="margin-bottom:20px;">
                <span style="font-size:32px; font-weight:800; color:white;">{p['price']}</span>
                <span style="font-size:14px; color:rgba(255,255,255,0.6);">{p['period']}</span>
            </div>
            <div style="font-size:13px; color:rgba(255,255,255,0.78); line-height:2.1;">
                {"<br>".join(f"&check;&nbsp; {f}" for f in p['features'])}
            </div>
        </div>
        """
        for p in _PLANS
    )

    st.markdown(
        f"""
        <div class="kf-stage-hero">
            <div class="kf-stage-eyebrow">Pricing</div>
            <div class="kf-stage-title">
                Simple Plans, <span class="gradient-text">No Surprises</span>
            </div>
            <div class="kf-stage-desc">
                Start on Starter, upgrade when you need more environments
                or the AI Co-Pilot, and talk to us directly for Enterprise
                requirements. No credit card required to get your API key
                today.
            </div>
        </div>
        <div class="kf-score-grid" style="grid-template-columns: repeat(3, 1fr); max-width: 920px; margin: 40px auto 0;">
            {cards_html}
        </div>
        <div class="kf-cta">
            <div class="kf-cta-title">Ready to Create Your Workspace?</div>
            <div class="kf-cta-desc">Register in one form and get a live API key instantly.</div>
            <a class="kf-cta-button" href="/get-started" target="_self">Get Started</a>
        </div>
        """,
        unsafe_allow_html=True
    )
