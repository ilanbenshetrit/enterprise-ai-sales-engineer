"""
Homepage Product Grid — Datadog-style big cards with a visual per capability

No stock photos or fake screenshots: each visual is a small CSS mockup
built from the same primitives used on the real product pages, so it's
an honest miniature of what's actually behind the link.
"""

import streamlit as st


def _visual_scanning():
    return """
    <div class="kf-pg-visual">
        <div class="kf-pg-row"><span class="kf-tag kf-tag-purple">Critical</span><span class="kf-pg-line"></span></div>
        <div class="kf-pg-row"><span class="kf-tag kf-tag-blue">High</span><span class="kf-pg-line" style="width:70%;"></span></div>
        <div class="kf-pg-row"><span class="kf-tag kf-tag-muted">Medium</span><span class="kf-pg-line" style="width:50%;"></span></div>
    </div>
    """


def _visual_posture():
    return """
    <div class="kf-pg-visual kf-pg-visual-grid">
        <div class="kf-pg-mini-score"><div class="kf-pg-mini-value gradient-text">86</div><div class="kf-pg-mini-label">DSPM</div></div>
        <div class="kf-pg-mini-score"><div class="kf-pg-mini-value gradient-text">92</div><div class="kf-pg-mini-label">CSPM</div></div>
    </div>
    """


def _visual_copilot():
    return """
    <div class="kf-pg-visual">
        <div class="kf-pg-bubble kf-pg-bubble-user">What changed since Friday?</div>
        <div class="kf-pg-bubble kf-pg-bubble-ai">2 new criticals in prod-eks, both RBAC.</div>
    </div>
    """


def _visual_alerting():
    return """
    <div class="kf-pg-visual">
        <div class="kf-pg-alert-row"><span class="kf-pg-dot"></span>Slack alert sent &middot; 2m ago</div>
        <div class="kf-pg-alert-row"><span class="kf-pg-dot" style="background:#38bdf8;"></span>Scan complete &middot; 41m ago</div>
    </div>
    """


def _visual_ai_security():
    return """
    <div class="kf-pg-visual">
        <div class="kf-pg-row"><span class="kf-tag kf-tag-purple">Prompt Injection</span></div>
        <div class="kf-pg-row"><span class="kf-tag kf-tag-blue">Exposed NHI</span></div>
        <div class="kf-pg-row"><span class="kf-tag kf-tag-muted">MCP Risk</span></div>
    </div>
    """


def _visual_console():
    return """
    <div class="kf-pg-visual kf-pg-browser">
        <div class="kf-pg-browser-bar">
            <span class="kf-pg-browser-dot" style="background:#f87171;"></span>
            <span class="kf-pg-browser-dot" style="background:#fbbf24;"></span>
            <span class="kf-pg-browser-dot" style="background:#34d399;"></span>
        </div>
        <div class="kf-pg-browser-live"><span class="kf-pg-live-dot"></span>LIVE</div>
    </div>
    """


_PRODUCTS = [
    {
        "title": "Continuous Scanning",
        "desc": "Kubernetes, dependencies, secrets, and network exposure — scanned continuously, not once a quarter.",
        "href": "/security-scanning",
        "visual": _visual_scanning,
    },
    {
        "title": "Posture & Risk Analysis",
        "desc": "DSPM and CSPM correlated into one risk view, ranked by actual exposure.",
        "href": "/security-posture",
        "visual": _visual_posture,
    },
    {
        "title": "AI Copilot Triage",
        "desc": "Ask what changed and why it matters — grounded answers, not another dashboard to learn.",
        "href": "/security-copilot",
        "visual": _visual_copilot,
    },
    {
        "title": "Alerting & Remediation",
        "desc": "New risk pushed to Slack the moment it's found, with a full audit trail.",
        "href": "/security-alerting",
        "visual": _visual_alerting,
    },
    {
        "title": "AI & Identity Security",
        "desc": "Prompt injection, exposed machine credentials, and MCP server misconfiguration.",
        "href": "/security-ai",
        "visual": _visual_ai_security,
    },
    {
        "title": "Live Security Console",
        "desc": "Not a mockup — the actual backend, running now, embedded right here.",
        "href": "/security-console",
        "visual": _visual_console,
    },
]


