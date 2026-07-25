import requests


class AIService:

    BASE_URL = "http://127.0.0.1:8000"

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