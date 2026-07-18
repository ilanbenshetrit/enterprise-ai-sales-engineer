import streamlit as st

from app.ui.components.sidebar import render_sidebar
from app.ui.pages.customers import render as render_customers
from app.ui.pages.home import render as render_home

from app.dashboard.dashboard_service import DashboardService


st.set_page_config(
    page_title="Kubeforge",
    layout="wide"
)


selected_page = render_sidebar()



# ==========================
# Page Router
# ==========================

if selected_page == "dashboard":

    render_home()

    st.stop()



if selected_page == "customers":

    render_customers()

    st.stop()



# ==========================
# Default Dashboard
# ==========================


service = DashboardService()


data = service.get_dashboard_data()



st.title(
    "🚀 Kubeforge"
)


st.subheader(
    "Enterprise AI Sales Engineer Platform"
)



st.divider()



customer = data["customer"]



st.header(
    "Customer Opportunity"
)



col1, col2, col3 = st.columns(3)



with col1:

    st.metric(
        "Customer",
        customer["name"]
    )



with col2:

    st.metric(
        "Industry",
        customer["industry"]
    )



with col3:

    st.metric(
        "Size",
        customer["size"]
    )



st.divider()



st.header(
    "AI Analysis"
)



analysis = data["analysis"]



st.subheader(
    "Technical Risks"
)


for risk in analysis.get(
    "technical_risks",
    []
):

    st.warning(
        risk
    )



st.subheader(
    "Discovery Questions"
)


for question in analysis.get(
    "discovery_questions",
    []
):

    st.info(
        question
    )



st.divider()



st.header(
    "Solution Architecture"
)



solution = data["solution"]



architecture = solution.get(
    "architecture",
    {}
)



st.success(
    architecture.get(
        "deployment_model",
        ""
    )
)



for component in architecture.get(
    "components",
    []
):

    st.write(
        "✅ " + component
    )



st.divider()



st.header(
    "POC Plan"
)



poc = data["poc_plan"]



st.write(
    "Duration:",
    poc.get(
        "duration",
        ""
    )
)



for test in poc.get(
    "test_cases",
    []
):

    st.write(
        "✔ " + test
    )



st.divider()



st.header(
    "Implementation Plan"
)



implementation = data["implementation_plan"]



for phase in implementation.get(
    "phases",
    []
):

    if isinstance(
        phase,
        dict
    ):

        st.write(
            "➡️ " + phase.get(
                "name",
                phase.get(
                    "phase",
                    str(phase)
                )
            )
        )

    else:

        st.write(
            "➡️ " + phase
        )



st.divider()



st.header(
    "Demo Strategy"
)



demo = data["demo_plan"]



st.write(
    demo.get(
        "objective",
        ""
    )
)



st.divider()



st.header(
    "Proposal"
)



proposal = data.get(
    "proposal",
    {}
)



st.write(
    proposal.get(
        "executive_summary",
        ""
    )
)