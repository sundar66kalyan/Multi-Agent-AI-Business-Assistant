from app.services.llm_router import select_agent

questions = [

    "Generate business report",

    "Monthly report",

    "Executive summary",

    "Show analytics dashboard",

    "System metrics"

]

print("=" * 60)
print("REPORT & ANALYTICS ROUTER TEST")
print("=" * 60)

for question in questions:

    print(f"\nQuestion : {question}")

    agent = select_agent(question)

    print(f"Agent    : {agent}")