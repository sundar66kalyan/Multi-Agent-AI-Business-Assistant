import time
from datetime import datetime
import streamlit as st
from dashboard.api import DashboardAPI


def show_ai_chat():
    """Enterprise AI Business Chat"""

    st.title("💬 AI Business Assistant")
    st.caption(
        "Ask questions about Finance, HR, Sales, Documents, Reports, Analytics and more."
    )

    col1, col2 = st.columns([8, 2])

    with col2:
        if st.button("🗑 Clear Chat"):
            st.session_state.chat_history = []
            st.rerun()

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Export conversation button
    if st.session_state.chat_history:
        export_text = ""
        
        for item in st.session_state.chat_history:
            export_text += (
                f"User : {item['user']}\n\n"
                f"{item['agent']} Agent:\n"
                f"{item['assistant']}\n\n"
                + "-" * 70
                + "\n\n"
            )
        
        st.download_button(
            "💾 Export Conversation",
            export_text,
            file_name="AI_Conversation.txt",
            mime="text/plain",
            use_container_width=True,
        )

    # ---------------------------------------------------------
    # Suggested Questions
    # ---------------------------------------------------------

    st.subheader("💡 Suggested Questions")

    suggestions = [
        "Show finance summary",
        "What is the leave policy?",
        "Generate employee report",
        "Business analytics",
        "Revenue this month"
    ]

    cols = st.columns(len(suggestions))

    # Store selected prompt from buttons
    selected_prompt = None

    for i, question in enumerate(suggestions):
        if cols[i].button(question, use_container_width=True):
            selected_prompt = question

    # Chat input takes priority, but falls back to selected prompt
    prompt = st.chat_input("Ask your business question...")

    if prompt is None:
        prompt = selected_prompt

    if prompt:

        with st.spinner("Thinking..."):

            start_time = time.time()
            response = DashboardAPI.chat(prompt)
            response_time = round(
                time.time() - start_time,
                2
            )
            
            #st.json(response)

            # ============================================================
            # ✅ FIXED: Robust response handling with fallbacks
            # ============================================================
            
            if response.get("success"):

                # Handle direct General AI response
                if response.get("answer"):

                    answer = response["answer"]
                    agent = response.get("agent", "General")
                    sources = response.get("sources", [])

                # Analytics response
                elif response.get("agent") == "Analytics":

                    analytics = response.get("system", {})

                    answer = f"""
📄 Documents : {analytics.get('documents', 0)}

🧩 Chunks : {analytics.get('chunks', 0)}

💼 Finance Records : {analytics.get('finance_records', 0)}

🤖 Registered Agents : {analytics.get('registered_agents', 0)}
"""

                    agent = "Analytics"
                    sources = []

                # Finance response
                elif response.get("agent") == "Finance":
                    finance = response.get("data", {})

                    answer = f"""
📅 Month : {finance.get('month', 'N/A')}

💰 Revenue : ₹{finance.get('revenue', 0):,}

💸 Expenses : ₹{finance.get('expenses', 0):,}

📈 Profit : ₹{finance.get('profit', 0):,}
"""

                    agent = "Finance"
                    sources = []

                # New Multi-Agent response
                elif "report" in response:

                    answer = response["report"].get("report", "")
                    agent = "Report"
                    sources = []

                elif "result" in response:

                    result = response["result"]
                    agent = response.get("agent", "System")
                    
                    # Handle direct answer returned by backend
                    if "answer" in response:
                        answer = response["answer"]
                        sources = response.get("sources", [])

                    if agent == "Finance":

                        finance = result.get("data", {})

                        answer = f"""
📅 Month : {finance.get('month','N/A')}

💰 Revenue : ₹{finance.get('revenue',0):,}

💸 Expenses : ₹{finance.get('expenses',0):,}

📈 Profit : ₹{finance.get('profit',0):,}
"""

                        sources = []

                    elif agent in ["HR", "Document"]:

                        answer = result.get("answer", "No response")
                        sources = result.get("sources", [])

                    elif agent == "Analytics":

                        analytics = result.get("system", {})

                        answer = f"""
📄 Documents : {analytics.get('documents',0)}

🧩 Chunks : {analytics.get('chunks',0)}

💼 Finance Records : {analytics.get('finance_records',0)}

🤖 Registered Agents : {analytics.get('registered_agents',0)}
"""

                        sources = []

                    elif agent == "Report":

                        answer = result.get("report", "")
                        sources = []

                    elif agent == "General":

                        answer = result.get("answer", "No response")
                        sources = []

                    else:

                        answer = str(result)
                        sources = []

                # -------------------------------
                # OLD MULTI-AGENT FORMAT
                # -------------------------------
                else:

                    raw = response.get("raw_results", {})

                    if response.get("report"):

                        answer = response["report"].get("report", "")
                        agent = "Report"
                        sources = []

                    elif "Finance" in raw:

                        finance = raw["Finance"]["data"]

                        answer = f"""
📅 Month : {finance.get('month','N/A')}

💰 Revenue : ₹{finance.get('revenue',0):,}

💸 Expenses : ₹{finance.get('expenses',0):,}

📈 Profit : ₹{finance.get('profit',0):,}
"""

                        agent = "Finance"
                        sources = []

                    elif "Document" in raw:

                        answer = raw["Document"].get("answer", "")
                        agent = "Document"
                        sources = raw["Document"].get("sources", [])

                    elif "Analytics" in raw:

                        analytics = raw["Analytics"]["system"]

                        answer = f"""
📄 Documents : {analytics.get('documents',0)}

🧩 Chunks : {analytics.get('chunks',0)}

💼 Finance Records : {analytics.get('finance_records',0)}

🤖 Registered Agents : {analytics.get('registered_agents',0)}
"""

                        agent = "Analytics"
                        sources = []

                    else:

                        answer = response.get("message", "No response")
                        agent = "System"
                        sources = []

            else:

                if response.get("answer"):
                    answer = response["answer"]
                else:
                    answer = response.get("detail", "Unable to process request.")

                agent = response.get("agent", "System")
                sources = response.get("sources", [])

        # Store in session state with sources, timestamp, response time, and animation flag
        st.session_state.chat_history.append(
            {
                "user": prompt,
                "assistant": answer,
                "agent": agent,
                "sources": sources,
                "time": datetime.now().strftime("%I:%M %p"),
                "response_time": response_time,
                "animated": False,
            }
        )

    st.divider()

    # Agent icons mapping
    agent_icons = {
        "Finance": "💰",
        "Analytics": "📊",
        "Document": "📄",
        "Report": "📈",
        "Sales": "🛒",
        "Marketing": "📢",
        "Research": "🔍",
        "HR": "👥",
        "General": "🤖",
        "System": "⚙️"
    }

    for item in reversed(st.session_state.chat_history):

        with st.chat_message("user"):
            st.write(item["user"])

        with st.chat_message("assistant"):

            with st.container():

                col1, col2 = st.columns([1, 9])

                with col1:
                    st.markdown(
                        agent_icons.get(
                            item["agent"],
                            "🤖"
                        )
                    )

                with col2:
                    st.markdown(
                        f"""
**{item['agent']} Agent**

<small>
🕒 {item['time']} &nbsp;&nbsp;&nbsp;
⚡ {item.get('response_time', 0)} sec
</small>
""",
                        unsafe_allow_html=True,
                    )

                    if item["agent"] == "Report":
                        with st.expander("📈 Executive Business Report", expanded=True):
                            st.markdown(item["assistant"])
                            
                            st.download_button(
                                label="📥 Download Report",
                                data=item["assistant"],
                                file_name="Executive_Report.txt",
                                mime="text/plain",
                                use_container_width=True,
                            )
                    else:
                        # Typing animation for new messages only
                        if not item.get("animated", False):
                            placeholder = st.empty()
                            text = ""
                            
                            for word in item["assistant"].split():
                                text += word + " "
                                placeholder.markdown(text)
                                time.sleep(0.015)
                            
                            item["animated"] = True
                        else:
                            st.markdown(item["assistant"])
            
            # Display sources if available
            sources = item.get("sources", [])
            
            if sources:
                st.markdown("#### 📄 Sources")
                
                for src in sources:
                    # Handle different source formats
                    if isinstance(src, dict):
                        doc_name = src.get("document", src.get("source", "Unknown"))
                        page = src.get("page", 0)
                        # Page numbers might be 0-indexed, add 1 for display
                        page_display = page + 1 if isinstance(page, int) else page
                        st.caption(f"📄 {doc_name} (Page {page_display})")
                    else:
                        # If source is just a string
                        st.caption(f"📄 {src}")