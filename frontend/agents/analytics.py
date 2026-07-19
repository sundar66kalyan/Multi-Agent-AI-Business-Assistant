import streamlit as st

from dashboard.api import DashboardAPI


def show_analytics_agent():
    """Render the Analytics Agent page."""
    
    st.title("📊 Analytics Agent")
    st.caption("AI-powered business intelligence and insights")
    
    st.info("""
    **Analytics Agent Capabilities:**
    - Business intelligence
    - KPI tracking
    - Predictive analytics
    - Custom reports
    - Trend analysis
    """)
    
    agents_response = DashboardAPI.get_agents()
    agents = agents_response["agents"] if agents_response["success"] else []
    
    metrics = DashboardAPI.get_metrics()
    data = metrics["metrics"] if metrics["success"] else {}
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Documents Analyzed", data.get('documents', 0))
        st.metric("Data Points", data.get('chunks', 0))
    with col2:
        st.metric("Insights Generated", "156", "+23")
        st.metric("Reports", "42", "+8")
    with col3:
        st.metric("Active Agents", len(agents))
        st.metric("Accuracy", "96.5%", "+0.5%")