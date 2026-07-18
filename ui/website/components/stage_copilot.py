"""
Security Platform — Stage 03 Detail: AI Copilot Triage
"""

import streamlit as st


_CHAT = [
    {"role": "user", "text": "What changed in prod-cluster-eks in the last 24 hours?"},
    {
        "role": "ai",
        "text": (
            "Two new findings: an over-permissioned RBAC role on "
            "<b>payments-api</b> and a newly exposed admin port on "
            "<b>load-balancer-01</b>. The RBAC issue is the higher "
            "priority &mdash; it grants cluster-wide write access that "
            "wasn't present in yesterday's scan."
        ),
    },
    {"role": "user", "text": "Why does that RBAC change matter more than the exposed port?"},
    {
        "role": "ai",
        "text": (
            "The exposed port is reachable but requires valid "
            "credentials. The RBAC change means a single compromised pod "
            "in that namespace could now modify workloads cluster-wide "
            "&mdash; it widens the blast radius of any other issue you "
            "have open."
        ),
    },
]

_AREAS = [
    {
        "n": "01",
        "title": "Natural Language Q&amp;A",
        "desc": (
            "Engineers ask questions in plain language instead of writing "
            "queries by hand &mdash; \"what changed,\" \"what's the "
            "riskiest thing open right now.\""
        ),
    },
    {
        "n": "02",
        "title": "Grounded Answers",
        "desc": (
            "Every answer is grounded in the actual scan data for your "
            "environment, not a generic model response disconnected from "
            "what's really running."
        ),
    },
    {
        "n": "03",
        "title": "Structured Query Assistant",
        "desc": (
            "A SQL-aware assistant lets teams ask precise, structured "
            "questions over historical findings when a conversational "
            "answer isn't specific enough."
        ),
    },
    {
        "n": "04",
        "title": "Prioritized Recommendations",
        "desc": (
            "The copilot doesn't just list findings &mdash; it reasons "
            "about which ones compound each other and recommends what to "
            "fix first."
        ),
    },
]


def render_stage_copilot():

    chat_html = "".join(
        f"""<div class="kf-chat-bubble {'kf-chat-user' if turn['role'] == 'user' else 'kf-chat-ai'}">{turn['text']}</div>"""
        for turn in _CHAT
    )

    cards_html = "".join(
        f"""
        <a class="kf-stage-card" href="/security-alerting" target="_self">
            <div class="kf-card-number">{a['n']}</div>
            <div class="kf-card-title">{a['title']}</div>
            <div class="kf-card-desc">{a['desc']}</div>
            <div class="kf-stage-card-link">See how this reaches your team &rarr;</div>
        </a>
        """
        for a in _AREAS
    )

    st.markdown(
        f"""
        <a class="kf-stage-back" href="/security" target="_self">&larr; Back to Security Platform</a>
        <div class="kf-stage-hero">
            <div class="kf-stage-eyebrow">Stage 03 &middot; AI Copilot Triage</div>
            <div class="kf-stage-title">
                Ask your posture data <span class="gradient-text">a question</span>
            </div>
            <div class="kf-stage-desc">
                The same reasoning discipline behind Kubeforge's AI Sales
                Engineer applies here: a copilot grounded in your real
                findings, able to explain what changed and why it matters.
            </div>
        </div>
        <div class="kf-section">
            <div class="kf-chat-panel">
                {chat_html}
            </div>
            <div class="kf-card-grid" style="margin-top: 60px;">
                {cards_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
