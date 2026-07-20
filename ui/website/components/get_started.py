"""
Get Started — Self-Serve Account Signup

Calls the real SixStage backend's Stage 12.2 Auth API
(POST /api/v1/auth/signup) &mdash; backed by Supabase Auth &mdash; to
create an actual account and auto-provision an isolated tenant
workspace. Not a mockup form. Gated behind a server-side health
check, same pattern as the Live Security Console.

Signing in (after the account exists / email is confirmed) happens on
the Live Security Console itself, which has its own Supabase-JS login
screen &mdash; this page only handles account creation.
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


def _signup(email: str, password: str, full_name: str):
    try:
        r = requests.post(
            f"{SECURITY_BACKEND_URL}/api/v1/auth/signup",
            json={"email": email, "password": password, "full_name": full_name},
            timeout=8,
        )
        if r.status_code == 201:
            return {"ok": True, "data": r.json()}
        if r.status_code == 400:
            detail = "That email may already be registered, or the password is too weak. Try a different email or a stronger password."
            try:
                server_detail = r.json().get("detail")
                if server_detail:
                    detail = server_detail
            except ValueError:
                pass
            return {"ok": False, "error": detail}
        if r.status_code == 503:
            return {"ok": False, "error": "Account creation isn't configured on the server yet. Please try again shortly."}
        if r.status_code == 422:
            return {"ok": False, "error": "Please fill in a valid name, email address, and password."}
        return {"ok": False, "error": f"Unexpected response from the server ({r.status_code}). Please try again."}
    except requests.exceptions.RequestException:
        return {"ok": False, "error": "Could not reach the signup server. Please try again in a moment."}


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
            Every new workspace starts on Starter &mdash; plan upgrades and
            billing are being wired up next. Need Enterprise &mdash; unlimited
            environments, SSO, SLA?
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

    result = st.session_state.get("kf_signup_result")

    if result and result.get("ok"):
        data = result["data"]
        confirmed = bool(data.get("confirmed"))

        if confirmed:
            st.markdown(
                f"""
                <div class="kf-mock-panel" style="margin-top:40px; max-width:620px; margin-left:auto; margin-right:auto;">
                    <div class="kf-mock-panel-label">Workspace Created</div>
                    <div style="font-size:14px; color:rgba(255,255,255,0.85); line-height:1.8;">
                        Account: <b>{data.get('email', '')}</b><br>
                        Tenant ID: <code>{data.get('tenant_id', '')}</code>
                    </div>
                </div>
                <div style="max-width:620px; margin:14px auto 0; text-align:center;">
                    <a class="kf-cta-button" href="/security-console" target="_self">Sign In to Your Console &rarr;</a>
                </div>
                <div style="max-width:620px; margin:10px auto 0; font-size:13px; color:rgba(255,255,255,0.6); text-align:center;">
                    Use the email and password you just set &mdash; the Live
                    Security Console signs you in directly.
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div class="kf-mock-panel" style="margin-top:40px; max-width:620px; margin-left:auto; margin-right:auto;">
                    <div class="kf-mock-panel-label">Confirm Your Email</div>
                    <div style="font-size:14px; color:rgba(255,255,255,0.85); line-height:1.8;">
                        We sent a confirmation link to <b>{data.get('email', '')}</b>.
                        Click it, then sign in at the
                        <a href="/security-console" target="_self" style="color:#38bdf8;">Live Security Console</a>
                        with your email and password.
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        if st.button("Create another workspace"):
            st.session_state["kf_signup_result"] = None
            st.rerun()

    elif not reachable:
        st.markdown(
            """
            <div class="kf-mock-panel" style="padding:36px; text-align:center; margin-top:40px; max-width:620px; margin-left:auto; margin-right:auto;">
                <div class="kf-mock-panel-label" style="padding:0 0 14px;">Signup Server Not Reachable</div>
                <div class="kf-stage-desc" style="max-width:480px; margin:0 auto;">
                    Signup connects to the live SixStage backend, which isn't
                    reachable right now. Start it locally, then reload this page.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            """
            <div style="text-align:center; margin-top:8px; margin-bottom:4px; font-size:13px; color:rgba(255,255,255,0.6);">
                Already have a workspace?
                <a href="/security-console" target="_self" style="color:#38bdf8; font-weight:600;">Sign in here &rarr;</a>
            </div>
            """,
            unsafe_allow_html=True
        )

        with st.form("kf_get_started_form"):
            col1, col2 = st.columns(2)
            with col1:
                full_name = st.text_input("Your name / organization")
            with col2:
                email = st.text_input("Work email")
            col3, col4 = st.columns(2)
            with col3:
                password = st.text_input("Password", type="password")
            with col4:
                password_confirm = st.text_input("Confirm password", type="password")
            submitted = st.form_submit_button("Create My Workspace")

            if submitted:
                if not full_name.strip() or "@" not in email:
                    st.error("Please enter your name/organization and a valid email address.")
                elif len(password) < 6:
                    st.error("Password must be at least 6 characters.")
                elif password != password_confirm:
                    st.error("Passwords don't match.")
                else:
                    outcome = _signup(email.strip(), password, full_name.strip())
                    if outcome["ok"]:
                        st.session_state["kf_signup_result"] = outcome
                        st.rerun()
                    else:
                        st.error(outcome["error"])

        st.markdown(
            """
            <div style="text-align:center; margin-top:14px; font-size:12px; color:rgba(255,255,255,0.5);">
                No credit card required today &mdash; billing is being wired up next.
                You're securing early access to your workspace now.
            </div>
            """,
            unsafe_allow_html=True
        )
