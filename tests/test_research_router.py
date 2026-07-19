from app.services.llm_router import select_agent

questions = [
    "Latest AI trends",
    "Compare GPT vs Llama",
    "Research Tesla",
    "Technology trends",
    "Analyze competitors"
]

for q in questions:

    print("=" * 60)
    print("Question :", q)
    print("Agent    :", select_agent(q))