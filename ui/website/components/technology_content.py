"""
Kubeforge Technology Page Content
"""

import streamlit as st

from components.icons import (
    ICON_AGENTS,
    ICON_KNOWLEDGE,
    ICON_ARCHITECTURE,
    ICON_SECURITY,
)


_LAYERS = [
    {
        "icon": ICON_AGENTS,
        "title": "Reasoning & Agent Orchestration",
        "desc": (
            "A coordinated set of specialized agents &mdash; reasoning, "
            "architecture, planning, and proposal generation &mdash; each "
            "responsible for one stage of the pipeline, with a shared "
            "context passed between them."
        ),
    },
    {
        "icon": ICON_KNOWLEDGE,
        "title": "Enterprise Knowledge Layer",
        "desc": (
            "Retrieval over your own product documentation, prior deals, "
            "and technical collateral, built on embeddings, a vector "
            "store, and similarity-ranked retrieval &mdash; so answers are "
            "grounded in your business."
        ),
    },
    {
        "icon": ICON_ARCHITECTURE,
        "title": "Architecture & Planning Engines",
        "desc": (
            "Purpose-built engines for architecture recommendation, POC "
            "scoping, implementation planning, and demo planning &mdash; "
            "each modeled on how experienced solution engineers actually "
            "work."
        ),
    },
    {
        "icon": ICON_SECURITY,
        "title": "Security & Governance",
        "desc": (
            "Every recommendation is auditable and reviewable. Data stays "
            "inside your environment, and every automated step keeps a "
            "human in the loop before it reaches the customer."
        ),
    },
]


def render_technology_content():

    cards_html = "".join(
        f"""
        <div class="kf-card">
            <div class="kf-card-icon">{layer['icon']}</div>
            <div class="kf-card-title">{layer['title']}</div>
            <div class="kf-card-desc">{layer['desc']}</div>
        </div>
        """
        for layer in _LAYERS
    )

    st.markdown(
        f"""
        <style>
        .kf-tech-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 22px;
            margin-top: 40px;
        }}
        </style>
        <div class="kf-section">
            <div class="kf-section-label">Technology</div>
            <div class="kf-section-title">Built for Production, Not Demos</div>
            <div class="kf-section-body">
                <p>Kubeforge is engineered as infrastructure, not a single
                prompt. The platform is organized into four layers that
                work together on every opportunity:</p>
            </div>
            <div class="kf-tech-grid">
                {cards_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
