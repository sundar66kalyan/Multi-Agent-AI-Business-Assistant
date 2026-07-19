import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime

from dashboard.api import DashboardAPI
from components.metric_card import metric_card


def show_dashboard():
    """Render the Dashboard page."""
    
    st.title("📊 Multi-Agent AI Business Assistant")
    
    # Welcome Banner
    st.info(
        f"""
## 👋 Welcome, {st.session_state.username}

Enterprise AI Business Platform

✔ 9 AI Agents Online
✔ API Connected
✔ Reports Available
✔ Vector Database Ready
"""
    )
    
    # Live System Clock
    st.caption(f"🕒 Last Updated : {datetime.now().strftime('%d-%b-%Y %H:%M:%S')}")
    
    # Activity History
    st.subheader("📜 Activity History")
    for item in st.session_state.activity_log[:20]:
        with st.container(border=True):
            col1, col2 = st.columns([1, 5])
            with col1:
                st.write(item["time"])
            with col2:
                st.write(item["activity"])
    
    # Initialize search session state
    if "recent_searches" not in st.session_state:
        st.session_state.recent_searches = []
    if "search_query" not in st.session_state:
        st.session_state.search_query = ""
    
    # Global Search
    st.markdown("### 🔍 Global Search")
    search_query = st.text_input(
        "Search",
        value=st.session_state.search_query,
        placeholder="Search documents, reports, AI agents...",
        label_visibility="collapsed"
    )
    
    if search_query:
        if search_query not in st.session_state.recent_searches:
            st.session_state.recent_searches.insert(0, search_query)
        st.session_state.recent_searches = st.session_state.recent_searches[:5]
        if st.session_state.search_query and st.session_state.search_query == search_query:
            st.session_state.search_query = ""
    
    # Quick Search
    st.markdown("### 💡 Quick Search")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("📄 Reports"):
            st.session_state.search_query = "Reports"
            st.rerun()
    with col2:
        if st.button("👥 Employees"):
            st.session_state.search_query = "Employee"
            st.rerun()
    with col3:
        if st.button("💰 Finance"):
            st.session_state.search_query = "Finance"
            st.rerun()
    with col4:
        if st.button("🤖 AI Agents"):
            st.session_state.search_query = "Agent"
            st.rerun()
    
    # Search Results
    if search_query:
        sample_results = [
            "Finance Report Q2",
            "Employee Handbook",
            "HR Leave Policy",
            "Sales Dashboard",
            "Research Agent",
            "Analytics Report",
            "Marketing Strategy",
            "Expense Summary"
        ]
        results = [item for item in sample_results if search_query.lower() in item.lower()]
        if results:
            st.success(f"{len(results)} result(s) found")
            for result in results:
                st.write(f"📄 {result}")
        else:
            st.warning("No matching records found.")
    
    # Recent Searches
    st.markdown("### 🕒 Recent Searches")
    if st.session_state.recent_searches:
        for item in st.session_state.recent_searches:
            st.write(f"🔍 {item}")
    else:
        st.info("No recent searches.")
    
    # Dashboard Filters
    st.subheader("📌 Dashboard Filters")
    f1, f2, f3, f4 = st.columns([2, 2, 2, 1])
    with f1:
        month = st.selectbox("Month", ["January", "February", "March", "April", "May", "June"])
    with f2:
        agent = st.selectbox("Agent", ["All", "Finance", "HR", "Research", "Marketing", "Sales"])
    with f3:
        report = st.selectbox("Report", ["Finance", "Analytics", "HR", "Marketing"])
    with f4:
        st.write("")
        st.write("")
        if "refresh" not in st.session_state:
            st.session_state.refresh = 1
        if st.button("🔄 Refresh", use_container_width=True):
            st.session_state.refresh += 1
            st.success("Dashboard refreshed.")
        st.caption(f"Refreshed {st.session_state.refresh} times")
    
    st.divider()
    
    # Fetch metrics
    metrics = DashboardAPI.get_metrics()
    if not metrics["success"]:
        st.error("Unable to load dashboard.")
        return
    data = metrics["metrics"]
    
    chart = DashboardAPI.get_finance_chart()
    agents = DashboardAPI.get_agents()
    health = DashboardAPI.get_health()
    
    # Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        metric_card("Revenue", f"₹{data['revenue']:,.0f}", "12%", "💰")
    with col2:
        metric_card("Expenses", f"₹{data['expenses']:,.0f}", "5%", "💳")
    with col3:
        metric_card("Profit", f"₹{data['profit']:,.0f}", "18%", "📈")
    with col4:
        metric_card("Margin", f"{data['profit_margin']}%", "3%", "📊")
    
    st.divider()
    
    # Dashboard Notifications
    with st.expander("🔔 Notifications"):
        st.success("Finance report generated.")
        st.info("7 documents indexed.")
        st.warning("No pending approvals.")
        st.success("All AI agents are online.")
    
    # Enterprise Dashboard Tabs
    tab1, tab2, tab3 = st.tabs(["📈 Business Overview", "🤖 AI Agents", "❤️ System Health"])
    
    with tab1:
        st.subheader("📊 Business Metrics")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Documents", data["documents"])
        with c2:
            st.metric("Chunks", data["chunks"])
        with c3:
            st.metric("Finance Records", data["finance_records"])
        
        st.divider()
        st.subheader("📈 Financial Overview")
        chart_data = pd.DataFrame({
            "Metric": chart["chart"]["labels"],
            "Amount": chart["chart"]["values"]
        })
        fig = px.bar(
            chart_data,
            x="Metric",
            y="Amount",
            text="Amount",
            title="Revenue vs Expenses vs Profit"
        )
        fig.update_traces(textposition="outside")
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("🤖 Registered AI Agents")
        agent_rows = []
        for agent in agents["agents"]:
            agent_rows.append({
                "Agent": agent["name"],
                "Status": agent["status"],
                "Description": agent["description"]
            })
        agent_df = pd.DataFrame(agent_rows)
        st.dataframe(agent_df, use_container_width=True, hide_index=True)
    
    with tab3:
        st.subheader("❤️ System Health")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.success("🗄 Database")
            st.write(health["status"])
        with c2:
            st.success("🚀 API")
            st.write("Running")
        with c3:
            st.success("🤖 AI Services")
            st.write("Available")
    
    # Recent Activity & Business Health
    st.divider()
    left, right = st.columns([2, 1])
    
    with left:
        st.subheader("🕒 Recent Activity")
        activities = [
            ("✅ PDF Report Generated", "2 min ago"),
            ("📄 Employee Handbook Indexed", "10 min ago"),
            ("💰 Finance Data Updated", "25 min ago"),
            ("🤖 AI Chat Session Started", "40 min ago"),
            ("📊 Dashboard Refreshed", "1 hour ago")
        ]
        for activity, time in activities:
            st.info(f"**{activity}**\n\n{time}")
    
    with right:
        st.subheader("🟢 Business Health")
        st.success("Database Connected")
        st.success("Vector DB Ready")
        st.success("9 AI Agents Online")
        st.success("API Running")
        st.success("Reports Available")
    
    st.divider()
    st.caption("© 2026 Kalyana Sundar AI Solutions | Enterprise AI Business Platform | Version 1.0")