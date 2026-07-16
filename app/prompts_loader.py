from pathlib import Path


def load_sales_engineer_prompt():

    prompt_path = Path(
        "prompts/sales_engineer.txt"
    )

    return prompt_path.read_text()