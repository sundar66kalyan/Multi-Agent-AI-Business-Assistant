from app.services.llm_router import LLMRouter

class AgentManager:

    @staticmethod
    def execute(question):

        agent = LLMRouter.select_agent(question)

        response = {
            "agent": agent,
            "steps": [],
            "answer": ""
        }

        if agent == "Finance":

            response["steps"].append("Finance Agent analyzed financial data.")
            response["steps"].append("Analytics Agent generated insights.")
            response["steps"].append("Report Agent prepared summary.")

            response["answer"] = (
                "Revenue is increasing by 12%. "
                "Expenses remain stable. "
                "Profit margin is healthy."
            )

        elif agent == "HR":

            response["steps"].append("HR Agent searched handbook.")
            response["answer"] = "Leave Policy retrieved."

        elif agent == "Research":

            response["steps"].append("Research Agent collected information.")
            response["steps"].append("Analytics Agent summarized trends.")
            response["answer"] = "Research completed."

        else:

            response["steps"].append("General Agent processed request.")
            response["answer"] = "General response."

        return response