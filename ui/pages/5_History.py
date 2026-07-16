"""
Enterprise AI Sales Platform
Analysis History UI
"""


import streamlit as st


from components.layout import (
    setup_page,
    page_header
)



setup_page(
    "Analysis History",
    "📊"
)



page_header(
    "📊 Analysis History",
    "Review previous RFP analyses and AI Sales Engineer sessions"
)



# Temporary history data
# Will be connected to persistent storage later

history_items = [

    {
        "title": "Rubrik RFP Analysis",
        "date": "2026-07-16",
        "requirements": 5,
        "risks": 2
    },

    {
        "title": "Cyber Resilience Assessment",
        "date": "2026-07-15",
        "requirements": 7,
        "risks": 1
    }

]



st.subheader(
    "📄 Previous Analyses"
)



for item in history_items:


    with st.container():

        st.markdown(
            f"### 📄 {item['title']}"
        )


        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Date",
                item["date"]
            )


        with col2:

            st.metric(
                "Requirements",
                item["requirements"]
            )


        with col3:

            st.metric(
                "Risks",
                item["risks"]
            )


        st.divider()
