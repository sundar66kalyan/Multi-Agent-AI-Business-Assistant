class AgentRegistry:

    def __init__(self):

        self.agents = []

    def register(self, agent):

        self.agents.append(agent)

    def get_agents(self):

        return self.agents