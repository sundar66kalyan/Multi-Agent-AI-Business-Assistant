import os
import requests


class AIService:

    BASE_URL = os.getenv(
        "AI_SERVICE_URL",
        "https://multi-agent-ai-business-assistant-1.onrender.com"
    )

    @staticmethod
    def ask(question: str):

        response = requests.post(
            f"{AIService.BASE_URL}/chat/",
            json={
                "question": question
            },
            timeout=60
        )

        response.raise_for_status()

        return response.json()