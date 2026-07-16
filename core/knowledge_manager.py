"""
Enterprise AI Sales Platform
Knowledge Manager
"""

from pathlib import Path


class KnowledgeManager:
    """
    Responsible for loading and searching
    the platform knowledge base.
    """

    def __init__(self):

        self.knowledge_path = Path("knowledge")

    def search(self, query: str):

        if not self.knowledge_path.exists():
            return []

        results = []

        for file in self.knowledge_path.glob("*.md"):

            try:

                content = file.read_text(encoding="utf-8")

                if query.lower() in content.lower():

                    results.append(
                        {
                            "file": file.name,
                            "content": content
                        }
                    )

            except Exception:

                continue

        return results