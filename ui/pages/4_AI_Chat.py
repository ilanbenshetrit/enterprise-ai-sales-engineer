"""
Enterprise AI Sales Platform
AI Chat UI
"""


import streamlit as st



st.set_page_config(
    page_title="AI Chat",
    page_icon="🤖",
    layout="wide"
)



st.title(
    "🤖 AI Chat"
)


st.caption(
    "Chat with the Enterprise Sales Engineer Agent"
)


st.divider()



# Initialize chat history

if "messages" not in st.session_state:

    st.session_state.messages = []



# Display previous messages

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.write(
            message["content"]
        )



# User input

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



    # Temporary response

    response = (
        "Agent connection will be integrated here. "
        "The Enterprise Sales Engineer Agent will answer using knowledge and RFP context."
    )



    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )


    with st.chat_message(
        "assistant"
    ):

        st.write(
            response
        )
