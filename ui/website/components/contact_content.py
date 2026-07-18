"""
SixStage Contact Page Content
"""

import streamlit as st


def render_contact_content():

    st.markdown(
        """
        <style>
        [data-testid="stTextInput"] input,
        [data-testid="stTextArea"] textarea {
            background: rgba(255,255,255,0.06) !important;
            border: 1px solid rgba(255,255,255,0.15) !important;
            color: white !important;
            border-radius: 10px !important;
        }
        [data-testid="stTextInput"] label p,
        [data-testid="stTextArea"] label p {
            color: rgba(255,255,255,0.75) !important;
        }
        [data-testid="stFormSubmitButton"] button {
            background: linear-gradient(90deg,#8b5cf6,#38bdf8,#34d399) !important;
            color: white !important;
            border: none !important;
            border-radius: 14px !important;
            padding: 10px 30px !important;
            font-weight: 600 !important;
        }
        .kf-contact-info-item {
            margin-bottom: 32px;
        }
        .kf-contact-info-label {
            color: #38bdf8;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 8px;
        }
        .kf-contact-info-desc {
            font-size: 15px;
            color: rgba(255,255,255,0.85);
            line-height: 1.6;
        }
        </style>
        <div class="kf-section" style="margin-bottom:60px;">
            <div class="kf-section-label">Contact</div>
            <div class="kf-section-title">Let's Talk About Your Next Deal</div>
            <div class="kf-section-body">
                <p>Tell us a bit about what you are working on and a member
                of the SixStage team will follow up.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    info_col, form_col = st.columns([2, 3], gap="large")

    with info_col:
        st.markdown(
            """
            <div class="kf-contact-info-item">
                <div class="kf-contact-info-label">General Inquiries</div>
                <div class="kf-contact-info-desc">hello@sixstage.ai</div>
            </div>
            <div class="kf-contact-info-item">
                <div class="kf-contact-info-label">Headquarters</div>
                <div class="kf-contact-info-desc">San Francisco, CA<br>
                Engineering hubs in Tel Aviv and Berlin</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with form_col:
        if st.session_state.get("kf_contact_submitted"):
            st.success(
                "Thanks — your message has been received. "
                "We'll be in touch shortly."
            )
            if st.button("Send another message"):
                st.session_state["kf_contact_submitted"] = False
                st.rerun()
        else:
            with st.form("kf_contact_form", clear_on_submit=True):
                st.text_input("Name")
                st.text_input("Work email")
                st.text_input("Company")
                st.text_area("What are you looking to solve?", height=120)
                submitted = st.form_submit_button("Send message")

                if submitted:
                    st.session_state["kf_contact_submitted"] = True
                    st.rerun()
