"""
Enterprise AI Sales Platform
Prompt Builder

Responsible for creating LLM prompts.
"""


class PromptBuilder:
    """
    Builds structured prompts
    from system instructions,
    user tasks and knowledge context.
    """


    def build(
        self,
        system_prompt: str,
        task: str,
        knowledge=None,
        tools=None
    ):

        return f"""
{system_prompt}

User Task:
{task}


Knowledge Context:
{knowledge}


Tool Information:
{tools}


Instructions:
- Analyze the customer requirement.
- Identify technical needs.
- Recommend solution direction.
- Explain business value.
- Highlight risks and next steps.
"""
