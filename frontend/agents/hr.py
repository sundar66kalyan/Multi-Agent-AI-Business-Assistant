import streamlit as st
import plotly.express as px
import pandas as pd


def show_hr_agent():
    """Render the HR Agent page."""
    
    st.title("👔 HR Agent")
    st.caption("AI-powered human resources management")
    
    st.info("""
    **HR Agent Capabilities:**
    - Employee management
    - Leave tracking
    - Attendance monitoring
    - Payroll processing
    - Performance reviews
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Employees", "156", "+4")
        st.metric("On Leave", "12", "+2")
    with col2:
        st.metric("New Hires (This Month)", "8", "+3")
        st.metric("Open Positions", "5", "-2")
    with col3:
        st.metric("Attendence Rate", "94%", "+1%")
        st.metric("Employee Satisfaction", "4.2/5", "+0.3")
    
    st.divider()
    
    dept_data = pd.DataFrame({
        "Department": ["Engineering", "Marketing", "Sales", "HR", "Finance"],
        "Employees": [45, 32, 28, 15, 36]
    })
    fig = px.bar(
        dept_data,
        x="Department",
        y="Employees",
        title="Department Distribution",
        color_discrete_sequence=["#667eea", "#764ba2", "#06b6d4", "#f59e0b", "#ef4444"]
    )
    st.plotly_chart(fig, use_container_width=True)