# app/services/analytics_service.py

import json
import logging
import requests
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Any, Optional

from app.repositories.analytics_repository import AnalyticsRepository

# Configure logging
logger = logging.getLogger(__name__)


class AnalyticsService:

    @staticmethod
    def system_summary(db) -> Dict[str, Any]:
        """
        Generate a system summary including document and finance statistics.
        
        Args:
            db: Database session
            
        Returns:
            dict: System summary statistics
        """
        try:
            # Get document metadata
            metadata_file = Path("data/metadata/documents.json")
            documents = 0
            chunks = 0

            if metadata_file.exists():
                try:
                    data = json.loads(metadata_file.read_text(encoding="utf-8"))
                    documents = len(data)
                    chunks = sum(item.get("chunks", 0) for item in data)
                except json.JSONDecodeError as e:
                    logger.error(f"Error parsing documents.json: {e}")
                except Exception as e:
                    logger.error(f"Error reading metadata file: {e}")

            # Get finance records count
            try:
                finance_records = AnalyticsRepository.total_finance_records(db)
            except Exception as e:
                logger.error(f"Error fetching finance records: {e}")
                finance_records = 0

            # Make request to AI service status
            try:
                response = requests.get(
                    "http://127.0.0.1:8000/stats/",
                    timeout=5
                )
                
                # Parse AI service response if available
                ai_status = response.json() if response.status_code == 200 else None
                
                if ai_status:
                    chunks = ai_status.get("indexed_chunks", 0)
                    # Temporary until we expose actual document count
                    documents = 1 if chunks > 0 else 0
                    
            except requests.RequestException as e:
                logger.error(f"AI Service Error: {e}")
                ai_status = None

            # Return system summary
            return {
                "documents": documents,
                "chunks": chunks,
                "finance_records": finance_records,
                "ai_service": ai_status,
                "timestamp": datetime.now().isoformat()
            }

        except Exception as e:
            import traceback
            traceback.print_exc()
            return {
                "documents": 0,
                "chunks": 0,
                "finance_records": 0,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }

    @staticmethod
    def ai_usage(db: Optional[Any] = None) -> Dict[str, Any]:
        """
        AI Usage Analytics with realistic metrics.
        
        Args:
            db: Optional database session for real data fetching
            
        Returns:
            dict: AI usage statistics
        """
        try:
            # In a real implementation, these would come from the database
            # Here we return realistic mock data with timestamps
            
            current_time = datetime.now()
            today_start = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
            
            # Mock data - in production, these would be calculated from actual usage logs
            return {
                "questions_today": 156,
                "active_users": 12,
                "avg_response_time": 0.82,
                "most_used_agent": "HR",
                "knowledge_searches": 348,
                "agent_usage": {
                    "HR": 45,
                    "Finance": 30,
                    "Research": 20,
                    "Sales": 15,
                    "Marketing": 10
                },
                "period": {
                    "start": today_start.isoformat(),
                    "end": current_time.isoformat()
                },
                "last_updated": current_time.isoformat()
            }
            
        except Exception as e:
            import traceback
            traceback.print_exc()
            return {
                "error": str(e),
                "last_updated": datetime.now().isoformat()
            }

    @staticmethod
    def get_document_stats(db) -> Dict[str, Any]:
        """
        Get detailed document statistics.
        
        Args:
            db: Database session
            
        Returns:
            dict: Document statistics
        """
        try:
            metadata_file = Path("data/metadata/documents.json")
            
            if not metadata_file.exists():
                return {"total_documents": 0, "total_chunks": 0, "documents": []}
            
            data = json.loads(metadata_file.read_text(encoding="utf-8"))
            
            # Calculate per-document stats
            doc_stats = []
            total_chunks = 0
            
            for doc in data:
                chunks_count = doc.get("chunks", 0)
                total_chunks += chunks_count
                doc_stats.append({
                    "id": doc.get("id"),
                    "filename": doc.get("filename"),
                    "chunks": chunks_count,
                    "created_at": doc.get("created_at")
                })
            
            return {
                "total_documents": len(data),
                "total_chunks": total_chunks,
                "documents": doc_stats,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            import traceback
            traceback.print_exc()
            return {
                "total_documents": 0,
                "total_chunks": 0,
                "documents": [],
                "error": str(e)
            }

    @staticmethod
    def get_finance_summary(db) -> Dict[str, Any]:
        """
        Get finance records summary.
        
        Args:
            db: Database session
            
        Returns:
            dict: Finance summary statistics
        """
        try:
            total_records = AnalyticsRepository.total_finance_records(db)
            
            # Additional finance stats could be added here
            return {
                "total_records": total_records,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            import traceback
            traceback.print_exc()
            return {
                "total_records": 0,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }