import streamlit as st
import requests
import os

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://127.0.0.1:8000"
)


class AuthService:

    @staticmethod
    def initialize():

        if "logged_in" not in st.session_state:
            st.session_state.logged_in = False

        if "username" not in st.session_state:
            st.session_state.username = ""

        if "name" not in st.session_state:
            st.session_state.name = ""

        if "role" not in st.session_state:
            st.session_state.role = ""

        if "user" not in st.session_state:
            st.session_state.user = {}

        if "token" not in st.session_state:
            st.session_state.token = ""

    @staticmethod
    def login(username, password):

        try:

            response = requests.post(
                f"{BACKEND_URL}/login",
                json={
                    "email": username,
                    "password": password
                },
                timeout=10
            )

            if response.status_code != 200:
                st.error("Invalid email or password.")
                return False

            data = response.json()
            
            st.session_state.token = data.get("access_token", "")
           
            user = data.get("user", {})

            st.session_state.logged_in = True

            st.session_state.username = user.get("email", username)

            st.session_state.name = user.get("name", username)

            st.session_state.role = user.get("role", "User")

            st.session_state.user = user

            return True

        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to the backend server.")
            return False

        except Exception as e:
            st.error(str(e))
            return False

    @staticmethod
    def logout():

        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.name = ""
        st.session_state.role = ""
        st.session_state.user = {}
        st.session_state.token = ""

    @staticmethod
    def is_authenticated():

        return st.session_state.get("logged_in", False)

    @staticmethod
    def get_current_user():

        return st.session_state.get("user", None)

    @staticmethod
    def get_current_role():

        return st.session_state.get("role", "")