import streamlit as st
from dashboard.api import DashboardAPI


def show_agents():
    st.title("🤖 AI Agents")

    st.caption("Enterprise AI Agent Management")

    response = DashboardAPI.get_dashboard()

    if not response.get("success"):
        st.error("Unable to load agents.")
        return

    agents = response["dashboard"]["agents"]

    cols = st.columns(3)

    for i, agent in enumerate(agents):

        with cols[i % 3]:

            with st.container(border=True):

                st.subheader(f"🤖 {agent['name']}")

                st.success(agent["status"])

                st.write(agent["description"])

                if st.button(
                    f"Open {agent['name']}",
                    key=agent["name"]
                ):
                    st.session_state.page = f"{agent['name']} Agent"
                    st.rerun()