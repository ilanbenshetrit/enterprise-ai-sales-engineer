import streamlit as st


st.set_page_config(
    page_title="Enterprise AI Sales Engineer",
    page_icon="🤖",
    layout="wide"
)


# Header

st.title(
    "🤖 Enterprise AI Sales Engineer Platform"
)

st.caption(
    "AI-Powered Presales & Solution Engineering Workspace"
)


st.divider()


# KPI Cards

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Knowledge Docs",
        "18"
    )


with col2:

    st.metric(
        "RFP Analyses",
        "12"
    )


with col3:

    st.metric(
        "AI Requests",
        "148"
    )


with col4:

    st.metric(
        "System Status",
        "Online"
    )


st.divider()


# Recent Activity + System Health

left, right = st.columns(2)


with left:

    st.subheader(
        "📊 Recent Activity"
    )


    st.write(
        """
        ✅ Rubrik RFP Analysis Completed
        
        ✅ Customer Discovery Session Prepared
        
        ✅ Knowledge Base Updated
        
        ✅ Executive Summary Generated
        """
    )



with right:

    st.subheader(
        "⚙️ System Health"
    )


    st.success(
        "Knowledge Base - Online"
    )


    st.success(
        "AI Agent - Ready"
    )


    st.success(
        "Memory Service - Healthy"
    )


st.divider()


# Platform Description

st.subheader(
    "🚀 Platform Capabilities"
)


cap1, cap2, cap3 = st.columns(3)


with cap1:

    st.info(
        """
        📄 RFP Intelligence
        
        Analyze customer requirements,
        risks and technical gaps.
        """
    )


with cap2:

    st.info(
        """
        📚 Knowledge Engine
        
        Retrieve information from
        enterprise solution knowledge.
        """
    )


with cap3:

    st.info(
        """
        🤖 AI Sales Engineer
        
        Generate discovery questions,
        architectures and recommendations.
        """
    )