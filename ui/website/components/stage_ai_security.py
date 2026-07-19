"""
Security Platform — Stage 11 Detail: AI & Identity Security

Covers the three newest scanners: AI workload risks (prompt injection,
unsafe model loading, vector DB exposure), Non-Human Identity (NHI)
credential exposure, and MCP server misconfiguration &mdash; the newest
attack surface, born alongside AI coding assistants in 2024-2025.
"""

import streamlit as st


_FINDINGS = [
    {
        "tag": "Critical",
        "tag_class": "kf-tag-purple",
        "text": (
            "<b>Prompt Injection</b> &mdash; unsanitized user input passed "
            "directly into an LLM prompt in <b>support-bot/handler.py</b>."
        ),
    },
    {
        "tag": "High",
        "tag_class": "kf-tag-blue",
        "text": (
            "<b>Exposed NHI</b> &mdash; GitHub Personal Access Token "
            "hardcoded in <b>.github/workflows/deploy.yml</b>."
        ),
    },
    {
        "tag": "High",
        "tag_class": "kf-tag-blue",
        "text": (
            "<b>Unsafe Model Loading</b> &mdash; <code>torch.load()</code> "
            "called without <code>weights_only=True</code> in "
            "<b>inference/load_model.py</b>."
        ),
    },
    {
        "tag": "Medium",
        "tag_class": "kf-tag-muted",
        "text": (
            "<b>MCP Filesystem Risk</b> &mdash; Claude Desktop config grants "
            "root filesystem access to a local MCP server."
        ),
    },
    {
        "tag": "Medium",
        "tag_class": "kf-tag-muted",
        "text": (
            "<b>Vector DB Without Auth</b> &mdash; Chroma instance reachable "
            "with no authentication configured."
        ),
    },
]

_AREAS = [
    {
        "n": "01",
        "title": "AI Workload Scanner",
        "desc": (
            "Scans code and infrastructure for LLM-specific risk: prompt "
            "injection, unsafe model loading, unauthenticated vector "
            "databases, hardcoded LLM API keys, and unpinned model "
            "versions."
        ),
    },
    {
        "n": "02",
        "title": "Non-Human Identity (NHI) Scanner",
        "desc": (
            "Finds exposed machine credentials &mdash; cloud access keys, "
            "SSH and TLS private keys, CI/CD tokens, and hardcoded "
            "database connection strings &mdash; the identities behind "
            "most breaches that aren't a person."
        ),
    },
    {
        "n": "03",
        "title": "MCP Server Scanner",
        "desc": (
            "Audits Model Context Protocol configurations used by AI "
            "coding assistants &mdash; Claude Desktop, Cursor, VS Code "
            "Copilot &mdash; for unrestricted filesystem access, secrets "
            "in plaintext, and data flowing to untrusted endpoints."
        ),
    },
    {
        "n": "04",
        "title": "First-to-Market Coverage",
        "desc": (
            "MCP servers are a new attack surface with almost no existing "
            "tooling. SixStage is among the first security platforms "
            "scanning for this class of risk."
        ),
    },
]


def render_stage_ai_security():

    findings_html = "".join(
        f"""
        <div class="kf-alert-item">
            <span class="kf-tag {f['tag_class']}">{f['tag']}</span>
            <div class="kf-alert-text">{f['text']}</div>
        </div>
        """
        for f in _FINDINGS
    )

    cards_html = "".join(
        f"""
        <a class="kf-stage-card" href="/security-console" target="_self">
            <div class="kf-card-number">{a['n']}</div>
            <div class="kf-card-title">{a['title']}</div>
            <div class="kf-card-desc">{a['desc']}</div>
            <div class="kf-stage-card-link">Try it in the Live Console &rarr;</div>
        </a>
        """
        for a in _AREAS
    )

    st.markdown(
        f"""
        <a class="kf-stage-back" href="/security" target="_self">&larr; Back to Security Platform</a>
        <div class="kf-stage-hero">
            <div class="kf-stage-eyebrow">Stage 11 &middot; AI &amp; Identity Security</div>
            <div class="kf-stage-title">
                Securing the <span class="gradient-text">newest attack surface</span>
            </div>
            <div class="kf-stage-desc">
                AI workloads and the machine identities behind them are the
                fastest-growing part of the attack surface, and the least
                covered by existing tools. SixStage scans for LLM-specific
                risk, exposed non-human credentials, and MCP server
                misconfiguration &mdash; all in the same pipeline as the
                rest of the platform.
            </div>
        </div>
        <div class="kf-section">
            <div class="kf-alert-list">
                {findings_html}
            </div>
            <div class="kf-card-grid" style="margin-top: 60px;">
                {cards_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
