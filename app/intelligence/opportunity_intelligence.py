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



    def build_context(
        self,
        opportunity
    ):

        customer_context = {}


        if opportunity.customer:

            customer_context = {

                "name": opportunity.customer.name,

                "industry": opportunity.customer.industry,

                "size": opportunity.customer.size,

                "environment": opportunity.customer.environment,

                "compliance": opportunity.customer.compliance,

                "challenges": opportunity.customer.challenges,

                "business_goals": opportunity.customer.business_goals

            }



        return {

            "task": "solution_design",

            "knowledge": opportunity.requirements,

            "customer_context": customer_context

        }



    def analyze(
        self,
        opportunity
    ):

        context = self.build_context(
            opportunity
        )


        analysis = self.reasoning_engine.analyze(
            context
        )


        opportunity.set_analysis(
            analysis
        )


        return opportunity