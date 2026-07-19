from sqlalchemy.orm import Session

from app.agents.base.base_agent import BaseAgent
from app.services.analytics_service import AnalyticsService


class AnalyticsAgent(BaseAgent):

    @property
    def name(self):
        return "Analytics"

    def execute(
        self,
        message: str,
        db: Session = None,
        agent_count: int = 0,
    ):
        summary = AnalyticsService.system_summary(db)

        summary["registered_agents"] = agent_count

        return {
            "agent": self.name,
            "success": True,
            "system": summary,
        }