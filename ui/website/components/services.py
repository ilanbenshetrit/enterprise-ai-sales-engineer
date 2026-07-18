"""
Kubeforge Services / What We Do Section
"""

import streamlit as st


_SERVICES = [
    {
        "n": "01",
        "title": "Intelligent Process Automation",
        "desc": (
            "We re-architect manual, document-heavy, and decision-intensive "
            "workflows into automated pipelines powered by large language "
            "models, retrieval-augmented reasoning, and domain-specific "
            "agents &mdash; cutting processing time from days to minutes."
        ),
    },
    {
        "n": "02",
        "title": "Autonomous Agent Orchestration",
        "desc": (
            "We design multi-agent systems that plan, execute, and "
            "self-correct across complex enterprise tasks &mdash; from "
            "opportunity intelligence to implementation planning &mdash; "
            "with full auditability and human-in-the-loop controls."
        ),
    },
    {
        "n": "03",
        "title": "Enterprise Knowledge Systems",
        "desc": (
            "We build secure retrieval and knowledge infrastructure that "
            "lets AI reason over an organization's proprietary data "
            "&mdash; contracts, technical documentation, historical deals "
            "&mdash; without that data ever leaving their environment."
        ),
    },
    {
        "n": "04",
        "title": "Custom AI Architecture &amp; Advisory",
        "desc": (
            "For organizations building their own AI capability, we design "
            "the underlying architecture: model selection, evaluation "
            "frameworks, security boundaries, and integration patterns "
            "tailored to their existing technology stack."
        ),
    },
]


def render_services():

    cards_html = "".join(
        f"""
        <div class="kf-service-card">
            <div class="kf-card-number">{s['n']}</div>
            <div class="kf-service-title">{s['title']}</div>
            <div class="kf-service-desc">{s['desc']}</div>
        </div>
        """
        for s in _SERVICES
    )

    st.markdown(
        f"""
        <style>
        .kf-services-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 24px;
            margin-top: 40px;
        }}
        .kf-service-card {{
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 18px;
            padding: 32px;
            transition: 0.3s;
        }}
        .kf-service-card:hover {{
            transform: translateY(-6px);
            border-color: rgba(56,189,248,0.4);
        }}
        .kf-service-title {{
            font-size: 20px;
            font-weight: 700;
            color: white;
            margin-bottom: 12px;
        }}
        .kf-service-desc {{
            font-size: 15px;
            line-height: 1.75;
            color: rgba(255,255,255,0.7);
        }}
        .kf-industries {{
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin-top: 40px;
        }}
        .kf-industry-tag {{
            padding: 8px 18px;
            border-radius: 999px;
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.12);
            color: rgba(255,255,255,0.85);
            font-size: 14px;
        }}
        </style>
        <div class="kf-section">
            <div class="kf-section-label">What We Do</div>
            <div class="kf-section-title">Enterprise AI Automation, Engineered for Production</div>
            <div class="kf-section-body">
                <p>Today, Kubeforge designs, builds, and operates AI automation
                systems for enterprises that need more than a proof of concept.
                Our work spans four core disciplines:</p>
            </div>
            <div class="kf-services-grid">
                {cards_html}
            </div>
            <div class="kf-industries">
                <div class="kf-industry-tag">Financial Services</div>
                <div class="kf-industry-tag">Healthcare &amp; Life Sciences</div>
                <div class="kf-industry-tag">Manufacturing &amp; Supply Chain</div>
                <div class="kf-industry-tag">Public Sector</div>
                <div class="kf-industry-tag">Insurance</div>
                <div class="kf-industry-tag">Technology &amp; SaaS</div>
                <div class="kf-industry-tag">Retail &amp; E-commerce</div>
                <div class="kf-industry-tag">Logistics</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
