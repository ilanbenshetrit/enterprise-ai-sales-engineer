class AgentContextBuilder:


    def build(
        self,
        query,
        knowledge_results,
        customer_context=None
    ):


        if customer_context is None:

            customer_context = {}



        context = {

            "query": query,


            "knowledge": [

                result["chunk"]

                for result in knowledge_results

            ],


            "customer_context": customer_context,


            "task": self.detect_task(query)

        }


        return context



    def detect_task(
        self,
        query
    ):


        query = query.lower()


        if "rfp" in query:

            return "rfp_analysis"


        if "design" in query or "architecture" in query:

            return "solution_design"


        if "discover" in query or "customer" in query:

            return "discovery"



        return "general_sales_support"