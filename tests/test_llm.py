from app.services.llm_service import LLMService

llm = LLMService()

answer = llm.generate(
    "What is Artificial Intelligence?"
)

print("=" * 60)
print("LLM TEST")
print("=" * 60)

print(answer)