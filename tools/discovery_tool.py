class DiscoveryTool:

    def run(self, customer_type):

        return {
            "customer": customer_type,
            "questions": [
                "What are your main business challenges?",
                "What security risks are you trying to reduce?",
                "How do you currently handle backup and recovery?",
                "What compliance requirements do you have?"
            ]
        }