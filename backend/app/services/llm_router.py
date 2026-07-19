# app/services/llm_router.py

from google import genai
from google.genai.errors import ClientError

from app.core.config import settings
from app.prompts.router_prompt import ROUTER_PROMPT

client = genai.Client(api_key=settings.GOOGLE_API_KEY)


class LLMRouter:
    """
    Router for selecting the appropriate agent based on user question.
    Uses keyword matching for fast, deterministic routing.
    """
    
    @staticmethod
    def select_agent(question: str) -> str:
        """
        Select the appropriate agent based on the user's question.
        Uses keyword matching for fast and reliable routing.
        
        Args:
            question (str): User's input question
            
        Returns:
            str: Name of the selected agent
        """
        q = question.lower()
        
        # HR Agent - Employee related queries
        if any(word in q for word in [
            "leave",
            "salary",
            "employee",
            "holiday",
            "hr",
            "attendance",
            "payroll",
            "recruitment",
            "promotion",
            "performance",
            "training",
            "benefits",
            "compensation",
            "onboarding"
        ]):
            return "HR"
        
        # Finance Agent - Financial queries
        elif any(word in q for word in [
            "finance",
            "revenue",
            "expense",
            "profit",
            "budget",
            "cost",
            "income",
            "financial",
            "accounting",
            "invoice",
            "payment",
            "tax",
            "audit",
            "cash flow"
        ]):
            return "Finance"
        
        # Analytics Agent - Data and analytics queries
        elif any(word in q for word in [
            "analytics",
            "analysis",
            "dashboard",
            "chart",
            "statistics",
            "metrics",
            "kpi",
            "data",
            "visualization",
            "trend",
            "performance metrics",
            "system status",
            "system health"
        ]):
            return "Analytics"
        
        # Research Agent - Research and market queries
        elif any(word in q for word in [
            "research",
            "market",
            "competitor",
            "study",
            "analysis",
            "trend",
            "latest",
            "technology",
            "paper",
            "industry",
            "compare",
            "benchmark"
        ]):
            return "Research"
        
        # Report Agent - Report generation queries
        elif any(word in q for word in [
            "report",
            "pdf",
            "excel",
            "docx",
            "summary",
            "generate",
            "export",
            "download",
            "monthly report",
            "weekly report",
            "annual report",
            "business report",
            "executive summary"
        ]):
            return "Report"
        
        # Sales Agent - Sales and customer queries
        elif any(word in q for word in [
            "sales",
            "customer",
            "lead",
            "deal",
            "quote",
            "purchase",
            "order",
            "client",
            "prospect",
            "conversion",
            "pipeline"
        ]):
            return "Sales"
        
        # Marketing Agent - Marketing queries
        elif any(word in q for word in [
            "marketing",
            "campaign",
            "social media",
            "advertisement",
            "advertising",
            "seo",
            "content",
            "brand",
            "engagement",
            "influencer",
            "email campaign",
            "promotion"
        ]):
            return "Marketing"
        
        # Document Agent - Document related queries
        elif any(word in q for word in [
            "document",
            "policy",
            "handbook",
            "manual",
            "guide",
            "pdf",
            "file",
            "upload",
            "download"
        ]):
            return "Document"
        
        # General Agent - Default fallback
        return "General"


def keyword_fallback(message: str):
    """
    Fallback routing using keyword matching when Gemini is unavailable.
    (Legacy function - kept for backward compatibility)
    
    Priority order (specific to broad):
    1. HR
    2. Marketing
    3. Research
    4. Analytics
    5. Report
    6. Finance
    7. Sales
    8. Document
    9. General (default)
    
    Args:
        message (str): User input message
        
    Returns:
        str: Agent name to route to
    """
    message = message.lower()

    # HR
    if any(word in message for word in [
        "leave",
        "attendance",
        "employee",
        "holiday",
        "payroll",
        "recruitment",
        "promotion",
        "performance",
        "salary"
    ]):
        return "HR"

    # Marketing
    if any(word in message for word in [
        "marketing",
        "campaign",
        "linkedin",
        "social media",
        "advertisement",
        "advertising",
        "promotion",
        "seo",
        "facebook",
        "instagram",
        "twitter",
        "blog",
        "caption",
        "content",
        "influencer",
        "engagement",
        "brand",
        "email campaign"
    ]):
        return "Marketing"

    # Research
    if any(word in message for word in [
        "research",
        "compare",
        "analysis",
        "trend",
        "latest",
        "technology",
        "paper",
        "study",
        "competitor",
        "competitors",
        "market analysis"
    ]):
        return "Research"

    # Analytics
    if any(word in message for word in [
        "analytics",
        "dashboard",
        "statistics",
        "metrics",
        "system status",
        "system health",
        "performance metrics"
    ]):
        return "Analytics"

    # Report
    if any(word in message for word in [
        "report",
        "summary",
        "business report",
        "monthly report",
        "weekly report",
        "annual report",
        "generate report",
        "executive summary"
    ]):
        return "Report"

    # Finance
    if any(word in message for word in [
        "profit",
        "revenue",
        "expense",
        "finance",
        "budget"
    ]):
        return "Finance"

    # Sales
    if any(word in message for word in [
        "sales",
        "customer",
        "invoice",
        "lead",
        "deal",
        "quote",
        "purchase",
        "order",
        "client"
    ]):
        return "Sales"

    # Documents
    if any(word in message for word in [
        "document",
        "pdf",
        "policy",
        "handbook",
        "manual",
        "guide"
    ]):
        return "Document"

    # Default fallback
    return "General"


def select_agent(message: str) -> str:
    """
    Select the appropriate agent for the given message.
    Uses Gemini LLM for intelligent routing, with keyword fallback.
    (Legacy function - kept for backward compatibility)
    
    Args:
        message (str): User input message
        
    Returns:
        str: Name of the selected agent
    """
    prompt = f"""
{ROUTER_PROMPT}

Question:
{message}

Answer:
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        
        agent_name = response.text.strip()
        print("=" * 60)
        print("🤖 GEMINI ROUTER")
        print(f"Selected Agent : {agent_name}")
        print("=" * 60)
        return agent_name

    except ClientError as e:
        print("=" * 60)
        print("⚠️ Gemini unavailable")
        print(f"Error: {e}")
        print("🔧 Using keyword fallback...")
        print("=" * 60)
        
        fallback_agent = keyword_fallback(message)
        print(f"📌 Fallback routing to: {fallback_agent}")
        return fallback_agent

    except Exception as e:
        print("=" * 60)
        print("❌ Unexpected error in router")
        print(f"Error: {e}")
        print("🔧 Using keyword fallback...")
        print("=" * 60)
        return keyword_fallback(message)