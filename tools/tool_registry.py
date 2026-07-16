from tools.discovery_tool import DiscoveryTool
from tools.rfp_tool import RFPAnalyzerTool


class ToolRegistry:

    def __init__(self):

        self.tools = {
            "discovery": DiscoveryTool(),
            "rfp": RFPAnalyzerTool()
        }


    def get_tool(self, name):

        return self.tools.get(name)


    def list_tools(self):

        return list(self.tools.keys())