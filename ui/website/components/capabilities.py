"""
Kubeforge Platform Page — Capability Pipeline
"""

import streamlit as st


_STAGES = [
    {
        "n": "01",
        "title": "Opportunity Intelligence",
        "desc": (
            "Kubeforge ingests customer and deal context to surface signal "
            "buried in CRM records, notes, and historical engagement &mdash; "
            "flagging risk, readiness, and where technical effort should "
            "focus first."
        ),
    },
    {
        "n": "02",
        "title": "Architecture Recommendation",
        "desc": (
            "Given a customer's existing stack and requirements, the "
            "platform proposes a tailored technical architecture &mdash; "
            "work that would otherwise take engineers days of manual "
            "research."
        ),
    },
    {
        "n": "03",
        "title": "POC Planning",
        "desc": (
            "Kubeforge scopes proof-of-concept plans automatically: success "
            "criteria, timeline, and resourcing &mdash; so engineers open a "
            "validated plan instead of a blank page."
        ),
    },
    {
        "n": "04",
        "title": "Demo Intelligence",
        "desc": (
            "The platform plans demos tailored to each prospect's "
            "priorities, so every technical walkthrough speaks directly to "
            "what that buyer cares about."
        ),
    },
    {
        "n": "05",
        "title": "Implementation Planning",
        "desc": (
            "Once a deal is won, the platform generates a delivery roadmap "
            "that turns the sales-cycle architecture into an actionable "
            "plan for the delivery team."
        ),
    },
    {
        "n": "06",
        "title": "Solution Package Generation",
        "desc": (
            "Every engagement compiles into a complete solution package "
            "&mdash; architecture, plan, and proposal &mdash; ready to hand "
            "to the customer."
        ),
    },
]


def render_capabilities():

    cards_html = "".join(
        f"""
        <a class="kf-cap-card" href="/demo" target="_self">
            <div class="kf-cap-number">{stage['n']}</div>
            <div class="kf-cap-title">{stage['title']}</div>
            <div class="kf-cap-desc">{stage['desc']}</div>
            <div class="kf-cap-link">View it live &rarr;</div>
        </a>
        """
        for stage in _STAGES
    )

    st.markdown(
        f"""
        <style>
        .kf-section {{
            max-width: 1050px;
            margin: 40px auto 100px;
        }}
        .kf-cap-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 22px;
            margin-top: 40px;
        }}
        .kf-cap-card {{
            display: block;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 18px;
            padding: 30px;
            transition: 0.3s;
            text-decoration: none;
            color: inherit;
        }}
        .kf-cap-card:hover {{
            transform: translateY(-6px);
            border-color: rgba(56,189,248,0.4);
        }}
        .kf-cap-number {{
            font-size: 34px;
            font-weight: 800;
            background: linear-gradient(90deg, #c084fc, #38bdf8, #34d399);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 14px;
            line-height: 1;
        }}
        .kf-cap-title {{
            font-size: 18px;
            font-weight: 700;
            color: white;
            margin-bottom: 10px;
        }}
        .kf-cap-desc {{
            font-size: 14px;
            line-height: 1.7;
            color: rgba(255,255,255,0.68);
        }}
        .kf-cap-link {{
            margin-top: 16px;
            font-size: 13px;
            font-weight: 600;
            color: #38bdf8;
        }}
        .kf-knowledge-band {{
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 18px;
            padding: 30px 32px;
            margin-top: 32px;
        }}
        .kf-knowledge-title {{
            font-size: 17px;
            font-weight: 700;
            color: white;
            margin-bottom: 8px;
        }}
        .kf-knowledge-desc {{
            font-size: 15px;
            line-height: 1.75;
            color: rgba(255,255,255,0.7);
        }}
        </style>
        <div class="kf-section">
            <div class="kf-cap-grid">
                {cards_html}
            </div>
            <div class="kf-knowledge-band">
                <div class="kf-knowledge-title">Built on an Enterprise Knowledge Layer</div>
                <div class="kf-knowledge-desc">
                Every stage above is powered by retrieval-augmented
                reasoning over your own product documentation, prior
                deals, and technical collateral &mdash; so recommendations
                are grounded in your business, not a generic model
                response.
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
