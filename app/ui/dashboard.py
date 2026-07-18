"""
Kubeforge Product Dashboard

The actual internal sales-engineering tool: customer records,
opportunity management, and the full six-stage AI intelligence
pipeline (analysis, architecture, POC plan, implementation plan,
demo plan, proposal). Rendered as a page inside the marketing site.
"""

import streamlit as st

from app.ui.components.sidebar import render_sidebar
from app.ui.components.intelligence_view import render_intelligence_package

from app.ui.pages.home import render as render_home
from app.ui.pages.customers import render as render_customers
from app.ui.pages.opportunities import render as render_opportunities
from app.ui.pages.architecture import render as render_architecture
from app.ui.pages.poc_builder import render as render_poc_builder
from app.ui.pages.rfp_analyzer import render as render_rfp_analyzer
from app.ui.pages.ai_assistant import render as render_ai_assistant
from app.ui.pages.reports import render as render_reports
from app.ui.pages.settings import render as render_settings

from app.dashboard.dashboard_service import DashboardService


_PAGE_ROUTES = {
    "dashboard": render_home,
    "customers": render_customers,
    "opportunities": render_opportunities,
    "architecture": render_architecture,
    "poc_builder": render_poc_builder,
    "rfp_analyzer": render_rfp_analyzer,
    "ai_assistant": render_ai_assistant,
    "reports": render_reports,
    "settings": render_settings,
}


def render_dashboard():

    st.markdown(
        '<a href="/platform" target="_self" '
        'style="color:#38bdf8; text-decoration:none; font-size:14px;">'
        '&larr; Back to Platform overview</a>',
        unsafe_allow_html=True
    )

    selected_page = render_sidebar()

    route = _PAGE_ROUTES.get(selected_page)

    if route:
        route()
        return

    # Fallback: full pipeline snapshot for the latest opportunity.

    service = DashboardService()

    data = service.get_dashboard_data()

    st.title("🚀 Kubeforge")
    st.subheader("Enterprise AI Sales Engineer Platform")
    st.divider()

    render_intelligence_package(data)
