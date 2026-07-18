"""
SixStage Technology Page Content
"""

import streamlit as st


_LAYERS = [
    {
        "n": "01",
        "title": "Reasoning &amp; Agent Orchestration",
        "desc": (
            "A coordinated set of specialized agents &mdash; reasoning, "
            "architecture, planning, and proposal generation &mdash; each "
            "responsible for one stage of the pipeline, with a shared "
            "context passed between them."
        ),
    },
    {
        "n": "02",
        "title": "Enterprise Knowledge Layer",
        "desc": (
            "Retrieval over your own product documentation, prior deals, "
            "and technical collateral, built on embeddings, a vector "
            "store, and similarity-ranked retrieval &mdash; so answers are "
            "grounded in your business."
        ),
    },
    {
        "n": "03",
        "title": "Architecture &amp; Planning Engines",
        "desc": (
            "Purpose-built engines for architecture recommendation, POC "
            "scoping, implementation planning, and demo planning &mdash; "
            "each modeled on how experienced solution engineers actually "
            "work."
        ),
    },
    {
        "n": "04",
        "title": "Security &amp; Governance",
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
            <div class="kf-card-number">{layer['n']}</div>
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
                <p>SixStage is engineered as infrastructure, not a single
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
