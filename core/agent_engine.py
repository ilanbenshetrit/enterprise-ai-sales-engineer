"""
Enterprise AI Sales Platform
Core Agent Engine

Responsible for orchestrating the execution flow of every AI request.
"""

from typing import Optional


class AgentEngine:
    """
    Main orchestration engine.

    Coordinates all platform components:
    - Task Routing
    - Memory
    - Tools
    - Knowledge
    - Prompt Building
    - LLM
    """

    def __init__(
        self,
        router=None,
        tool_manager=None,
        knowledge_manager=None,
        prompt_builder=None,
        memory_manager=None,
        llm=None,
    ):

        self.router = router
        self.tool_manager = tool_manager
        self.knowledge_manager = knowledge_manager
        self.prompt_builder = prompt_builder
        self.memory_manager = memory_manager
        self.llm = llm

    def run(self, task: str) -> str:
        """
        Execute a complete AI workflow.
        """

        print("=" * 60)
        print("Enterprise AI Sales Platform")
        print("=" * 60)

        print(f"Task: {task}")

        route = self._route(task)

        print(f"Route: {route}")

        tool_result = self._run_tool(route, task)

        print(f"Tool Result: {tool_result}")

        knowledge = self._load_knowledge(task)

        prompt = self._build_prompt(
            task,
            tool_result,
            knowledge
        )

        response = self._ask_llm(prompt)

        return response

    def _route(self, task: str):

        if self.router:

            return self.router.decide(task)

        return None

    def _run_tool(
        self,
        route: Optional[str],
        task: str
    ):

        if self.tool_manager and route:

            return self.tool_manager.run(
                route,
                task
            )

        return None

    def _load_knowledge(
        self,
        task: str
    ):

        if self.knowledge_manager:

            return self.knowledge_manager.search(
                task
            )

        return None

    def _build_prompt(
        self,
        task,
        tool_result,
        knowledge
    ):

        if self.prompt_builder:

            return self.prompt_builder.build(
                task=task,
                tool_result=tool_result,
                knowledge=knowledge,
            )

        return task

    def _ask_llm(
        self,
        prompt
    ):

        if self.llm:

            return self.llm.ask(prompt)

        return "LLM Provider not configured."