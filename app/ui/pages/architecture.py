import streamlit as st

from app.services.intelligence_service import IntelligenceService


def render():

    st.title("🏗 Architecture")

    st.subheader("Architecture Recommendation Engine")

    st.caption(
        "The most recent recommendation produced by "
        "ArchitectureRecommendationEngine. Run a new opportunity from the "
        "Opportunities page to generate another."
    )

    record = IntelligenceService().get_latest()

    if not record:
        st.info("No architecture recommendation generated yet.")
        return

    customer = record["customer"]

    st.caption(f"Latest opportunity: {customer['name']} — {record['title']}")

    st.divider()

    solution = record.get("solution") or {}
    architecture = solution.get("architecture", {})

    if not architecture.get("deployment_model") and not architecture.get("components"):
        st.warning(
            "This opportunity's requirements did not match a known "
            "architecture pattern, so no recommendation was produced. "
            "The engine currently recognizes a small set of requirement "
            "keywords (for example \"Immutable Backup\")."
        )
        return

    st.header("Deployment Model")
    st.success(architecture.get("deployment_model", "—"))

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Components")
        for component in architecture.get("components", []):
            st.write("✅ " + component)

    with col2:
        st.subheader("Security Controls")
        for control in architecture.get("security_controls", []):
            st.write("🔒 " + control)

    st.divider()

    st.subheader("Risks")
    for risk in solution.get("risks", []):
        st.warning(risk)

    st.subheader("Implementation Steps")
    for step in solution.get("implementation_plan", []):
        st.write("➡️ " + step)
