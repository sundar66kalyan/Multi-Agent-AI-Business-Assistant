import streamlit as st
import pandas as pd


def show_document_agent():
    """Render the Document Agent page."""
    
    st.title("📄 Document Agent")
    st.caption("AI-powered document management and analysis")
    
    st.info("""
    **Document Agent Capabilities:**
    - Document indexing
    - Content extraction
    - Search and retrieval
    - Summarization
    - Document analysis
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Documents", "247", "+18")
        st.metric("Indexed Chunks", "12,456", "+1,234")
    with col2:
        st.metric("Uploaded Today", "7", "+3")
        st.metric("File Types", "12", "+0")
    with col3:
        st.metric("Total Storage", "128 MB", "+12 MB")
        st.metric("Last Indexed", "10 min ago", "")
    
    st.divider()
    st.subheader("Recent Documents")
    st.dataframe(
        pd.DataFrame({
            "Document Name": ["Q2 Report.pdf", "Employee Handbook.docx", "Financial_Summary.xlsx"],
            "Type": ["PDF", "DOCX", "XLSX"],
            "Date": ["2026-07-15", "2026-07-14", "2026-07-13"],
            "Status": ["Indexed", "Indexed", "Processing"]
        }),
        use_container_width=True,
        hide_index=True
    )