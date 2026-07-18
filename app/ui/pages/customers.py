import streamlit as st

from app.services.customer_service import CustomerService



def render():


    st.title(
        "Customers"
    )


    st.subheader(
        "Customer Management"
    )


    service = CustomerService()


    customers = service.load_all()



    if not customers:

        st.info(
            "No customers found"
        )

        return



    for customer in customers:


        with st.container():

            st.divider()


            col1, col2, col3 = st.columns(3)



            with col1:

                st.metric(
                    "Customer",
                    customer.name
                )


            with col2:

                st.metric(
                    "Industry",
                    customer.industry
                )


            with col3:

                st.metric(
                    "Size",
                    customer.size
                )