import streamlit as st

st.set_page_config(
    page_title="Enterprise Dashboard",
    page_icon="📊",
    layout="wide",
)

# ============================================================
# PROJECT ROOT PATH FIX
# ============================================================

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BACKEND_PATH = PROJECT_ROOT / "backend"

if str(BACKEND_PATH) not in sys.path:
    sys.path.insert(0, str(BACKEND_PATH))

# ============================================================
# IMPORTS
# ============================================================

from datetime import datetime

from auth import AuthService
from app.services.permission_service import PermissionService

# ============================================================
# COMPONENTS
# ============================================================

from components import render_sidebar

# ============================================================
# VIEWS
# ============================================================

from views.dashboard import show_dashboard
from views.ai_chat import show_ai_chat
from views.analytics import show_analytics
from views.reports import show_reports
from views.settings import show_settings
from views.users import show_users
from views.knowledge_base import show_knowledge_base
from views.upload_documents import show_upload_documents

# ============================================================
# AGENTS
# ============================================================

from agents import (
    show_agents,
    show_sales_agent,
    show_finance_agent,
    show_hr_agent,
    show_marketing_agent,
    show_research_agent,
    show_analytics_agent,
    show_document_agent,
    show_report_agent,
    show_general_agent,
)

# ============================================================
# CSS LOADING
# ============================================================

def load_css():
    css_file = Path("frontend/assets/styles/theme.css")
    if css_file.exists():
        with open(css_file) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ============================================================
# INITIALIZE AUTHENTICATION
# ============================================================

AuthService.initialize()

# ============================================================
# INITIALIZE SESSION STATE
# ============================================================

if "show_preferences" not in st.session_state:
    st.session_state.show_preferences = False

if "preferences" not in st.session_state:
    st.session_state.preferences = {
        "theme": "Enterprise Blue",
        "language": "English",
        "notifications": True,
        "auto_save": True
    }

if "activity_log" not in st.session_state:
    st.session_state.activity_log = [
        {"time": datetime.now().strftime("%H:%M:%S"), "activity": "System Started"}
    ]

if "notifications" not in st.session_state:
    st.session_state.notifications = [
        ("🟢", "System Online"),
        ("📄", "Report Generated"),
        ("🤖", "AI Agents Running"),
        ("📥", "7 Documents Indexed"),
        ("👤", "Last Login Today")
    ]

# ============================================================
# LOGIN PAGE
# ============================================================

if not st.session_state.logged_in:
    st.markdown("# 🏢 Kalyana Sundar AI Solutions")
    st.caption("Enterprise AI Business Platform")
    st.markdown("---")
    
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.subheader("🔐 Login")
        username = st.text_input("Email")
        password = st.text_input("Password", type="password")
        login = st.button("🚀 Login", use_container_width=True)
        
        if login:
            if AuthService.login(username, password):
                st.session_state.page = "Dashboard"
                st.session_state.activity_log.insert(
                    0,
                    {"time": datetime.now().strftime("%H:%M:%S"), "activity": f"{st.session_state.username} logged in"}
                )
                st.success("Login successful.")
                st.rerun()
            else:
                st.error("Invalid username or password.")
        
        st.markdown("---")
        st.info("""
### Demo Accounts

**Administrator**
- Email: `admin@example.com`
- Password: `admin123`

**Manager**
- Email: `manager@example.com`
- Password: `manager123`

**User**
- Email: `user@example.com`
- Password: `user123`
""")
    st.stop()

load_css()

# ============================================================
# PROTECT THE SIDEBAR
# ============================================================

if "user" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

# ============================================================
# RENDER SIDEBAR AND GET CURRENT PAGE
# ============================================================

page = render_sidebar()

# ============================================================
# PAGE ACCESS CONTROL
# ============================================================

from app.core.permissions import ROLE_PERMISSIONS

user = st.session_state.user
if not PermissionService.has_permission(user["role"], page):
    st.error("⛔ Access Denied. You don't have permission to view this page.")
    st.stop()

# ============================================================
# RENDER PAGES
# ============================================================

if page == "Dashboard":
    show_dashboard()

elif page == "AI Chat":
    show_ai_chat()

elif page == "Analytics":
    show_analytics()

elif page == "Agents":
    show_agents()

elif page == "Users":
    show_users()

elif page == "Reports":
    show_reports()

elif page == "Settings":
    show_settings()

elif page == "Knowledge Base":
    show_knowledge_base()

# ✅ NEW: Upload Documents page routing
elif page == "Upload Documents":
    show_upload_documents()

elif page == "Sales Agent":
    show_sales_agent()

elif page == "Finance Agent":
    show_finance_agent()

elif page == "HR Agent":
    show_hr_agent()

elif page == "Marketing Agent":
    show_marketing_agent()

elif page == "Research Agent":
    show_research_agent()

elif page == "Analytics Agent":
    show_analytics_agent()

elif page == "Document Agent":
    show_document_agent()

elif page == "Report Agent":
    show_report_agent()

elif page == "General Agent":
    show_general_agent()