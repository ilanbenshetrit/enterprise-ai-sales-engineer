from app.agents.reasoning_engine import SalesReasoningEngine
from app.architecture.recommendation_engine import ArchitectureRecommendationEngine



class OpportunityIntelligence:


    def __init__(
        self,
        reasoning_engine=None,
        architecture_engine=None
    ):

        self.reasoning_engine = (
            reasoning_engine
            if reasoning_engine
            else SalesReasoningEngine()
        )


        self.architecture_engine = (
            architecture_engine
            if architecture_engine
            else ArchitectureRecommendationEngine()
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

            "requirements": opportunity.requirements,

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


        architecture = self.architecture_engine.recommend(
            context
        )


        opportunity.set_solution(
            architecture
        )


        return opportunity