"""
Enterprise AI Sales Platform
AI Chat UI
"""


import streamlit as st


from components.layout import (
    setup_page,
    page_header
)


from services.agent_service import AgentService



setup_page(
    "AI Chat",
    "🤖"
)



page_header(
    "🤖 AI Chat",
    "Chat with the Enterprise Sales Engineer Agent"
)



agent_service = AgentService()



if "messages" not in st.session_state:

    st.session_state.messages = []



for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.write(
            message["content"]
        )



prompt = st.chat_input(
    "Ask the Sales Engineer Agent..."
)



if prompt:


    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )


    with st.chat_message(
        "user"
    ):

        st.write(
            prompt
        )



    with st.chat_message(
        "assistant"
    ):


        with st.spinner(
            "Agent is thinking..."
        ):


            try:

                response = agent_service.ask(
                    prompt
                )


            except Exception as e:

                response = (
                    f"Agent error: {e}"
                )


            st.write(
                response
            )



    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
