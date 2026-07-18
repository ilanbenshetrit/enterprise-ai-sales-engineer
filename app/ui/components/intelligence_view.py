"""
Shared renderer for a full AI intelligence package: the output of
running a customer opportunity through all six pipeline stages
(analysis, architecture, POC plan, implementation plan, demo plan,
proposal). Used by the Dashboard, Opportunities, and RFP Analyzer
pages so every entry point shows the same real product output.
"""

import streamlit as st


def render_intelligence_package(data, show_customer=True):

    if show_customer:

        customer = data.get("customer") or {}

        st.header("Customer Opportunity")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Customer", customer.get("name", "—"))

        with col2:
            st.metric("Industry", customer.get("industry", "—"))

        with col3:
            st.metric("Size", customer.get("size", "—"))

        st.divider()

    st.header("AI Analysis")

    analysis = data.get("analysis") or {}

    st.subheader("Technical Risks")

    for risk in analysis.get("technical_risks", []):
        st.warning(risk)

    st.subheader("Discovery Questions")

    for question in analysis.get("discovery_questions", []):
        st.info(question)

    st.divider()

    st.header("Solution Architecture")

    solution = data.get("solution") or {}

    architecture = solution.get("architecture", {})

    if architecture.get("deployment_model"):
        st.success(architecture.get("deployment_model"))

    for component in architecture.get("components", []):
        st.write("✅ " + component)

    for control in architecture.get("security_controls", []):
        st.write("🔒 " + control)

    st.divider()

    st.header("POC Plan")

    poc = data.get("poc_plan") or {}

    if poc.get("duration"):
        st.write("Duration:", poc.get("duration"))

    for test in poc.get("test_cases", []):
        st.write("✔ " + test)

    for criterion in poc.get("success_criteria", []):
        st.write("🎯 " + criterion)

    st.divider()

    st.header("Implementation Plan")

    implementation = data.get("implementation_plan") or {}

    for phase in implementation.get("phases", []):
        if isinstance(phase, dict):
            st.write("➡️ " + phase.get("name", phase.get("phase", str(phase))))
        else:
            st.write("➡️ " + phase)

    st.divider()

    st.header("Demo Strategy")

    demo = data.get("demo_plan") or {}

    if demo.get("objective"):
        st.write(demo.get("objective"))
    else:
        st.caption("No demo objective generated for this opportunity yet.")

    st.divider()

    st.header("Proposal")

    proposal = data.get("proposal") or {}

    if proposal.get("executive_summary"):
        st.write(proposal.get("executive_summary"))
    else:
        st.caption("No proposal summary generated for this opportunity yet.")
