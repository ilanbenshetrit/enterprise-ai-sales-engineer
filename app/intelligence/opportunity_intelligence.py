from app.agents.reasoning_engine import SalesReasoningEngine
from app.architecture.recommendation_engine import ArchitectureRecommendationEngine
from app.planning.poc_planner import POCPlanner
from app.implementation.implementation_planner import ImplementationPlanner
from app.demo.demo_planner import DemoPlanner
from app.proposal.proposal_generator import ProposalGenerator
from app.services.intelligence_service import IntelligenceService



class OpportunityIntelligence:


    def __init__(
        self,
        reasoning_engine=None,
        architecture_engine=None,
        poc_planner=None,
        implementation_planner=None,
        demo_planner=None,
        proposal_generator=None,
        intelligence_service=None
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


        self.poc_planner = (
            poc_planner
            if poc_planner
            else POCPlanner()
        )


        self.implementation_planner = (
            implementation_planner
            if implementation_planner
            else ImplementationPlanner()
        )


        self.demo_planner = (
            demo_planner
            if demo_planner
            else DemoPlanner()
        )


        self.proposal_generator = (
            proposal_generator
            if proposal_generator
            else ProposalGenerator()
        )


        self.intelligence_service = (
            intelligence_service
            if intelligence_service
            else IntelligenceService()
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


        poc_context = {

            "solution": architecture,

            "customer_context": context["customer_context"]

        }


        poc_plan = self.poc_planner.create_plan(
            poc_context
        )


        opportunity.set_poc_plan(
            poc_plan
        )


        implementation_context = {

            "solution": architecture,

            "customer_context": context["customer_context"]

        }


        implementation_plan = self.implementation_planner.create_plan(
            implementation_context
        )


        opportunity.set_implementation_plan(
            implementation_plan
        )


        demo_context = {

            "requirements": opportunity.requirements,

            "solution": architecture,

            "customer_context": context["customer_context"]

        }


        demo_plan = self.demo_planner.create_plan(
            demo_context
        )


        opportunity.set_demo_plan(
            demo_plan
        )


        proposal_context = {

            "customer_context": context["customer_context"],

            "analysis": analysis,

            "solution": architecture,

            "poc_plan": poc_plan,

            "implementation_plan": implementation_plan,

            "demo_plan": demo_plan

        }


        proposal = self.proposal_generator.generate(
            proposal_context
        )


        opportunity.set_proposal(
            proposal
        )


        # Save AI Intelligence Package

        self.intelligence_service.save(
            opportunity
        )


        return opportunity