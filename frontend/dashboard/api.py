import os
import requests
import streamlit as st

API_URL = os.getenv(
    "BACKEND_URL",
    "http://127.0.0.1:8000"
)


class DashboardAPI:

    @staticmethod
    def get_dashboard():
        try:
            headers = {}

            if "token" in st.session_state:
                headers["Authorization"] = (
                    f"Bearer {st.session_state.token}"
                )

            response = requests.get(
                f"{API_URL}/dashboard/summary",
                headers=headers,
                timeout=15
            )

            return response.json()

        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "dashboard": {
                    "agents": [],
                    "rag": {
                        "documents_loaded": 0
                    }
                }
            }

    @staticmethod
    def get_metrics():
        try:
            return requests.get(
                f"{API_URL}/dashboard/metrics"
            ).json()
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "metrics": {
                    "revenue": 0,
                    "expenses": 0,
                    "profit": 0,
                    "profit_margin": 0,
                    "documents": 0,
                    "chunks": 0,
                    "finance_records": 0
                }
            }

    @staticmethod
    def get_agents():
        try:
            dashboard = DashboardAPI.get_dashboard()

            return {
                "success": dashboard.get("success", False),
                "agents": dashboard.get("dashboard", {}).get("agents", [])
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "agents": []
            }

    @staticmethod
    def get_finance_chart():
        try:
            return requests.get(
                f"{API_URL}/dashboard/charts/finance"
            ).json()
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "chart": {
                    "labels": ["Revenue", "Expenses", "Profit"],
                    "values": [0, 0, 0]
                }
            }

    @staticmethod
    def get_health():
        try:
            return requests.get(
                f"{API_URL}/dashboard/health/check-db"
            ).json()
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "status": "Unavailable"
            }

    @staticmethod
    def export_pdf():
        return f"{API_URL}/report/pdf"

    @staticmethod
    def export_excel():
        return f"{API_URL}/report/excel"

    @staticmethod
    def export_docx():
        return f"{API_URL}/report/docx"

    @staticmethod
    def chat(message: str):
        """
        Send a chat message to the AI assistant.
        
        Args:
            message (str): User message to send
            
        Returns:
            dict: Response from the AI assistant
        """
        try:
            response = requests.post(
                f"{API_URL}/chat",
                json={
                    "message": message
                }
            )
            return response.json()
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "answer": "Sorry, I'm unable to process your request at the moment.",
                "agent": "Error",
                "sources": [],
                "confidence": 0,
                "response_time": "0.00 sec"
            }

    @staticmethod
    def get_notifications():
        """
        Get all notifications from the API.
        
        Returns:
            dict: Notifications data with count and list
        """
        try:
            response = requests.get(
                f"{API_URL}/notifications",
                timeout=5
            )
            
            if response.status_code == 200:
                data = response.json()
                
                # Ensure consistent format
                if "notifications" in data:
                    return {
                        "count": len(data["notifications"]),
                        "notifications": data["notifications"],
                        "success": True
                    }
                elif "data" in data and "notifications" in data["data"]:
                    notifications = data["data"]["notifications"]
                    return {
                        "count": len(notifications),
                        "notifications": notifications,
                        "success": True
                    }
                else:
                    # Try to handle different response formats
                    return {
                        "count": 0,
                        "notifications": [],
                        "success": True,
                        "message": "No notifications found"
                    }
            else:
                # Return empty notifications on error
                return {
                    "count": 0,
                    "notifications": [],
                    "success": False,
                    "error": f"API returned status {response.status_code}"
                }
                
        except requests.exceptions.Timeout:
            return {
                "count": 0,
                "notifications": [],
                "success": False,
                "error": "Request timeout"
            }
        except requests.exceptions.ConnectionError:
            return {
                "count": 0,
                "notifications": [],
                "success": False,
                "error": "Connection error - API may be offline"
            }
        except Exception as e:
            # Return empty notifications on error
            return {
                "count": 0,
                "notifications": [],
                "success": False,
                "error": str(e)
            }

    @staticmethod
    def mark_notification_read(notification_id: int):
        """
        Mark a notification as read.
        
        Args:
            notification_id (int): ID of the notification to mark as read
            
        Returns:
            dict: Response from the API
        """
        try:
            response = requests.post(
                f"{API_URL}/notifications/mark-read/{notification_id}"
            )
            return response.json()
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    @staticmethod
    def mark_all_notifications_read():
        """
        Mark all notifications as read.
        
        Returns:
            dict: Response from the API
        """
        try:
            response = requests.post(
                f"{API_URL}/notifications/mark-all-read"
            )
            return response.json()
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    @staticmethod
    def delete_notification(notification_id: int):
        """
        Delete a notification.
        
        Args:
            notification_id (int): ID of the notification to delete
            
        Returns:
            dict: Response from the API
        """
        try:
            response = requests.delete(
                f"{API_URL}/notifications/{notification_id}"
            )
            return response.json()
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    # ============================================================
    # ✅ FIXED: Upload PDF - /upload-pdf endpoint
    # ============================================================
    
    @staticmethod
    def upload_pdf(uploaded_file):
        """Upload a PDF document to the knowledge base"""

        try:

            headers = {}

            if "token" in st.session_state:
                headers["Authorization"] = (
                    f"Bearer {st.session_state.token}"
                )

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "application/pdf"
                )
            }

            response = requests.post(
                f"{API_URL}/upload-pdf",  # ✅ FIXED: Changed from /upload to /upload-pdf
                files=files,
                headers=headers,
                timeout=120
            )

            return response.json()

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

    # ============================================================
    # ✅ FIXED: Get Documents - /knowledge-base endpoint
    # ============================================================
    
    @staticmethod
    def get_documents():
        """List indexed documents from the knowledge base"""

        try:

            headers = {}

            if "token" in st.session_state:
                headers["Authorization"] = (
                    f"Bearer {st.session_state.token}"
                )

            response = requests.get(
                f"{API_URL}/knowledge-base",  # ✅ FIXED: Changed from /documents to /knowledge-base
                headers=headers
            )

            return response.json()

        except Exception as e:

            return {
                "total_documents": 0,  # ✅ FIXED: Added total_documents field
                "documents": [],
                "error": str(e)
            }

    @staticmethod
    def search_documents(query):

        try:

            headers = {}

            if "token" in st.session_state:
                headers["Authorization"] = (
                    f"Bearer {st.session_state.token}"
                )

            response = requests.post(
                f"{API_URL}/search",
                json={
                    "query": query
                },
                headers=headers
            )

            return response.json()

        except Exception as e:

            return {
                "success": False,
                "results": [],
                "error": str(e)
            }

    @staticmethod
    def rebuild_index():

        try:

            headers = {}

            if "token" in st.session_state:
                headers["Authorization"] = (
                    f"Bearer {st.session_state.token}"
                )

            response = requests.post(
                f"{API_URL}/rebuild",
                headers=headers
            )

            return response.json()

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }