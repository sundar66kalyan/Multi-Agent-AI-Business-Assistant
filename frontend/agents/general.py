import streamlit as st


def show_general_agent():
    """Render the General Agent page."""
    
    st.title("🤖 General Agent")
    st.caption("AI-powered general business assistance")
    
    st.info("""
    **General Agent Capabilities:**
    - General business queries
    - Document search
    - Data analysis
    - Task automation
    - Multi-domain support
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Queries Answered", "2,847", "+234")
        st.metric("User Ratings", "4.8/5", "+0.2")
    with col2:
        st.metric("Success Rate", "97.5%", "+1.2%")
        st.metric("Avg. Response", "2.4 sec", "-0.3 sec")
    with col3:
        st.metric("Active Sessions", "12", "+4")
        st.metric("Knowledge Base", "247 docs", "+18")