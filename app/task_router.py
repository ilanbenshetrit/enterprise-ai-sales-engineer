class TaskRouter:


    def decide(self, task):

        task_lower = task.lower()


        discovery_keywords = [
            "discovery",
            "customer questions",
            "customer needs",
            "requirements gathering"
        ]


        rfp_keywords = [
            "rfp",
            "proposal",
            "requirements",
            "technical document",
            "gap analysis",
            "gaps"
        ]


        for keyword in discovery_keywords:

            if keyword in task_lower:
                return "discovery"


        for keyword in rfp_keywords:

            if keyword in task_lower:
                return "rfp"


        return None