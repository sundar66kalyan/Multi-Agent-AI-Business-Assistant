# app/services/analytics_service.py

import json
from pathlib import Path

from app.repositories.analytics_repository import AnalyticsRepository


class AnalyticsService:

    @staticmethod
    def system_summary(db):
        """
        Generate a system summary including document and finance statistics.
        
        Args:
            db: Database session
            
        Returns:
            dict: System summary statistics
        """
        # Get document metadata
        metadata_file = Path(
            "data/metadata/documents.json"
        )

        documents = 0
        chunks = 0

        if metadata_file.exists():
            data = json.loads(
                metadata_file.read_text(
                    encoding="utf-8"
                )
            )

            documents = len(data)
            chunks = sum(
                item.get("chunks", 0)
                for item in data
            )

        # Get finance records count
        finance_records = (
            AnalyticsRepository.total_finance_records(db)
        )

        # Return system summary
        return {
            "documents": documents,
            "chunks": chunks,
            "finance_records": finance_records
        }

    @staticmethod
    def ai_usage(db=None):
        """
        AI Usage Analytics
        """

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
            }
        }