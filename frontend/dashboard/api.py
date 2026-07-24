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

            url = f"{API_URL}/dashboard/summary"
            print("=" * 60)
            print("REQUEST URL:", url)
            print("=" * 60)

            response = requests.get(
                url,
                headers=headers,
                timeout=60
            )

            print("=" * 60)
            print("STATUS:", response.status_code)
            print("BODY:", response.text)
            print("=" * 60)

            if response.status_code != 200:
                return {
                    "success": False,
                    "answer": response.text
                }

            try:
                data = response.json()
            except Exception:
                return {
                    "success": False,
                    "answer": response.text
                }

            return data

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
            url = f"{API_URL}/dashboard/metrics"
            print("=" * 60)
            print("REQUEST URL:", url)
            print("=" * 60)

            response = requests.get(
                url,
                timeout=60
            )

            print("=" * 60)
            print("STATUS:", response.status_code)
            print("BODY:", response.text)
            print("=" * 60)

            if response.status_code != 200:
                return {
                    "success": False,
                    "answer": response.text
                }

            try:
                data = response.json()
            except Exception:
                return {
                    "success": False,
                    "answer": response.text
                }

            return data

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
            url = f"{API_URL}/dashboard/charts/finance"
            print("=" * 60)
            print("REQUEST URL:", url)
            print("=" * 60)

            response = requests.get(
                url,
                timeout=60
            )

            print("=" * 60)
            print("STATUS:", response.status_code)
            print("BODY:", response.text)
            print("=" * 60)

            if response.status_code != 200:
                return {
                    "success": False,
                    "answer": response.text
                }

            try:
                data = response.json()
            except Exception:
                return {
                    "success": False,
                    "answer": response.text
                }

            return data

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
            url = f"{API_URL}/dashboard/health/check-db"
            print("=" * 60)
            print("REQUEST URL:", url)
            print("=" * 60)

            response = requests.get(
                url,
                timeout=60
            )

            print("=" * 60)
            print("STATUS:", response.status_code)
            print("BODY:", response.text)
            print("=" * 60)

            if response.status_code != 200:
                return {
                    "success": False,
                    "answer": response.text
                }

            try:
                data = response.json()
            except Exception:
                return {
                    "success": False,
                    "answer": response.text
                }

            return data

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
            url = f"{API_URL}/chat"
            payload = {"message": message}
            
            print("=" * 60)
            print("REQUEST URL:", url)
            print("REQUEST BODY:", payload)
            print("=" * 60)

            response = requests.post(
                url,
                json=payload,
                timeout=60
            )

            print("=" * 60)
            print("STATUS:", response.status_code)
            print("BODY:", response.text)
            print("=" * 60)

            if response.status_code != 200:
                return {
                    "success": False,
                    "answer": response.text
                }

            try:
                data = response.json()
            except Exception:
                return {
                    "success": False,
                    "answer": response.text
                }

            return data

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
            url = f"{API_URL}/notifications"
            print("=" * 60)
            print("REQUEST URL:", url)
            print("=" * 60)

            response = requests.get(
                url,
                timeout=60
            )

            print("=" * 60)
            print("STATUS:", response.status_code)
            print("BODY:", response.text)
            print("=" * 60)

            if response.status_code == 200:
                try:
                    data = response.json()
                except Exception:
                    return {
                        "count": 0,
                        "notifications": [],
                        "success": False,
                        "error": "Invalid JSON response"
                    }
                
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
            url = f"{API_URL}/notifications/mark-read/{notification_id}"
            print("=" * 60)
            print("REQUEST URL:", url)
            print("=" * 60)

            response = requests.post(
                url,
                timeout=60
            )

            print("=" * 60)
            print("STATUS:", response.status_code)
            print("BODY:", response.text)
            print("=" * 60)

            if response.status_code != 200:
                return {
                    "success": False,
                    "answer": response.text
                }

            try:
                data = response.json()
            except Exception:
                return {
                    "success": False,
                    "answer": response.text
                }

            return data

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
            url = f"{API_URL}/notifications/mark-all-read"
            print("=" * 60)
            print("REQUEST URL:", url)
            print("=" * 60)

            response = requests.post(
                url,
                timeout=60
            )

            print("=" * 60)
            print("STATUS:", response.status_code)
            print("BODY:", response.text)
            print("=" * 60)

            if response.status_code != 200:
                return {
                    "success": False,
                    "answer": response.text
                }

            try:
                data = response.json()
            except Exception:
                return {
                    "success": False,
                    "answer": response.text
                }

            return data

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
            url = f"{API_URL}/notifications/{notification_id}"
            print("=" * 60)
            print("REQUEST URL:", url)
            print("=" * 60)

            response = requests.delete(
                url,
                timeout=60
            )

            print("=" * 60)
            print("STATUS:", response.status_code)
            print("BODY:", response.text)
            print("=" * 60)

            if response.status_code != 200:
                return {
                    "success": False,
                    "answer": response.text
                }

            try:
                data = response.json()
            except Exception:
                return {
                    "success": False,
                    "answer": response.text
                }

            return data

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

            url = f"{API_URL}/upload-pdf"
            print("=" * 60)
            print("REQUEST URL:", url)
            print("UPLOADING FILE:", uploaded_file.name)
            print("=" * 60)

            response = requests.post(
                url,
                files=files,
                headers=headers,
                timeout=60
            )

            print("=" * 60)
            print("STATUS:", response.status_code)
            print("BODY:", response.text)
            print("=" * 60)

            if response.status_code != 200:
                return {
                    "success": False,
                    "error": response.text
                }

            try:
                data = response.json()
            except Exception:
                return {
                    "success": False,
                    "error": response.text
                }

            return data

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

            url = f"{API_URL}/knowledge-base"
            print("=" * 60)
            print("REQUEST URL:", url)
            print("=" * 60)

            response = requests.get(
                url,
                headers=headers,
                timeout=60
            )

            print("=" * 60)
            print("STATUS:", response.status_code)
            print("BODY:", response.text)
            print("=" * 60)

            if response.status_code != 200:
                return {
                    "success": False,
                    "answer": response.text,
                    "total_documents": 0,
                    "documents": []
                }

            try:
                data = response.json()
            except Exception:
                return {
                    "success": False,
                    "answer": response.text,
                    "total_documents": 0,
                    "documents": []
                }

            return data

        except Exception as e:

            return {
                "total_documents": 0,
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

            url = f"{API_URL}/search"
            payload = {"query": query}
            
            print("=" * 60)
            print("REQUEST URL:", url)
            print("REQUEST BODY:", payload)
            print("=" * 60)

            response = requests.post(
                url,
                json=payload,
                headers=headers,
                timeout=60
            )

            print("=" * 60)
            print("STATUS:", response.status_code)
            print("BODY:", response.text)
            print("=" * 60)

            if response.status_code != 200:
                return {
                    "success": False,
                    "results": [],
                    "error": response.text
                }

            try:
                data = response.json()
            except Exception:
                return {
                    "success": False,
                    "results": [],
                    "error": response.text
                }

            return data

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

            url = f"{API_URL}/rebuild"
            print("=" * 60)
            print("REQUEST URL:", url)
            print("=" * 60)

            response = requests.post(
                url,
                headers=headers,
                timeout=60
            )

            print("=" * 60)
            print("STATUS:", response.status_code)
            print("BODY:", response.text)
            print("=" * 60)

            if response.status_code != 200:
                return {
                    "success": False,
                    "error": response.text
                }

            try:
                data = response.json()
            except Exception:
                return {
                    "success": False,
                    "error": response.text
                }

            return data

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }