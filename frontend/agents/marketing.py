import streamlit as st


def show_marketing_agent():
    """Render the Marketing Agent page."""
    
    st.title("📢 Marketing Agent")
    st.caption("AI-powered marketing analytics and campaigns")
    
    st.info("""
    **Marketing Agent Capabilities:**
    - Campaign analytics
    - Social media insights
    - Brand monitoring
    - Lead generation
    - ROI analysis
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Campaigns Active", "12", "+3")
        st.metric("Click-through Rate", "4.2%", "+0.8%")
    with col2:
        st.metric("Lead Generation", "284", "+45")
        st.metric("Conversion Rate", "18.5%", "+2.3%")
    with col3:
        st.metric("Social Reach", "45K", "+12K")
        st.metric("ROI", "320%", "+45%")