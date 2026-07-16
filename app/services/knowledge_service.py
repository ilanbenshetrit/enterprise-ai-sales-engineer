from core.knowledge_manager import KnowledgeManager


class KnowledgeService:


    def __init__(self):

        self.manager = KnowledgeManager()



    def search(self, query):

        return self.manager.search(
            query
        )