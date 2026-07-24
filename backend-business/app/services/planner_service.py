import json

from google import genai

from app.core.config import settings

class PlannerService:
    """
    Creates an execution plan for the orchestrator.
    """

    def create_plan(self, selected_agent: str, message: str):

        client = genai.Client(api_key=settings.GOOGLE_API_KEY)

        prompt = f"""
You are an AI planner for a Multi-Agent Business Assistant.

Available Agents:

- Finance
- Analytics
- Document
- Report
- HR
- Sales
- Marketing
- Research
- General

Based on the user's request, return ONLY a JSON array.

Example:

["Finance","Analytics"]

User Request:
{message}
"""

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            text = response.text.strip()

            plan = json.loads(text)

            if isinstance(plan, list) and len(plan) > 0:
                return plan

        except Exception:
            pass

        # ---------- FALLBACK ----------
        message = message.lower()

        if (
            "business" in message
            or "performance" in message
            or "analysis" in message
        ):
            return [
                "Finance",
                "Analytics",
                "Document"
            ]

        return [selected_agent]