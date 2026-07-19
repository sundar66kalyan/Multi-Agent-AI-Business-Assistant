from app.tools.sql.sql_tool import SQLTool


class ToolManager:

    def __init__(self):

        self.tools = {}

        self.register(
            "SQL",
            SQLTool()
        )

    def register(self, name, tool):

        self.tools[name] = tool

    def get(self, name):

        return self.tools.get(name)

    def list_tools(self):

        return list(self.tools.keys())