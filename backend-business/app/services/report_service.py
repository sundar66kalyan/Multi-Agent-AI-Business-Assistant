# app/services/report_service.py

from app.services.finance_service import FinanceService
from app.services.analytics_service import AnalyticsService


class ReportService:

    @staticmethod
    def generate(db):

        finance = FinanceService.answer_question(
            db,
            "summary"
        )

        analytics = AnalyticsService.system_summary(db)

        report = f"""
===============================
BUSINESS REPORT
===============================

FINANCE

Revenue  : {finance.get("revenue", 0)}

Expenses : {finance.get("expenses", 0)}

Profit   : {finance.get("profit", 0)}

Month    : {finance.get("month", "")}


-------------------------------

SYSTEM ANALYTICS

Indexed Documents : {analytics.get("documents", 0)}

Chunks            : {analytics.get("chunks", 0)}

Finance Records   : {analytics.get("finance_records", 0)}

===============================
"""

        return {
            "report": report,
            "finance": finance,
            "analytics": analytics,
        }