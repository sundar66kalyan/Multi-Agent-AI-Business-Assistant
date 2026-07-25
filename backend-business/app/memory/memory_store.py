class MemoryStore:

    def __init__(self):
        self.messages = []

    def add(self, role, content):
        self.messages.append(
            {
                "role": role,
                "content": content
            }
        )

    def clear(self):
        self.messages = []


memory = MemoryStore()