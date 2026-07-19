class ExecutionPlan:
    """
    Stores the list of agents that should execute
    for the current user request.
    """

    def __init__(self):
        self.agents = []

    def add(self, agent_name: str):
        """Add an agent if it is not already included."""
        if agent_name not in self.agents:
            self.agents.append(agent_name)

    def get_agents(self):
        """Return the execution list."""
        return self.agents