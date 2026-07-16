import json
from pathlib import Path


class MemoryManager:

    def __init__(self):
        self.memory_file = Path(
            "memory/memory.json"
        )

        if not self.memory_file.exists():
            self.memory_file.write_text("{}")


    def save(self, key, value):

        memory = self.load()

        memory[key] = value

        self.memory_file.write_text(
            json.dumps(
                memory,
                indent=4,
                ensure_ascii=False
            )
        )


    def load(self):

        return json.loads(
            self.memory_file.read_text()
        )