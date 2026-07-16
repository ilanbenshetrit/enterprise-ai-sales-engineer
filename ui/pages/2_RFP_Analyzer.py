"""
Enterprise AI Sales Platform
RFP Analyzer UI
"""


import streamlit as st


from services.rfp_service import RFPService



st.set_page_config(
    page_title="RFP Analyzer",
    page_icon="📄",
    layout="wide"
)



# Initialize service

rfp_service = RFPService()



# Page Header

st.title(
    "📄 RFP Analyzer"
)


st.caption(
    "Analyze customer requirements, risks and solution direction"
)


st.divider()



# Upload Section

st.subheader(
    "Upload Customer RFP"
)



uploaded_file = st.file_uploader(
    "Choose RFP document",
    type=[
        "pdf",
        "docx",
        "txt",
        "md"
    ]
)



if uploaded_file:


    st.success(
        f"Uploaded: {uploaded_file.name}"
    )


    file_size = uploaded_file.size / 1024


    st.write(
        f"File size: {file_size:.2f} KB"
    )


    st.divider()



    if st.button(
        "🚀 Analyze RFP"
    ):


        with st.spinner(
            "Analyzing RFP..."
        ):


            try:


                result = rfp_service.analyze(
                    uploaded_file
                )


                st.success(
                    "Analysis Completed"
                )


                st.divider()


                st.subheader(
                    "📌 Analysis Result"
                )


                st.json(
                    result
                )


            except Exception as e:


                st.error(
                    "Analysis failed"
                )


                st.exception(e)
