"""
Enterprise AI Sales Engineer Platform
Main Dashboard
"""


import streamlit as st


from components.layout import (
    setup_page,
    page_header
)



setup_page(
    "Enterprise AI Sales Engineer",
    "🤖"
)



page_header(
    "🤖 Enterprise AI Sales Engineer Platform",
    "AI-Powered Presales & Solution Engineering Workspace"
)



st.subheader(
    "📊 Platform Overview"
)



col1, col2, col3, col4 = st.columns(4)



with col1:

    st.metric(
        "Knowledge Documents",
        "18"
    )


with col2:

    st.metric(
        "RFP Analyses",
        "12"
    )


with col3:

    st.metric(
        "AI Conversations",
        "148"
    )


with col4:

    st.metric(
        "System Status",
        "Online"
    )



st.divider()



left, right = st.columns(2)



with left:

    st.subheader(
        "📊 Recent Activity"
    )


    st.success(
        "Rubrik RFP Analysis Completed"
    )


    st.success(
        "Knowledge Base Updated"
    )


    st.success(
        "AI Discovery Session Generated"
    )



with right:

    st.subheader(
        "⚙️ Platform Health"
    )


    st.success(
        "Knowledge Engine Online"
    )


    st.success(
        "Enterprise Agent Ready"
    )


    st.success(
        "Memory Service Healthy"
    )



st.divider()



st.subheader(
    "🚀 Platform Capabilities"
)



cap1, cap2, cap3 = st.columns(3)



with cap1:

    st.info(
        """
        📄 RFP Intelligence
        
        Analyze requirements,
        risks and solution direction.
        """
    )



with cap2:

    st.info(
        """
        📚 Knowledge Engine
        
        Enterprise solution
        knowledge retrieval.
        """
    )



with cap3:

    st.info(
        """
        🤖 AI Sales Engineer
        
        Architecture,
        discovery and recommendations.
        """
    )
