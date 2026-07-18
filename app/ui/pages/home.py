import streamlit as st


def render():

    st.title(
        "Kubeforge"
    )

    st.subheader(
        "Enterprise AI Agents for Modern Sales Engineering"
    )

    st.write(
        """
        Kubeforge builds AI-powered enterprise agents
        that transform complex technical sales processes
        into intelligent, repeatable workflows.
        """
    )


    st.divider()


    col1, col2, col3 = st.columns(3)


    with col1:
        st.metric(
            "AI Agents",
            "Multi-Agent"
        )


    with col2:
        st.metric(
            "Enterprise Focus",
            "B2B"
        )


    with col3:
        st.metric(
            "Workflow",
            "Discovery → Proposal"
        )


    st.divider()


    st.header(
        "AI Sales Engineer Platform"
    )


    st.write(
        """
        An intelligent workspace that helps enterprise
        teams discover requirements, analyze risks,
        design solutions and accelerate proposals.
        """
    )