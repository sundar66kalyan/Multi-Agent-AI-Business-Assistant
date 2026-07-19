import streamlit as st
import webbrowser

from dashboard.api import DashboardAPI


def show_report_agent():
    """Render the Report Agent page."""
    
    st.title("📋 Report Agent")
    st.caption("AI-powered report generation and export")
    
    st.info("""
    **Report Agent Capabilities:**
    - Automated reports
    - PDF generation
    - Excel export
    - Data visualization
    - Scheduled reports
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Reports Generated", "126", "+15")
        st.metric("PDF Reports", "54", "+8")
    with col2:
        st.metric("Excel Reports", "42", "+5")
        st.metric("DOCX Reports", "30", "+2")
    with col3:
        st.metric("Scheduled Reports", "8", "+2")
        st.metric("Templates", "12", "+1")
    
    st.divider()
    st.subheader("Recent Reports")
    col1, col2 = st.columns(2)
    with col1:
        st.info("📄 Q2 Financial Report")
        st.info("📊 Marketing Campaign Summary")
        st.info("📄 Employee Performance Review")
    with col2:
        st.info("📊 Sales Dashboard - June")
        st.info("📄 HR Monthly Report")
        st.info("📊 Project Analytics Report")
    
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📥 Download All Reports (PDF)", use_container_width=True):
            webbrowser.open(DashboardAPI.export_pdf())
    with col2:
        if st.button("📊 Export as Excel", use_container_width=True):
            webbrowser.open(DashboardAPI.export_excel())
    with col3:
        if st.button("📝 Export as DOCX", use_container_width=True):
            webbrowser.open(DashboardAPI.export_docx())