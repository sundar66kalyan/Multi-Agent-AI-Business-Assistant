import streamlit as st
import webbrowser

from dashboard.api import DashboardAPI
from components.metric_card import metric_card


def show_reports():
    """Render the Reports page."""
    
    st.title("📄 Enterprise Reports Center")
    st.caption("Generate and download business reports")
    
    metrics = DashboardAPI.get_metrics()
    data = metrics["metrics"]
    
    # KPI Metrics
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("Revenue", f"₹{data['revenue']:,.0f}", "+12%", "💰")
    with c2:
        metric_card("Profit", f"₹{data['profit']:,.0f}", "+18%", "📈")
    with c3:
        metric_card("Documents", data["documents"], "+5", "📄")
    with c4:
        metric_card("Finance Records", data["finance_records"], "+8", "💰")
    
    st.divider()
    
    # Report Cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("📄 PDF Report")
        st.write("""
            Professional business report including:
            - Executive Summary
            - Financial Overview
            - Analytics
            - Charts
        """)
        if st.button("📥 Download PDF", use_container_width=True, key="pdf_report"):
            webbrowser.open(DashboardAPI.export_pdf())
    
    with col2:
        st.subheader("📊 Excel Report")
        st.write("""
            Spreadsheet including:
            - Revenue
            - Expenses
            - Profit
            - Analytics
        """)
        if st.button("📥 Download Excel", use_container_width=True, key="excel_report"):
            webbrowser.open(DashboardAPI.export_excel())
    
    with col3:
        st.subheader("📝 Word Report")
        st.write("""
            Formatted report suitable for:
            - Meetings
            - Management
            - Printing
        """)
        if st.button("📥 Download DOCX", use_container_width=True, key="docx_report"):
            webbrowser.open(DashboardAPI.export_docx())
    
    # Report Summary
    st.divider()
    st.subheader("📋 Report Contents")
    st.markdown("""
        ✔ Executive Summary
        ✔ Financial Overview
        ✔ Revenue Analysis
        ✔ Profit Analysis
        ✔ Business Metrics
        ✔ AI Agent Statistics
        ✔ System Analytics
        ✔ Generated Charts
    """)