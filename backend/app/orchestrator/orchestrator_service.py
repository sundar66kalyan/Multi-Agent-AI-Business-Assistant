# app/agents/base/agent_manager.py
from concurrent.futures import ThreadPoolExecutor
from app.orchestrator.execution_plan import ExecutionPlan
from app.agents.sales.sales_agent import SalesAgent
from app.agents.finance.finance_agent import FinanceAgent
from app.agents.document.document_agent import DocumentAgent
from app.agents.hr.hr_agent import HRAgent
from app.agents.marketing.marketing_agent import MarketingAgent
from app.agents.research.research_agent import ResearchAgent
from app.agents.analytics.analytics_agent import AnalyticsAgent
from app.agents.report.report_agent import ReportAgent
from app.agents.base.general_agent import GeneralAgent


class AgentManager:

    def __init__(self):
        self.agents = {}

        # Register all agents
        self.register(SalesAgent())
        self.register(FinanceAgent())
        self.register(DocumentAgent())
        self.register(HRAgent())
        self.register(MarketingAgent())
        self.register(ResearchAgent())
        self.register(AnalyticsAgent())
        self.register(ReportAgent())
        self.register(GeneralAgent())

    def register(self, agent):
        self.agents[agent.name] = agent

    def get(self, name):
        return self.agents.get(
            name,
            self.agents["General"]
        )

    def list_agents(self):
        return list(self.agents.keys())


# ============================================================
# ORCHESTRATOR
# ============================================================

from app.services.llm_router import select_agent  # ← IMPORT FOR ORCHESTRATOR


class Orchestrator:

    def __init__(self):
        self.manager = AgentManager()

    def process(self, message: str, db=None):
        """
        Process user message through the appropriate agent.
        
        Args:
            message (str): User input message
            db: Database session (optional)
            
        Returns:
            dict: Response from the selected agent
        """
        # Route the message to the appropriate agent
        selected = select_agent(message)

        print("=" * 60)
        print("Selected Agent:", selected)
        print("=" * 60)

        plan = ExecutionPlan()

        message_lower = message.lower()

        if selected == "Report":
            plan.add("Finance")
            plan.add("Analytics")
            plan.add("Document")

        elif (
            "business" in message_lower
            or "performance" in message_lower
            or "analysis" in message_lower
            or "report" in message_lower
        ):
            plan.add("Finance")
            plan.add("Analytics")
            plan.add("Document")

        else:
            plan.add(selected)

        print("=" * 60)
        print("🤖 AGENT ROUTER")
        print(f"Selected Agent : {selected}")
        print("=" * 60)

        # Get the agent instance from AgentManager
        results = {}

        def run_agent(agent_name):
            agent = self.manager.get(agent_name)

            if agent_name == "Analytics":
                return (
                    agent_name,
                    agent.execute(
                        message=message,
                        db=db,
                        agent_count=len(self.manager.list_agents())
                    )
                )

            # Special handling for Report Agent
            if agent_name == "Report":
                return (
                    agent_name,
                    agent.execute()
                )

            return (
                agent_name,
                agent.execute(
                    message=message,
                    db=db
                )
            )


        with ThreadPoolExecutor(max_workers=5) as executor:

            futures = [
                executor.submit(run_agent, name)
                for name in plan.get_agents()
            ]

            for future in futures:
                name, output = future.result()
                results[name] = output
                print("=" * 60)
                print(f"Agent: {name}")
                print(output)
                print("=" * 60)

        # If only one agent was executed, return it in a consistent format
        if len(results) == 1:

            agent_name = list(results.keys())[0]
            result = results[agent_name]

            # If the agent already returned a dictionary,
            # return it directly with consistent fields.
            if isinstance(result, dict):
                result.setdefault("success", True)
                result.setdefault("agent", agent_name)
                return result

            # Otherwise wrap plain text into the expected format.
            return {
                "success": True,
                "agent": agent_name,
                "answer": str(result)
            }

        # Generate Executive Report for multi-agent execution
        report_agent = ReportAgent()

        report = report_agent.execute(
            finance=results.get("Finance"),
            analytics=results.get("Analytics")
        )

        return {
            "success": True,
            "executed_agents": plan.get_agents(),
            "report": report,
            "raw_results": results
        }