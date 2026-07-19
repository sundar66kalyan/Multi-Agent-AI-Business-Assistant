import streamlit as st


def show_settings():
    """Render the Settings page."""
    
    st.title("⚙ Enterprise Settings")
    st.caption("Configure your AI Business Assistant")
    st.divider()
    
    # General Settings
    st.subheader("🎨 General Settings")
    col1, col2 = st.columns(2)
    with col1:
        theme = st.selectbox("Theme", ["Enterprise Blue", "Dark", "Light"])
        llm = st.selectbox("LLM Provider", ["Gemini", "OpenAI", "Groq", "Ollama"])
    with col2:
        default_agent = st.selectbox(
            "Default Agent",
            ["General", "Finance", "HR", "Document", "Research", "Analytics", "Report"]
        )
        temperature = st.slider("Temperature", 0.0, 1.0, 0.2)
    
    # Model Settings
    st.divider()
    st.subheader("🤖 Model Configuration")
    max_tokens = st.slider("Maximum Tokens", 256, 4096, 1024)
    st.write(f"Current Limit: {max_tokens}")
    
    # Maintenance
    st.divider()
    st.subheader("🛠 Maintenance")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🧹 Clear Chat History", use_container_width=True):
            st.success("Chat history cleared.")
    with c2:
        if st.button("🔄 Rebuild Vector Database", use_container_width=True):
            st.success("Vector database rebuild started.")
    
    # System Information
    st.divider()
    st.subheader("ℹ System Information")
    st.info("""
        **Application:** Multi-Agent AI Business Assistant
        **Version:** 1.0.0
        **Developer:** Kalyana Sundar
        **Framework:** FastAPI + Streamlit + ChromaDB + Gemini
    """)