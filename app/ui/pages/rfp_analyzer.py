import streamlit as st

from app.dashboard.dashboard_service import DashboardService
from app.ui.components.intelligence_view import render_intelligence_package


def render():

    st.title("RFP Analyzer")

    st.subheader("Turn RFP Requirements Into a Full Intelligence Package")

    st.caption(
        "Paste the requirements pulled from an RFP and SixStage will run "
        "them through the same opportunity intelligence pipeline used "
        "everywhere else on the platform: analysis, architecture, POC "
        "plan, implementation plan, demo plan, and proposal."
    )

    with st.form("kf_rfp_form"):

        col1, col2, col3 = st.columns(3)

        with col1:
            customer_name = st.text_input("Customer name")

        with col2:
            industry = st.text_input("Industry")

        with col3:
            size = st.text_input("Company size")

        rfp_text = st.text_area(
            "RFP requirements (one per line)",
            height=180,
            placeholder="Immutable Backup\nRansomware Recovery\n24/7 Support SLA"
        )

        submitted = st.form_submit_button("Analyze RFP")

    if submitted:

        requirements = [
            line.strip()
            for line in rfp_text.splitlines()
            if line.strip()
        ]

        if not customer_name or not requirements:
            st.warning("Customer name and at least one requirement are required.")
        else:
            service = DashboardService()

            result = service.create_opportunity(
                customer_name,
                industry,
                size,
                requirements,
                title="RFP Response"
            )

            st.success("RFP analyzed and saved to Opportunities.")

            render_intelligence_package(result)
