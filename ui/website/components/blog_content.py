"""
Blog Page Content — Honest Coming-Soon Placeholder
"""

import streamlit as st


def render_blog_content():

    st.markdown(
        """
        <div class="kf-stage-hero">
            <div class="kf-stage-eyebrow">Blog</div>
            <div class="kf-stage-title">
                Coming <span class="gradient-text">Soon</span>
            </div>
            <div class="kf-stage-desc">
                We're writing about what we're actually building &mdash;
                scanner internals, the move to multi-tenant SaaS, and
                lessons from AI/identity security &mdash; instead of
                publishing filler before we have something to say.
            </div>
        </div>
        <div class="kf-mock-panel" style="margin-top:20px; text-align:center; padding:36px;">
            <div class="kf-stage-desc" style="max-width:520px; margin:0 auto;">
                In the meantime, see the real product in the
                <a href="/security-console" target="_self" style="color:#38bdf8;">Live Security Console</a>,
                or read the <a href="/docs" target="_self" style="color:#38bdf8;">API docs</a>.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
