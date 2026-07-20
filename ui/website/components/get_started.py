"""
Get Started — Self-Serve Tenant Registration

Calls the real SixStage backend's Stage 12 Multi-Tenant API
(POST /api/v1/tenants/register) to create an actual, isolated tenant
and return a live API key &mdash; not a mockup form. Gated behind a
server-side health check, same pattern as the Live Security Console.
"""

import streamlit as st
import requests

SECURITY_BACKEND_URL = "http://localhost:8080"

_PLANS = [
    {
        "id": "starter",
        "name": "Starter",
        "price": "$49",
        "period": "/month",
        "features": [
            "1 environment",
            "3 users",
            "Dashboard",
            "Monthly report",
        ],
    },
    {
        "id": "professional",
        "name": "Professional",
        "price": "$149",
        "period": "/month",
        "features": [
            "3 environments",
            "10 users",
            "AI Co-Pilot",
            "Slack alerts",
        ],
        "featured": True,
    },
]


def _backend_is_reachable() -> bool:
    try:
        r = requests.get(f"{SECURITY_BACKEND_URL}/health", timeout=1.5)
        return r.status_code == 200
    except requests.exceptions.RequestException:
        return False


def _register_tenant(name: str, email: str, plan: str):
    try:
        r = requests.post(
            f"{SECURITY_BACKEND_URL}/api/v1/tenants/register",
            json={"name": name, "email": email, "plan": plan},
            timeout=8,
        )
        if r.status_code == 201:
            return {"ok": True, "data": r.json()}
        if r.status_code == 409:
            return {"ok": False, "error": "That email is already registered. Use the Live Console with your existing API key, or contact us to recover access."}
        if r.status_code == 422:
            return {"ok": False, "error": "Please fill in a valid organization name and email address."}
        return {"ok": False, "error": f"Unexpected response from the server ({r.status_code}). Please try again."}
    except requests.exceptions.RequestException:
        return {"ok": False, "error": "Could not reach the registration server. Please try again in a moment."}


def _render_plan_cards():

    cards_html = "".join(
        f"""
        <div class="kf-score-card" style="text-align:left; {'border-color: rgba(56,189,248,0.5); background: rgba(56,189,248,0.06);' if p.get('featured') else ''}">
            {'<div class="kf-tag kf-tag-blue" style="display:inline-block; margin-bottom:12px;">Most Popular</div>' if p.get('featured') else ''}
            <div style="font-size:18px; font-weight:800; color:white; margin-bottom:4px;">{p['name']}</div>
            <div style="margin-bottom:16px;">
                <span style="font-size:28px; font-weight:800; color:white;">{p['price']}</span>
                <span style="font-size:13px; color:rgba(255,255,255,0.6);">{p['period']}</span>
            </div>
            <div style="font-size:13px; color:rgba(255,255,255,0.75); line-height:2;">
                {"<br>".join(f"&check;&nbsp; {f}" for f in p['features'])}
            </div>
        </div>
        """
        for p in _PLANS
    )

    st.markdown(
        f"""
        <div class="kf-score-grid" style="grid-template-columns: repeat(2, 1fr); max-width: 620px; margin-left:auto; margin-right:auto;">
            {cards_html}
        </div>
        <div style="text-align:center; margin-top:18px; font-size:13px; color:rgba(255,255,255,0.55);">
            Need Enterprise &mdash; unlimited environments, SSO, SLA?
            <a href="/contact" target="_self" style="color:#38bdf8; font-weight:600;">Talk to us &rarr;</a>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_get_started():

    st.markdown(
        """
        <style>
        [data-testid="stTextInput"] input,
        [data-testid="stSelectbox"] > div > div {
            background: rgba(255,255,255,0.06) !important;
            border: 1px solid rgba(255,255,255,0.15) !important;
            color: white !important;
            border-radius: 10px !important;
        }
        [data-testid="stTextInput"] label p,
        [data-testid="stSelectbox"] label p {
            color: rgba(255,255,255,0.75) !important;
        }
        [data-testid="stFormSubmitButton"] button {
            background: linear-gradient(90deg,#8b5cf6,#38bdf8,#34d399) !important;
            color: white !important;
            border: none !important;
            border-radius: 14px !important;
            padding: 10px 30px !important;
            font-weight: 600 !important;
            width: 100%;
        }
        </style>
        <div class="kf-stage-hero">
            <div class="kf-stage-eyebrow">Get Started</div>
            <div class="kf-stage-title">
                Create Your <span class="gradient-text">SixStage Workspace</span>
            </div>
            <div class="kf-stage-desc">
                Register your organization and get a live, isolated tenant on
                the real SixStage backend &mdash; instantly. Your data, scans,
                and findings stay fully separated from every other customer.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    _render_plan_cards()

    reachable = _backend_is_reachable()

    result = st.session_state.get("kf_tenant_result")

    if result and result.get("ok"):
        data = result["data"]
        st.markdown(
            f"""
            <div class="kf-mock-panel" style="margin-top:40px; max-width:620px; margin-left:auto; margin-right:auto;">
                <div class="kf-mock-panel-label">Workspace Created</div>
                <div style="font-size:14px; color:rgba(255,255,255,0.85); margin-bottom:18px;">
                    Organization: <b>{data.get('name', '')}</b> &middot; Plan: <b>{data.get('plan', '')}</b>
                </div>
                <div style="font-size:12px; color:#fca5a5; font-weight:700; letter-spacing:1px; text-transform:uppercase; margin-bottom:8px;">
                    &#9888; Save this API key now &mdash; it will not be shown again
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.code(data.get("api_key", ""), language=None)
        st.markdown(
            f"""
            <div style="max-width:620px; margin:8px auto 0; font-size:13px; color:rgba(255,255,255,0.65); line-height:1.8;">
                Tenant ID: <code>{data.get('tenant_id', '')}</code><br>
                Pass this key as the <code>X-API-Key</code> header on every API
                request, or use it to sign in to the
                <a href="/security-console" target="_self" style="color:#38bdf8;">Live Security Console</a>.
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Register another organization"):
            st.session_state["kf_tenant_result"] = None
            st.rerun()

    elif not reachable:
        st.markdown(
            """
            <div class="kf-mock-panel" style="padding:36px; text-align:center; margin-top:40px; max-width:620px; margin-left:auto; margin-right:auto;">
                <div class="kf-mock-panel-label" style="padding:0 0 14px;">Registration Server Not Reachable</div>
                <div class="kf-stage-desc" style="max-width:480px; margin:0 auto;">
                    Signup connects to the live SixStage backend, which isn't
                    reachable right now. Start it locally, then reload this page.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        with st.form("kf_get_started_form"):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Organization name")
            with col2:
                email = st.text_input("Work email")
            plan = st.selectbox("Plan", options=["starter", "professional"], format_func=lambda p: p.capitalize())
            submitted = st.form_submit_button("Create My Workspace")

            if submitted:
                if not name.strip() or "@" not in email:
                    st.error("Please enter an organization name and a valid email address.")
                else:
                    outcome = _register_tenant(name.strip(), email.strip(), plan)
                    if outcome["ok"]:
                        st.session_state["kf_tenant_result"] = outcome
                        st.rerun()
                    else:
                        st.error(outcome["error"])

        st.markdown(
            """
            <div style="text-align:center; margin-top:14px; font-size:12px; color:rgba(255,255,255,0.5);">
                No credit card required today &mdash; billing is being wired up next.
                You're securing early access to your workspace and API key now.
            </div>
            """,
            unsafe_allow_html=True
        )
