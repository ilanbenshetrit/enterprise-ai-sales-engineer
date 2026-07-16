from app.llm.claude_client import ClaudeClient
from app.prompts_loader import load_sales_engineer_prompt
from app.memory_manager import MemoryManager
from tools.tool_registry import ToolRegistry
from app.task_router import TaskRouter

from core.knowledge_manager import KnowledgeManager
from core.prompt_builder import PromptBuilder


class EnterpriseAgent:

    def __init__(self, name):

        self.name = name

        self.llm = ClaudeClient()

        self.system_prompt = load_sales_engineer_prompt()

        self.memory = MemoryManager()

        self.tools = ToolRegistry()

        self.router = TaskRouter()

        self.knowledge = KnowledgeManager()

        self.prompt_builder = PromptBuilder()



    def execute(self, task):

        print(f"Agent: {self.name}")


        # Save task to memory
        self.memory.save(
            "last_task",
            task
        )


        # Retrieve relevant knowledge
        knowledge_result = self.knowledge.search(
            task
        )


        print("\nKnowledge Result:")
        print(knowledge_result)



        # Decide if a tool is required
        tool_result = None

        tool_name = self.router.decide(
            task
        )


        if tool_name:

            tool_result = self.use_tool(
                tool_name,
                task
            )

            print("\nTool Result:")
            print(tool_result)



        # Build prompt
        full_prompt = self.prompt_builder.build(
            system_prompt=self.system_prompt,
            task=task,
            knowledge=knowledge_result,
            tools=tool_result
        )


        response = self.llm.ask(
            full_prompt
        )


        return response



    def use_tool(
        self,
        tool_name,
        data
    ):

        tool = self.tools.get_tool(
            tool_name
        )


        if tool:

            return tool.run(
                data
            )


        return None



if __name__ == "__main__":


    agent = EnterpriseAgent(
        "Enterprise Sales Engineer Agent"
    )


    result = agent.execute(
        """
Analyze this RFP document:

Customer requirements:

- Enterprise backup solution
- Ransomware recovery
- Immutable backup storage
- Hybrid cloud integration
- Security and compliance support

Find:
1. Requirements
2. Technical questions
3. Risks
4. Recommended solution direction
"""
    )


    print("\nAI Response:")
    print(result)