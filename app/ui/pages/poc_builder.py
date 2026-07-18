import streamlit as st

from app.services.intelligence_service import IntelligenceService


def render():

    st.title("🧪 POC Builder")

    st.subheader("Proof-of-Concept Planning Engine")

    st.caption(
        "The most recent plan produced by POCPlanner. Run a new "
        "opportunity from the Opportunities page to generate another."
    )

    record = IntelligenceService().get_latest()

    if not record:
        st.info("No POC plan generated yet.")
        return

    customer = record["customer"]

    st.caption(f"Latest opportunity: {customer['name']} — {record['title']}")

    st.divider()

    poc = record.get("poc_plan") or {}

    if not poc.get("scope") and not poc.get("test_cases"):
        st.info("No POC plan was generated for this opportunity.")
        return

    st.metric("Duration", poc.get("duration", "—"))

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Scope")
        for item in poc.get("scope", []):
            st.write("• " + item)

        st.subheader("Test Cases")
        for test in poc.get("test_cases", []):
            st.write("✔ " + test)

    with col2:
        st.subheader("Success Criteria")
        for criterion in poc.get("success_criteria", []):
            st.write("🎯 " + criterion)

        st.subheader("Required Resources")
        for resource in poc.get("required_resources", []):
            st.write("👤 " + resource)
