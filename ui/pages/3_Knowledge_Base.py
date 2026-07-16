"""
Enterprise AI Sales Platform
Knowledge Base UI
"""


import streamlit as st


from pathlib import Path


from components.layout import (
    setup_page,
    page_header
)



setup_page(
    "Knowledge Base",
    "📚"
)



page_header(
    "📚 Knowledge Base",
    "Manage enterprise knowledge documents used by the AI Sales Engineer"
)



knowledge_path = Path(
    "knowledge"
)



st.subheader(
    "📄 Available Documents"
)



if not knowledge_path.exists():

    st.warning(
        "Knowledge directory not found"
    )


else:


    documents = list(
        knowledge_path.glob("*.md")
    )


    if not documents:

        st.info(
            "No knowledge documents available"
        )


    else:


        st.success(
            f"{len(documents)} knowledge documents available"
        )


        for document in documents:


            with st.expander(
                f"📄 {document.name}"
            ):


                content = document.read_text(
                    encoding="utf-8"
                )


                st.write(
                    content
                )


                st.caption(
                    f"Size: {len(content)} characters"
                )
