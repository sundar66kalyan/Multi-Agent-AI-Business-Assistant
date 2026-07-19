import streamlit as st


def show_users():
    """Users Management"""

    st.title("👥 Users")
    st.caption("Enterprise User Management")

    user = st.session_state.user

    st.subheader("Current User")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Name", user.get("name", ""))

    with col2:
        st.metric("Role", user.get("role", ""))

    with col3:
        st.metric("Status", "Online")

    st.divider()

    st.subheader("User Information")

    st.text_input(
        "Name",
        value=user.get("name", ""),
        disabled=True,
    )

    st.text_input(
        "Email",
        value=user.get("email", ""),
        disabled=True,
    )

    st.text_input(
        "Role",
        value=user.get("role", ""),
        disabled=True,
    )

    st.divider()

    st.success("User authenticated successfully.")