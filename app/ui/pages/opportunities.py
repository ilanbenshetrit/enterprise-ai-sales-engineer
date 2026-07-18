import streamlit as st

from app.services.intelligence_service import IntelligenceService
from app.dashboard.dashboard_service import DashboardService
from app.ui.components.intelligence_view import render_intelligence_package


def render():

    st.title("💼 Opportunities")

    st.subheader("Run and Review Opportunity Intelligence")

    with st.expander("➕ Run New Opportunity Analysis", expanded=False):

        with st.form("kf_new_opportunity_form"):

            col1, col2, col3 = st.columns(3)

            with col1:
                customer_name = st.text_input("Customer name", value="")

            with col2:
                industry = st.text_input("Industry", value="")

            with col3:
                size = st.text_input("Company size", value="")

            title = st.text_input("Opportunity title", value="")

            requirements_raw = st.text_area(
                "Requirements (one per line)",
                height=100,
                placeholder="Immutable Backup\nMulti-region Failover"
            )

            submitted = st.form_submit_button("Run Analysis")

            if submitted:

                if not customer_name or not title:
                    st.warning("Customer name and opportunity title are required.")
                else:
                    requirements = [
                        line.strip()
                        for line in requirements_raw.splitlines()
                        if line.strip()
                    ]

                    service = DashboardService()

                    result = service.create_opportunity(
                        customer_name,
                        industry,
                        size,
                        requirements,
                        title=title
                    )

                    st.session_state["kf_last_opportunity_result"] = result

    if st.session_state.get("kf_last_opportunity_result"):

        st.success("Analysis complete — this opportunity is now saved below.")

        with st.expander("Latest Result", expanded=True):
            render_intelligence_package(
                st.session_state["kf_last_opportunity_result"]
            )

    st.divider()

    st.subheader("Past Opportunities")

    records = IntelligenceService().list_all()

    if not records:
        st.info("No opportunities analyzed yet. Run one above to get started.")
        return

    for record in records:

        customer = record["customer"]

        label = f"{customer['name']} — {record['title']}"

        with st.expander(label):
            render_intelligence_package(record)
