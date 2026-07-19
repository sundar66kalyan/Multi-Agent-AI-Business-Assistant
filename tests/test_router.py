from app.services.llm_router import select_agent

questions = [
    "Show employee handbook",
    "Leave policy",
    "Summarize this PDF",
    "What is our profit?",
    "Show monthly sales"
]

for q in questions:
    print("=" * 60)
    print("Question :", q)
    print("Agent    :", select_agent(q))