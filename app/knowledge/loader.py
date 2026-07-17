from pathlib import Path
import uuid



class KnowledgeLoader:


    def __init__(
        self,
        knowledge_path="knowledge"
    ):

        self.knowledge_path = Path(
            knowledge_path
        )



    def load_documents(self):

        documents = []


        if not self.knowledge_path.exists():

            return documents



        for file in self.knowledge_path.glob("*.md"):


            content = file.read_text(
                encoding="utf-8"
            )


            documents.append(

                {
                    "document_id": str(uuid.uuid4()),

                    "metadata": {

                        "source": file.name,

                        "filename": file.stem,

                        "extension": file.suffix,

                        "type": "markdown",

                    },

                    "content": content

                }

            )


        return documents