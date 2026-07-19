from app.services.llm_router import select_agent

questions = [
    "Employee leave policy",
    "Attendance rules",
    "Holiday list",
    "Payroll process",
    "Performance review"
]

for q in questions:
    print("=" * 60)
    print("Question :", q)
    print("Agent    :", select_agent(q))