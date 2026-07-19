# app/agents/base/agent_manager.py

from app.agents.sales.sales_agent import SalesAgent
from app.agents.finance.finance_agent import FinanceAgent
from app.agents.base.general_agent import GeneralAgent
from app.agents.document.document_agent import DocumentAgent  # ← NEW IMPORT


class AgentManager:

    def __init__(self):
        """
        Initialize AgentManager and register all available agents.
        """
        self.agents = {}

        # Register all agents
        self.register(SalesAgent())
        self.register(FinanceAgent())
        self.register(DocumentAgent())  # ← NEW: Register DocumentAgent
        self.register(GeneralAgent())

    def register(self, agent):
        """
        Register an agent with the manager.
        
        Args:
            agent: Agent instance with a 'name' attribute
        """
        self.agents[agent.name] = agent

    def get(self, name):
        """
        Get an agent by name, with fallback to General agent.
        
        Args:
            name (str): Name of the agent to retrieve
            
        Returns:
            Agent: The requested agent instance, or General agent if not found
        """
        return self.agents.get(
            name,
            self.agents["General"]  # Fallback to General agent
        )

    def list_agents(self):
        """
        List all registered agent names.
        
        Returns:
            list: List of agent names
        """
        return list(self.agents.keys())