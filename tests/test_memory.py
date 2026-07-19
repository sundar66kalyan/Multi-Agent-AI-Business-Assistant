from app.memory.memory_manager import MemoryManager

memory = MemoryManager()

memory.add_message(
    "session1",
    "user",
    "Show revenue"
)

memory.add_message(
    "session1",
    "assistant",
    "Revenue is 250000"
)

memory.add_message(
    "session1",
    "user",
    "What about profit?"
)

print(memory.get_history("session1"))