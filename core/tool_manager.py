"""
Enterprise AI Sales Platform
Tool Manager
"""

from tools.tool_registry import ToolRegistry


class ToolManager:
    """
    Responsible for executing platform tools.
    """

    def __init__(self):
        self.registry = ToolRegistry()

    def run(self, tool_name: str, data):

        tool = self.registry.get_tool(tool_name)

        if tool is None:
            print(f"[ToolManager] Tool '{tool_name}' not found.")
            return None

        print(f"[ToolManager] Running '{tool_name}'...")

        return tool.run(data)

    def available_tools(self):

        return list(self.registry.tools.keys())