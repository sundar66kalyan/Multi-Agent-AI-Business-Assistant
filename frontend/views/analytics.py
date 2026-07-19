import streamlit as st
import plotly.express as px
import pandas as pd

from dashboard.api import DashboardAPI
from components.metric_card import metric_card


def show_analytics():
    """Analytics Dashboard"""

    st.title("📊 Analytics Dashboard")
    st.caption("Enterprise Business Analytics")

    metrics = DashboardAPI.get_metrics()

    if not metrics["success"]:
        st.error("Unable to load analytics.")
        return

    data = metrics["metrics"]

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card(
            "Documents",
            data["documents"],
            "+2",
            "📄",
        )

    with c2:
        metric_card(
            "Chunks",
            data["chunks"],
            "+18",
            "🧩",
        )

    with c3:
        metric_card(
            "Revenue",
            f"₹{data['revenue']:,.0f}",
            "+12%",
            "💰",
        )

    with c4:
        metric_card(
            "Profit",
            f"₹{data['profit']:,.0f}",
            "+18%",
            "📈",
        )

    st.divider()

    df = pd.DataFrame(
        {
            "Metric": [
                "Revenue",
                "Expenses",
                "Profit",
            ],
            "Value": [
                data["revenue"],
                data["expenses"],
                data["profit"],
            ],
        }
    )

    fig = px.bar(
        df,
        x="Metric",
        y="Value",
        text="Value",
        title="Business Performance",
    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    st.divider()

    st.subheader("Business Summary")

    st.success(
        f"""
Revenue : ₹{data['revenue']:,.0f}

Expenses : ₹{data['expenses']:,.0f}

Profit : ₹{data['profit']:,.0f}

Documents : {data['documents']}

Finance Records : {data['finance_records']}
"""
    )