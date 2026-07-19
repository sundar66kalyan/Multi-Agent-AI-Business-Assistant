import streamlit as st
from pathlib import Path
import webbrowser
from PIL import Image

from dashboard.api import DashboardAPI
from auth import AuthService
from app.core.permissions import ROLE_PERMISSIONS
from app.services.permission_service import PermissionService
from .metric_card import metric_card


def add_notification(icon, message):
    """Add a notification to the session state."""
    st.session_state.notifications.insert(0, (icon, message))
    if len(st.session_state.notifications) > 15:
        st.session_state.notifications.pop()


def add_activity(message):
    """Add an activity to the activity log."""
    st.session_state.activity_log.insert(
        0,
        {
            "time": st.session_state.get("current_time", "00:00:00"),
            "activity": message
        }
    )
    if len(st.session_state.activity_log) > 50:
        st.session_state.activity_log.pop()


def render_sidebar():
    """Render the sidebar with user profile, navigation, and system info."""
    
    with st.sidebar:
        
        # USER PROFILE — EXPANDER
        user = st.session_state.user
        
        with st.expander(f"👤 {user.get('name', 'User')}", expanded=True):
            
            st.success("🟢 Online")
            
            role = user.get("role", "User")
            
            if role == "Administrator":
                st.success("🛡 Administrator")
            elif role == "Manager":
                st.warning("👔 Manager")
            else:
                st.info("👤 User")
            
            role_pages = ROLE_PERMISSIONS.get(user.get("role", "User"), [])
            st.info(f"Access Level : {len(role_pages)} Modules")
            
            st.divider()
            
            if st.button("👤 My Profile", use_container_width=True):
                with st.container(border=True):
                    st.subheader("👤 User Profile")
                    col1, col2 = st.columns(2)
                    with col1:
                        st.text_input("Full Name", value=user.get("name", ""), disabled=True)
                        st.text_input("Username", value=user.get("username", ""), disabled=True)
                    with col2:
                        st.text_input("Email", value=user.get("email", ""), disabled=True)
                        st.text_input("Role", value=user.get("role", "User"), disabled=True)
                        st.text_input("Status", value="Online", disabled=True)
                    st.success("Profile loaded successfully.")
            
            # Preferences Toggle
            if st.button("⚙ Preferences", use_container_width=True):
                st.session_state.show_preferences = not st.session_state.show_preferences
            
            if st.session_state.show_preferences:
                with st.container(border=True):
                    st.subheader("⚙ Preferences")
                    
                    theme = st.selectbox(
                        "Theme",
                        ["Enterprise Blue", "Dark", "Light"],
                        index=["Enterprise Blue", "Dark", "Light"].index(
                            st.session_state.preferences["theme"]
                        )
                    )
                    
                    language = st.selectbox(
                        "Language",
                        ["English", "Tamil", "Hindi"],
                        index=["English", "Tamil", "Hindi"].index(
                            st.session_state.preferences["language"]
                        )
                    )
                    
                    notifications_toggle = st.toggle(
                        "Enable Notifications",
                        value=st.session_state.preferences["notifications"]
                    )
                    
                    auto_save = st.toggle(
                        "Auto Save Chat",
                        value=st.session_state.preferences["auto_save"]
                    )
                    
                    if st.button("💾 Save Preferences"):
                        st.session_state.preferences = {
                            "theme": theme,
                            "language": language,
                            "notifications": notifications_toggle,
                            "auto_save": auto_save
                        }
                        st.success("✔ Preferences saved successfully!")
                        add_activity("Preferences Updated")
                        st.write(f"🎨 Theme : {st.session_state.preferences['theme']}")
                        st.write(f"🌍 Language : {st.session_state.preferences['language']}")
                        st.write(f"🔔 Notifications : {'Enabled' if st.session_state.preferences['notifications'] else 'Disabled'}")
                        st.write(f"💾 Auto Save : {'Enabled' if st.session_state.preferences['auto_save'] else 'Disabled'}")
            
            # Activity Panel
            if st.button("📊 Activity", use_container_width=True):
                with st.container(border=True):
                    st.subheader("📊 Recent Activity")
                    for item in st.session_state.activity_log[:10]:
                        st.info(f"🕒 {item['time']}\n\n**{item['activity']}**")
            
            st.divider()
            
            if st.button("🚪 Logout", use_container_width=True):
                add_activity("Logged out")
                AuthService.logout()
                st.rerun()
        
        st.markdown("---")
        
        # Notification Counter
        notifications = st.session_state.notifications
        st.metric("🔔 Unread Notifications", len(notifications))
        st.markdown("---")
        
        # Company Branding
        logo_path = Path("frontend/assets/logo/logo.png")
        if logo_path.exists():
            logo = Image.open(logo_path)
            st.image(logo, width=90)
        
        st.markdown(
            """
            # Kalyana Sundar
            ### AI Solutions
            Enterprise AI Business Platform
            """
        )
        st.markdown("---")
        
        # Role-Based Navigation
        PAGE_LABELS = {
            "Dashboard": "🏠 Dashboard",
            "AI Chat": "💬 AI Chat",
            "Knowledge Base": "📚 Knowledge Base",
            "Upload Documents": "📤 Upload Documents",
            "Analytics": "📊 Analytics",
            "Agents": "🤖 Agents",
            "Users": "👥 Users",
            "Reports": "📄 Reports",
            "Settings": "⚙️ Settings",
            "Sales Agent": "💰 Sales Agent",
            "Finance Agent": "💳 Finance Agent",
            "HR Agent": "👔 HR Agent",
            "Marketing Agent": "📢 Marketing Agent",
            "Research Agent": "🔬 Research Agent",
            "Analytics Agent": "📊 Analytics Agent",
            "Document Agent": "📄 Document Agent",
            "Report Agent": "📋 Report Agent",
            "General Agent": "🤖 General Agent"
        }
        
        pages = ROLE_PERMISSIONS.get(user.get("role", "User"), [])
        
        if "page" not in st.session_state:
            st.session_state.page = pages[0] if pages else "Dashboard"
        
        for page_name in pages:
            label = PAGE_LABELS.get(page_name, page_name)
            if st.button(label, use_container_width=True):
                st.session_state.page = page_name
                st.rerun()
        
        page = st.session_state.page
        st.markdown("---")
        
        # Display Notifications
        st.subheader("🔔 Notifications")
        for icon, text in notifications:
            st.info(f"{icon} {text}")
        st.markdown("---")
        
        # Quick Actions
        st.subheader("Quick Actions")
        
        if st.button("📥 Download PDF Report", use_container_width=True):
            webbrowser.open(DashboardAPI.export_pdf())
            add_activity("Downloaded PDF Report")
            add_notification("📄", "PDF Report downloaded.")
        
        if st.button("📊 Download Excel", use_container_width=True):
            webbrowser.open(DashboardAPI.export_excel())
            add_activity("Downloaded Excel Report")
            add_notification("📊", "Excel Report downloaded.")
        
        if st.button("📝 Download DOCX", use_container_width=True):
            webbrowser.open(DashboardAPI.export_docx())
            add_activity("Downloaded DOCX Report")
            add_notification("📝", "DOCX Report downloaded.")
        
        st.markdown("---")
        
        # System Status
        summary = DashboardAPI.get_dashboard()
        
        if summary["success"]:
            dashboard = summary["dashboard"]
            st.success("API Connected")
            st.info(f"🤖 {len(dashboard['agents'])} Agents Active")
            st.info(f"📄 {dashboard['analytics']['documents']} Documents")
            st.info("💬 Chat Ready")
        else:
            st.error("Dashboard API unavailable")
        
        st.markdown("---")
        st.caption("Enterprise Edition v1.0.0")
    
    return page


# These functions are kept here for compatibility with existing code
# They will be imported from this module