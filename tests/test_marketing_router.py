from app.services.llm_router import select_agent

questions = [
    "Create a LinkedIn post for our AI product",
    "Write an email campaign",
    "Generate a social media caption",
    "Marketing strategy for startups",
    "Create advertisement"
]

for q in questions:

    print("=" * 60)
    print("Question :", q)
    print("Agent    :", select_agent(q))