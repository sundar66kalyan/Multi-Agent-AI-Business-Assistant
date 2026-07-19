from app.tools.tool_manager import ToolManager

manager = ToolManager()

print("\nRegistered Tools:")

for tool in manager.list_tools():
    print(" -", tool)