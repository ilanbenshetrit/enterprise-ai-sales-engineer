"""
Security Platform — Live Console

Embeds the real, locally-running SixStage Security backend
(kubeforge-app, FastAPI) so visitors can access and interact with the
actual product instead of a marketing mockup. Checks the backend's
health endpoint server-side first, so the page fails gracefully with
clear instructions instead of showing a broken iframe.
"""

import streamlit as st
import requests

SECURITY_BACKEND_URL = "http://localhost:8080"


def _backend_is_reachable() -> bool:
    try:
        r = requests.get(f"{SECURITY_BACKEND_URL}/health", timeout=1.5)
        return r.status_code == 200
    except requests.exceptions.RequestException:
        return False


def render_security_console():

    reachable = _backend_is_reachable()

    st.markdown(
        """
        <a class="kf-stage-back" href="/security" target="_self">&larr; Back to Security Platform</a>
        <div class="kf-stage-hero">
            <div class="kf-stage-eyebrow">Live Security Console</div>
            <div class="kf-stage-title">
                Your <span class="gradient-text">Real Security Platform</span>, Live
            </div>
            <div class="kf-stage-desc">
                This is the actual SixStage Security backend running on your
                machine &mdash; live scans, posture data, and the AI copilot,
                not a preview.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if reachable:
        st.markdown(
            f"""
            <div class="kf-mock-panel" style="padding:0; overflow:hidden; margin-top:20px;">
                <iframe src="{SECURITY_BACKEND_URL}" style="width:100%; height:900px;
                        border:none; display:block;"></iframe>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div class="kf-mock-panel" style="padding:36px; text-align:center; margin-top:20px;">
                <div class="kf-mock-panel-label" style="padding:0 0 14px;">Backend Not Reachable</div>
                <div class="kf-stage-desc" style="max-width:620px; margin:0 auto 20px;">
                    The Security Console couldn't reach the backend at
                    <code>{SECURITY_BACKEND_URL}</code>. Start it locally, then
                    reload this page.
                </div>
                <div class="kf-mock-panel-label" style="padding:0 0 8px; text-align:left;
                     max-width:460px; margin:0 auto;">To Start It</div>
                <div style="max-width:460px; margin:0 auto; text-align:left;
                     background:rgba(0,0,0,0.35); border-radius:10px; padding:16px 20px;
                     font-family:monospace; font-size:13px; color:#93c5fd; line-height:1.9;">
                    cd kubeforge-app<br>
                    python main.py
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
