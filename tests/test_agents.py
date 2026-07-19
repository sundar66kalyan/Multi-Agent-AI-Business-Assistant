from app.orchestrator.orchestrator_service import AgentManager

manager = AgentManager()

print("=" * 60)
print("REGISTERED AGENTS")
print("=" * 60)

for agent in manager.list_agents():
    print("-", agent)