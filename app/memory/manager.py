import json

from pathlib import Path

from datetime import datetime



class MemoryManager:


    def __init__(self):

        self.memory_file = Path(
            "memory/memory.json"
        )


        if not self.memory_file.exists():

            self.initialize_memory()



    def initialize_memory(self):

        memory = {

            "metadata": {
                "version": "2.0",
                "created": datetime.now().isoformat()
            },

            "last_task": None,

            "tasks": [],

            "conversations": [],

            "customers": [],

            "rfp_history": []

        }


        self.memory_file.write_text(

            json.dumps(
                memory,
                indent=4,
                ensure_ascii=False
            )

        )



    def save(self, key, value):

        memory = self.load()


        memory[key] = value



        if key == "last_task":


            memory["tasks"].append(

                {
                    "content": value,
                    "timestamp": datetime.now().isoformat()
                }

            )


        self.memory_file.write_text(

            json.dumps(
                memory,
                indent=4,
                ensure_ascii=False
            )

        )



    def load(self):

        memory = json.loads(

            self.memory_file.read_text()

        )


        if "tasks" not in memory:


            old_task = memory.get(
                "last_task"
            )


            memory = {

                "metadata": {
                    "version": "2.0",
                    "migrated": True
                },

                "last_task": old_task,

                "tasks": [],

                "conversations": [],

                "customers": [],

                "rfp_history": []

            }


            if old_task:


                memory["tasks"].append(

                    {
                        "content": old_task,
                        "timestamp": datetime.now().isoformat()
                    }

                )


        return memory
