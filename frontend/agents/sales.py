import streamlit as st
import plotly.express as px
import pandas as pd


def show_sales_agent():
    """Render the Sales Agent page."""
    
    st.title("💰 Sales Agent")
    st.caption("AI-powered sales analytics and insights")
    
    st.info("""
    **Sales Agent Capabilities:**
    - Sales performance tracking
    - Revenue forecasting
    - Customer insights
    - Product analytics
    - Sales pipeline management
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Revenue", "₹12,45,000", "+15%")
        st.metric("Sales Growth", "+12%", "+3%")
    with col2:
        st.metric("Active Customers", "1,284", "+8%")
        st.metric("Avg. Order Value", "₹4,250", "+5%")
    with col3:
        st.metric("Conversion Rate", "24.5%", "+2.1%")
        st.metric("Sales Pipeline", "₹85L", "+10%")
    
    st.divider()
    
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    sales_data = pd.DataFrame({
        "Month": months,
        "Revenue": [850000, 920000, 880000, 1050000, 1120000, 1245000],
        "Target": [900000, 950000, 900000, 1000000, 1100000, 1200000]
    })
    fig = px.line(
        sales_data,
        x="Month",
        y=["Revenue", "Target"],
        title="Sales Performance vs Target",
        color_discrete_sequence=["#667eea", "#ef4444"]
    )
    st.plotly_chart(fig, use_container_width=True)