def render_product_grid():

    cards_html = "".join(
        f"""
        <a class="kf-pg-card" href="{p['href']}" target="_self">
            {p['visual']()}
            <div class="kf-pg-title">{p['title']}</div>
            <div class="kf-pg-desc">{p['desc']}</div>
            <div class="kf-pg-link">Learn more &rarr;</div>
        </a>
        """
        for p in _PRODUCTS
    )

    st.markdown(
        f"""
        <style>
        .kf-pg-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 22px;
            margin-top: 40px;
        }}
        .kf-pg-card {{
            display: block;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 18px;
            padding: 22px;
            text-decoration: none;
            transition: 0.3s;
        }}
        .kf-pg-card:hover {{
            transform: translateY(-6px);
            border-color: rgba(56,189,248,0.4);
        }}
        .kf-pg-visual {{
            height: 110px;
            border-radius: 12px;
            background: rgba(0,0,0,0.18);
            padding: 16px;
            margin-bottom: 18px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            gap: 8px;
        }}
        .kf-pg-visual-grid {{
            flex-direction: row;
            justify-content: center;
            gap: 18px;
        }}
        .kf-pg-row {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .kf-pg-line {{
            height: 6px;
            width: 40%;
            border-radius: 4px;
            background: rgba(255,255,255,0.15);
        }}
        .kf-pg-mini-score {{
            text-align: center;
        }}
        .kf-pg-mini-value {{
            font-size: 26px;
            font-weight: 800;
        }}
        .kf-pg-mini-label {{
            font-size: 11px;
            color: rgba(255,255,255,0.55);
            letter-spacing: 1px;
            text-transform: uppercase;
        }}
        .kf-pg-bubble {{
            font-size: 11.5px;
            padding: 7px 12px;
            border-radius: 10px;
            max-width: 82%;
            line-height: 1.4;
        }}
        .kf-pg-bubble-user {{
            align-self: flex-end;
            background: linear-gradient(90deg, #8b5cf6, #38bdf8);
            color: white;
            margin-left: auto;
        }}
        .kf-pg-bubble-ai {{
            background: rgba(255,255,255,0.08);
            color: rgba(255,255,255,0.85);
        }}
        .kf-pg-alert-row {{
            font-size: 12px;
            color: rgba(255,255,255,0.75);
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .kf-pg-dot {{
            width: 7px; height: 7px; border-radius: 50%;
            background: #34d399;
            flex-shrink: 0;
        }}
        .kf-pg-browser {{
            padding: 0;
            overflow: hidden;
            position: relative;
        }}
        .kf-pg-browser-bar {{
            display: flex;
            gap: 6px;
            padding: 10px 14px;
            background: rgba(255,255,255,0.05);
        }}
        .kf-pg-browser-dot {{
            width: 8px; height: 8px; border-radius: 50%;
        }}
        .kf-pg-browser-live {{
            position: absolute;
            top: 42px; left: 0; right: 0; bottom: 0;
            display: flex; align-items: center; justify-content: center;
            gap: 8px;
            color: #34d399;
            font-size: 12px;
            font-weight: 800;
            letter-spacing: 2px;
        }}
        .kf-pg-live-dot {{
            width: 8px; height: 8px; border-radius: 50%;
            background: #34d399;
            animation: kfPulseDot 2s ease-in-out infinite;
        }}
        .kf-pg-title {{
            font-size: 18px;
            font-weight: 800;
            color: white;
            margin-bottom: 8px;
        }}
        .kf-pg-desc {{
            font-size: 13.5px;
            line-height: 1.6;
            color: rgba(255,255,255,0.68);
            margin-bottom: 14px;
        }}
        .kf-pg-link {{
            font-size: 13px;
            font-weight: 700;
            color: #38bdf8;
        }}
        </style>
        <div class="kf-section">
            <div class="kf-section-label">Products</div>
            <div class="kf-section-title">Everything Behind the Live Console</div>
            <div class="kf-pg-grid">
                {cards_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
