"""
Enterprise AI Sales Platform
RFP Analyzer UI
"""


import streamlit as st


from components.layout import (
    setup_page,
    page_header
)


from services.rfp_service import RFPService



setup_page(
    "RFP Analyzer",
    "📄"
)



page_header(
    "📄 RFP Analyzer",
    "Analyze customer requirements, risks and solution direction"
)



rfp_service = RFPService()



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
                    "📌 Customer Requirements"
                )


                for item in result.get(
                    "requirements",
                    []
                ):

                    st.write(
                        f"✅ {item}"
                    )



                st.divider()



                st.subheader(
                    "❓ Discovery Questions"
                )


                for question in result.get(
                    "technical_questions",
                    []
                ):

                    st.write(
                        f"• {question}"
                    )



                st.divider()



                st.subheader(
                    "⚠️ Identified Risks"
                )


                risks = result.get(
                    "risks",
                    []
                )


                if risks:

                    for risk in risks:

                        st.warning(
                            risk
                        )

                else:

                    st.info(
                        "No risks identified"
                    )



                st.divider()



                st.subheader(
                    "🏗 Recommended Solution Direction"
                )


                for solution in result.get(
                    "solution_direction",
                    []
                ):

                    st.success(
                        solution
                    )



            except Exception as e:


                st.error(
                    "Analysis failed"
                )


                st.exception(e)
