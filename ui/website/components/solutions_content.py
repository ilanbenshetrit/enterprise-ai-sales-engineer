"""
Kubeforge Solutions Page Content
"""

import streamlit as st

from components.icons import (
    ICON_OPPORTUNITY,
    ICON_KNOWLEDGE,
    ICON_AUTOMATION,
    ICON_ARCHITECTURE,
    ICON_AGENTS,
    ICON_PACKAGE,
)


_SOLUTIONS = [
    {
        "icon": ICON_OPPORTUNITY,
        "title": "Financial Services",
        "desc": (
            "Automate KYC-heavy discovery, architect compliant hybrid-cloud "
            "solutions, and generate audit-ready proposals for regulated "
            "banking and capital markets deals."
        ),
    },
    {
        "icon": ICON_KNOWLEDGE,
        "title": "Healthcare & Life Sciences",
        "desc": (
            "Navigate HIPAA and data-residency constraints automatically "
            "while designing architectures for clinical, research, and "
            "patient-data workloads."
        ),
    },
    {
        "icon": ICON_AUTOMATION,
        "title": "Manufacturing & Supply Chain",
        "desc": (
            "Plan automation projects across OT and IT boundaries &mdash; "
            "from plant-floor integration to end-to-end supply chain "
            "visibility."
        ),
    },
    {
        "icon": ICON_ARCHITECTURE,
        "title": "Public Sector",
        "desc": (
            "Meet procurement and security accreditation requirements from "
            "the first discovery call, with architecture recommendations "
            "built for government compliance frameworks."
        ),
    },
    {
        "icon": ICON_AGENTS,
        "title": "Insurance",
        "desc": (
            "Accelerate claims and underwriting automation opportunities "
            "with POC plans scoped around measurable loss-ratio and "
            "cycle-time outcomes."
        ),
    },
    {
        "icon": ICON_PACKAGE,
        "title": "Technology & SaaS",
        "desc": (
            "Scope integrations and multi-tenant architecture for platform "
            "and infrastructure deals, from proof-of-concept to production "
            "rollout."
        ),
    },
]


def render_solutions_content():

    cards_html = "".join(
        f"""
        <div class="kf-card">
            <div class="kf-card-icon">{s['icon']}</div>
            <div class="kf-card-title">{s['title']}</div>
            <div class="kf-card-desc">{s['desc']}</div>
        </div>
        """
        for s in _SOLUTIONS
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
