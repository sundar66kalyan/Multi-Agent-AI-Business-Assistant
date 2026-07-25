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
        pass

    def get(self, name):

        if name == "Sales":
            return SalesAgent()

        elif name == "Finance":
            return FinanceAgent()

        elif name == "Document":
            return DocumentAgent()

        elif name == "HR":
            return HRAgent()

        elif name == "Marketing":
            return MarketingAgent()

        elif name == "Research":
            return ResearchAgent()

        elif name == "Analytics":
            return AnalyticsAgent()

        elif name == "Report":
            return ReportAgent()

        return GeneralAgent()

    def list_agents(self):
        return [
            "Sales",
            "Finance",
            "Document",
            "HR",
            "Marketing",
            "Research",
            "Analytics",
            "Report",
            "General",
        ]


# ============================================================
# ORCHESTRATOR
# ============================================================

from app.services.llm_router import LLMRouter  # ← UPDATED IMPORT


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
        selected = LLMRouter.select_agent(message)  # ← UPDATED CALL

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


        MAX_WORKERS = 1

        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:

            futures = [
                executor.submit(run_agent, name)
                for name in plan.get_agents()
            ]

            for future in futures:
                try:
                    name, output = future.result()
                    results[name] = output

                    print("=" * 60)
                    print("Agent:", name)
                    print(output)
                    print("=" * 60)

                except Exception as e:
                    import traceback

                    print("=" * 80)
                    print("THREAD ERROR")
                    traceback.print_exc()
                    print("=" * 80)

                    raise

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