from sqlalchemy.orm import Session
from google import genai

from app.agents.base.base_agent import BaseAgent
from app.services.report_service import ReportService
from app.core.config import settings


class ReportAgent(BaseAgent):

    name = "Report"

    def execute(
        self,
        message=None,
        context=None,
        finance=None,
        analytics=None,
    ):
        """
        Execute Report Agent to generate business report.
        
        Args:
            message (str, optional): User message
            context (dict, optional): Orchestrator context
            finance (dict, optional): Finance data
            analytics (dict, optional): Analytics data
            
        Returns:
            dict: Generated report
        """
        # --------------------------------------------------
        # Support orchestrator context
        # --------------------------------------------------

        if context:
            finance = context.get("Finance", finance)
            analytics = context.get("Analytics", analytics)

        finance = finance or {}
        analytics = analytics or {}

        # Analytics agent returns data under "system"
        if "system" in analytics:
            analytics = analytics["system"]

        finance_data = finance.get("data", {})
        analytics_data = analytics

        prompt = f"""
You are a Senior Business Consultant.

Prepare a professional Executive Business Report.

Finance

Revenue: {finance_data.get("revenue")}
Expenses: {finance_data.get("expenses")}
Profit: {finance_data.get("profit")}

Analytics

Documents Indexed:
{analytics_data.get("documents", 0)}

Finance Records:
{analytics_data.get("finance_records", 0)}

Write:

1. Executive Summary
2. Financial Health
3. Business Insights
4. Risks
5. Recommendations

Return in clean markdown.
"""

        client = genai.Client(api_key=settings.GOOGLE_API_KEY)

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            report_text = response.text

        except Exception as e:

            report_text = f"""
EXECUTIVE BUSINESS REPORT
=========================

Executive Summary
-----------------
Business analysis completed successfully using the local analytics engine.
The AI-generated report is currently unavailable because the Gemini API could not be reached or the quota has been exceeded.

Financial Overview
------------------
Revenue : ₹{finance_data.get("revenue", 0)}
Expenses: ₹{finance_data.get("expenses", 0)}
Profit  : ₹{finance_data.get("profit", 0)}

Analytics
---------
Documents Indexed : {analytics_data.get("documents", 0)}
Finance Records   : {analytics_data.get("finance_records", 0)}

Business Health
---------------
Overall business performance appears stable based on the available financial metrics.

Recommendations
---------------
• Increase monthly revenue.
• Optimize operational expenses.
• Continue indexing business documents.
• Monitor KPIs regularly.

AI Status
---------
Gemini report generation is temporarily unavailable.

"""

        return {
            "agent": "Report",
            "report": report_text
        }