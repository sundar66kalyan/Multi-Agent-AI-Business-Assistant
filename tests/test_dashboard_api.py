from frontend.dashboard.api import DashboardAPI

print("=" * 60)
print("DASHBOARD API TEST")
print("=" * 60)

print("\nMetrics")
print(DashboardAPI.get_metrics())

print("\nAgents")
print(DashboardAPI.get_agents())

print("\nHealth")
print(DashboardAPI.get_health())

print("\nChart")
print(DashboardAPI.get_finance_chart())