"""
Enterprise AI Sales Platform
Shared UI Layout Components
"""


import streamlit as st



def setup_page(
    title,
    icon="🤖"
):


    st.set_page_config(
        page_title=title,
        page_icon=icon,
        layout="wide"
    )



    create_sidebar()



def create_sidebar():


    with st.sidebar:


        st.title(
            "🤖 Enterprise AI"
        )


        st.caption(
            "Sales Engineer Platform"
        )


        st.divider()



        st.success(
            "System Online"
        )



        st.write(
            """
            Version: MVP 1.0
            
            Agent: Ready
            
            Knowledge: Connected
            
            Memory: Enabled
            """
        )



        st.divider()



        st.info(
            "AI-Powered Presales Workspace"
        )



def page_header(
    title,
    description
):


    st.title(
        title
    )


    st.caption(
        description
    )


    st.divider()ס

