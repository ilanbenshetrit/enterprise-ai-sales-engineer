"""
Enterprise AI Sales Platform
Settings UI
"""


import streamlit as st


from components.layout import (
    setup_page,
    page_header
)



setup_page(
    "Settings",
    "⚙️"
)



page_header(
    "⚙️ Settings",
    "Configure Enterprise Sales Engineer Agent environment"
)



# Agent Configuration

st.subheader(
    "🤖 Agent Configuration"
)


st.text_input(
    "Agent Name",
    value="Enterprise Sales Engineer Agent"
)



st.divider()



# Knowledge Configuration

st.subheader(
    "📚 Knowledge Configuration"
)


st.text_input(
    "Knowledge Directory",
    value="knowledge/"
)



st.divider()



# Memory Configuration

st.subheader(
    "🧠 Memory Configuration"
)



memory_status = st.toggle(
    "Enable Agent Memory",
    value=True
)



if memory_status:

    st.success(
        "Agent memory is enabled"
    )

else:

    st.warning(
        "Agent memory is disabled"
    )



st.divider()



# LLM Configuration

st.subheader(
    "🔌 LLM Configuration"
)



st.selectbox(
    "LLM Provider",
    [
        "Claude",
        "OpenAI"
    ]
)



st.info(
    "LLM connection status will be validated here"
)
