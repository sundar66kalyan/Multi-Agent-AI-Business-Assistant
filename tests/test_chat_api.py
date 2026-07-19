from frontend.dashboard.api import DashboardAPI

print("=" * 60)
print("CHAT API TEST")
print("=" * 60)

response = DashboardAPI.chat(
    "What is the leave policy?"
)

print(response)