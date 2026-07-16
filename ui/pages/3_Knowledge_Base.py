"""
Enterprise AI Sales Platform
Knowledge Base UI
"""


import streamlit as st

from pathlib import Path



st.set_page_config(
    page_title="Knowledge Base",
    page_icon="📚",
    layout="wide"
)



st.title(
    "📚 Knowledge Base"
)


st.caption(
    "Manage enterprise knowledge documents used by the AI Sales Engineer"
)


st.divider()



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
