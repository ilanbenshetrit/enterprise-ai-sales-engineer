import streamlit as st



def render_sidebar():


    pages = {

        "Dashboard": "dashboard",

        "Customers": "customers",

        "Opportunities": "opportunities",

        "RFP Analyzer": "rfp_analyzer",

        "AI Assistant": "ai_assistant",

        "Architecture": "architecture",

        "POC Builder": "poc_builder",

        "Reports": "reports",

        "Settings": "settings"

    }



    with st.sidebar:


        st.title(
            "AI Sales Engineer"
        )


        st.divider()



        selected = st.radio(

            "Navigation",

            list(
                pages.keys()
            )

        )



        st.divider()



        st.caption(
            "Enterprise AI Sales Platform"
        )



    return pages[selected]