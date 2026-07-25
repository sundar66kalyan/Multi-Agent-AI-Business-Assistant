# app/agents/base/agent_manager.py

from app.agents.sales.sales_agent import SalesAgent
from app.agents.finance.finance_agent import FinanceAgent
from app.agents.base.general_agent import GeneralAgent
from app.agents.document.document_agent import DocumentAgent  # ← NEW IMPORT


class AgentManager:

    def __init__(self):
        pass

    def get(self, name):

        if name == "Sales":
            return SalesAgent()

        elif name == "Finance":
            return FinanceAgent()

        elif name == "Document":
            return DocumentAgent()

        return GeneralAgent()

    def list_agents(self):
        return [
            "Sales",
            "Finance",
            "Document",
            "General"
        ]