from app.agents.reasoning_engine import SalesReasoningEngine



class OpportunityIntelligence:


    def __init__(
        self,
        reasoning_engine=None
    ):

        self.reasoning_engine = (
            reasoning_engine
            if reasoning_engine
            else SalesReasoningEngine()
        )



    def analyze(
        self,
        opportunity
    ):

        context = {

            "task": "solution_design",

            "knowledge": opportunity.requirements

        }


        analysis = self.reasoning_engine.analyze(
            context
        )


        opportunity.set_analysis(
            analysis
        )


        return opportunity