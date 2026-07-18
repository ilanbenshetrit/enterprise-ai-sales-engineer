import os

import streamlit as st

from app.config.settings import settings
from app.knowledge.service import KnowledgeService


def render():

    st.title("Settings")

    st.subheader("Platform Configuration")

    st.caption(
        "Read-only view of the current configuration, loaded from "
        "app/config/settings.py and your environment. Change values in "
        "your .env file and restart the app to update them."
    )

    st.divider()

    st.subheader("LLM Provider")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Provider**")
        st.write(settings.llm_provider)

        st.write("**Model**")
        st.write(settings.llm_model)

    with col2:
        st.write("**Temperature**")
        st.write(settings.temperature)

        st.write("**Max tokens**")
        st.write(settings.max_tokens)

    api_key_set = bool(os.getenv("OPENAI_API_KEY"))

    if api_key_set:
        st.success("OPENAI_API_KEY is configured")
    else:
        st.warning("OPENAI_API_KEY is not set — reasoning and planning "
                    "engines currently run on rule-based logic only.")

    st.divider()

    st.subheader("Knowledge Base")

    doc_count = len(KnowledgeService().loader.load_documents())

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Documents Indexed", doc_count)

    with col2:
        st.write("**Embedding Provider**")
        st.write("Mock (local, hash-based) — swap in "
                  "app/embeddings/providers/openai_embedding_provider.py "
                  "for production use.")

    st.divider()

    st.subheader("Database")

    st.write("**Engine**")
    st.write("SQLite")

    st.write("**File**")
    st.code("sales_engineer.db")
