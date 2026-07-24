import json

from app.services.llm_service import LLMService


class PlannerService:
    """
    Creates an execution plan for the orchestrator.
    """

    def create_plan(self, selected_agent: str, message: str):

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

        llm = LLMService()

        try:

            text = llm.generate(prompt).strip()

            # Remove markdown code fences if present
            text = text.replace("```json", "").replace("```", "").strip()

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