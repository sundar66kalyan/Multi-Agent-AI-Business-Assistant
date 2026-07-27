import os
import requests
from dotenv import load_dotenv

load_dotenv()

class AIService:
    BASE_URL = os.getenv("AI_SERVICE_URL")
    
    if not BASE_URL:
        raise ValueError("AI_SERVICE_URL environment variable is not set")

    @staticmethod
    def ask(question: str):
        try:
            print("=" * 60)
            print("CALLING AI SERVICE")
            print("URL:", f"{AIService.BASE_URL}/chat")
            print("MESSAGE:", question)
            print("=" * 60)

            response = requests.post(
                f"{AIService.BASE_URL}/chat",
                json={"message": question},
                timeout=60,
            )

            print("STATUS:", response.status_code)
            print("BODY:", response.text)

            response.raise_for_status()
            return response.json()

        except Exception as e:
            print("=" * 60)
            print("AI SERVICE ERROR")
            print(type(e).__name__)
            print(str(e))
            print("=" * 60)
            raise