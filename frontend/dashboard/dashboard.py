import streamlit as st

from frontend.dashboard.api import DashboardAPI


st.set_page_config(
    page_title="Enterprise Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Multi-Agent AI Business Assistant")

metrics = DashboardAPI.get_metrics()

if not metrics["success"]:
    st.error("Unable to load dashboard.")
    st.stop()

data = metrics["metrics"]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Revenue",
        f"₹ {data['revenue']:,.0f}"
    )

with col2:
    st.metric(
        "Expenses",
        f"₹ {data['expenses']:,.0f}"
    )

with col3:
    st.metric(
        "Profit",
        f"₹ {data['profit']:,.0f}"
    )

with col4:
    st.metric(
        "Profit Margin",
        f"{data['profit_margin']} %"
    )

st.divider()

st.subheader("System Statistics")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Documents",
        data["documents"]
    )

with c2:
    st.metric(
        "Chunks",
        data["chunks"]
    )

with c3:
    st.metric(
        "Finance Records",
        data["finance_records"]
    )