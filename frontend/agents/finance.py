import streamlit as st
import plotly.express as px
import pandas as pd

from dashboard.api import DashboardAPI


def show_finance_agent():
    """Render the Finance Agent page."""
    
    st.title("💳 Finance Agent")
    st.caption("AI-powered financial analysis and reporting")
    
    st.info("""
    **Finance Agent Capabilities:**
    - Financial statement analysis
    - Budget tracking
    - Expense management
    - Profitability analysis
    - Cash flow forecasting
    """)
    
    metrics = DashboardAPI.get_metrics()
    data = metrics["metrics"] if metrics["success"] else {}
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Revenue", f"₹{data.get('revenue', 0):,}")
        st.metric("Expenses", f"₹{data.get('expenses', 0):,}")
    with col2:
        st.metric("Profit", f"₹{data.get('profit', 0):,}")
        st.metric("Profit Margin", f"{data.get('profit_margin', 0)}%")
    with col3:
        st.metric("Documents", data.get('documents', 0))
        st.metric("Finance Records", data.get('finance_records', 0))
    
    st.divider()
    
    chart = DashboardAPI.get_finance_chart()
    if chart["success"]:
        chart_data = pd.DataFrame({
            "Metric": chart["chart"]["labels"],
            "Amount": chart["chart"]["values"]
        })
        fig = px.bar(
            chart_data,
            x="Metric",
            y="Amount",
            text="Amount",
            title="Financial Overview",
            color_discrete_sequence=["#667eea", "#764ba2", "#06b6d4"]
        )
        st.plotly_chart(fig, use_container_width=True)