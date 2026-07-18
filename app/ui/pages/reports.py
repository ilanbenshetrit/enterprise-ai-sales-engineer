import streamlit as st

from app.services.customer_service import CustomerService
from app.services.opportunity_service import OpportunityService
from app.services.intelligence_service import IntelligenceService


def render():

    st.title("Reports")

    st.subheader("Pipeline Activity")

    customers = CustomerService().load_all()
    opportunities = OpportunityService().load_all()
    intelligence_records = IntelligenceService().list_all()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Customers", len(customers))

    with col2:
        st.metric("Opportunities", len(opportunities))

    with col3:
        st.metric("Intelligence Packages Generated", len(intelligence_records))

    st.divider()

    st.subheader("Opportunities by Industry")

    industry_counts = {}

    for record in intelligence_records:
        industry = record["customer"].get("industry") or "Unspecified"
        industry_counts[industry] = industry_counts.get(industry, 0) + 1

    if industry_counts:
        st.bar_chart(industry_counts)
    else:
        st.info("No data yet — run an opportunity analysis to populate reports.")

    st.divider()

    st.subheader("Recent Activity")

    if not intelligence_records:
        st.info("No opportunities analyzed yet.")
        return

    for record in intelligence_records[:10]:

        customer = record["customer"]

        col1, col2, col3 = st.columns([3, 2, 2])

        with col1:
            st.write(f"**{customer['name']}** — {record['title']}")

        with col2:
            st.write(customer.get("industry") or "—")

        with col3:
            st.caption(record["created_at"])
