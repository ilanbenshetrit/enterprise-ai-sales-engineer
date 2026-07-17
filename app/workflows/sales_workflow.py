from app.agents.context_builder import AgentContextBuilder
from app.agents.reasoning_engine import SalesReasoningEngine



class SalesWorkflow:


    def __init__(self):

        self.context_builder = AgentContextBuilder()

        self.reasoning_engine = SalesReasoningEngine()



    def run(
        self,
        query,
        knowledge_results,
        customer_context=None
    ):


        context = self.context_builder.build(

            query,

            knowledge_results,

            customer_context

        )


        analysis = self.reasoning_engine.analyze(

            context

        )


        return {

            "context": context,

            "analysis": analysis

        }