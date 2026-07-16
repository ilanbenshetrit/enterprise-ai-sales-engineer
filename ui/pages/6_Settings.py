"""
Enterprise AI Sales Platform
Settings UI
"""


import streamlit as st



st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)



st.title(
    "⚙️ Settings"
)


st.caption(
    "Configure Enterprise Sales Engineer Agent environment"
)


st.divider()



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
