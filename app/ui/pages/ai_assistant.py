import streamlit as st

from app.knowledge.service import KnowledgeService


def render():

    st.title("🧠 AI Assistant")

    st.subheader("Search the Enterprise Knowledge Base")

    st.caption(
        "Retrieval-augmented search over the documents in the knowledge/ "
        "folder, using the vector store and retriever already built into "
        "the platform. Currently running on the mock embedding provider — "
        "swap in the OpenAI provider in app/embeddings/providers for "
        "production-quality semantic matching."
    )

    if "kf_knowledge_service" not in st.session_state:
        st.session_state["kf_knowledge_service"] = KnowledgeService()

    service = st.session_state["kf_knowledge_service"]

    chunk_count = len(service.get_knowledge_chunks())

    st.caption(f"Indexed chunks: {chunk_count}")

    query = st.text_input(
        "Ask a question",
        placeholder="What ransomware recovery capabilities do we offer?"
    )

    if query:

        results = service.search(query)

        if not results:
            st.info("No matching knowledge found for that question.")
        else:
            for result in results:

                chunk = result["chunk"]
                score = result["score"]
                source = chunk.get("metadata", {}).get("source", "unknown")

                with st.container():
                    st.markdown(f"**Source:** {source}  \n**Relevance:** {score:.2f}")
                    st.write(chunk.get("content", ""))
                    st.divider()
