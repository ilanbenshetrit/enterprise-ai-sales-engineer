"""
Docs Page Content — Real Stage 12 Tenant API Reference

Pulled directly from the actual backend implementation, not invented.
"""

import streamlit as st


_ENDPOINTS = [
    {
        "method": "POST",
        "path": "/api/v1/tenants/register",
        "auth": "No",
        "desc": "Register a new organization. Returns an API key exactly once.",
    },
    {
        "method": "GET",
        "path": "/api/v1/tenants/me",
        "auth": "Yes",
        "desc": "Details for the current tenant, resolved from your API key.",
    },
    {
        "method": "GET",
        "path": "/api/v1/history",
        "auth": "Yes",
        "desc": "Recent scans for your tenant only.",
    },
    {
        "method": "POST",
        "path": "/api/v1/scan/trigger",
        "auth": "Yes",
        "desc": "Trigger a scan against a path with a chosen scanner.",
    },
]

_ERRORS = [
    ("201 Created", "Tenant created successfully."),
    ("401 Unauthorized", "API key missing, invalid, or inactive."),
    ("409 Conflict", "That email is already registered."),
    ("422 Unprocessable Entity", "Missing or invalid fields in the request body."),
    ("500 Server Error", "Unexpected error — check server logs."),
]


def render_docs_content():

    st.markdown(
        """
        <div class="kf-stage-hero">
            <div class="kf-stage-eyebrow">Docs</div>
            <div class="kf-stage-title">
                SixStage <span class="gradient-text">API Reference</span>
            </div>
            <div class="kf-stage-desc">
                Every SixStage tenant is isolated by API key. Register once,
                pass your key as <code>X-API-Key</code> on every request,
                and every query is automatically scoped to your data.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="kf-section">
            <div class="kf-section-label">Step 1</div>
            <div class="kf-section-title">Register &amp; Get Your Key</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.code(
        'curl -X POST https://api.sixstage.ai/api/v1/tenants/register \\\n'
        '  -H "Content-Type: application/json" \\\n'
        '  -d \'{"name":"Acme Corp","email":"admin@acme.io","plan":"starter"}\'',
        language="bash",
    )

    st.markdown(
        """
        <div class="kf-section" style="margin-top:50px;">
            <div class="kf-section-label">Step 2</div>
            <div class="kf-section-title">Call the API With Your Key</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.code(
        'curl https://api.sixstage.ai/api/v1/history \\\n'
        '  -H "X-API-Key: sk-live-xxxxxxxxxxxx"',
        language="bash",
    )

    rows_html = "".join(
        f"""
        <div class="kf-alert-item">
            <span class="kf-tag kf-tag-blue" style="min-width:64px; text-align:center;">{e['method']}</span>
            <div class="kf-alert-text">
                <code>{e['path']}</code> &mdash; {e['desc']}
                <span style="color:rgba(255,255,255,0.5); font-size:12px;"> (Auth: {e['auth']})</span>
            </div>
        </div>
        """
        for e in _ENDPOINTS
    )

    st.markdown(
        f"""
        <div class="kf-section" style="margin-top:50px;">
            <div class="kf-section-label">Endpoints</div>
            <div class="kf-section-title">Core Tenant &amp; Scan API</div>
            <div class="kf-alert-list">
                {rows_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    error_rows = "".join(
        f"""
        <div style="display:flex; gap:16px; padding:12px 0; border-bottom:1px solid rgba(255,255,255,0.08);">
            <div style="width:200px; flex-shrink:0; font-weight:700; color:#38bdf8; font-size:13px;">{code}</div>
            <div style="font-size:13px; color:rgba(255,255,255,0.75);">{meaning}</div>
        </div>
        """
        for code, meaning in _ERRORS
    )

    st.markdown(
        f"""
        <div class="kf-section" style="margin-top:50px;">
            <div class="kf-section-label">Status Codes</div>
            <div class="kf-section-title">What Each Response Means</div>
            <div style="margin-top:20px;">
                {error_rows}
            </div>
        </div>
        <div class="kf-cta">
            <div class="kf-cta-title">Don't Have a Key Yet?</div>
            <div class="kf-cta-desc">Registration takes one form and returns a live key instantly.</div>
            <a class="kf-cta-button" href="/get-started" target="_self">Get Started</a>
        </div>
        """,
        unsafe_allow_html=True
    )
