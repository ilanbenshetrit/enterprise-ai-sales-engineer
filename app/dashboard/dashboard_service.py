from app.services.customer_service import CustomerService
from app.services.opportunity_service import OpportunityService
from app.intelligence.opportunity_intelligence import OpportunityIntelligence



class DashboardService:


    def __init__(self):

        self.customer_service = CustomerService()

        self.opportunity_service = OpportunityService()

        self.intelligence = OpportunityIntelligence()



    def create_demo_opportunity(
        self
    ):


        customer = self.customer_service.create(
            "Bank XYZ",
            "Finance",
            "5000 Employees"
        )


        self.customer_service.set_environment(
            customer.id,
            {
                "cloud": "AWS",
                "platform": "VMware"
            }
        )


        self.customer_service.add_compliance(
            customer.id,
            "PCI-DSS"
        )


        self.customer_service.add_challenge(
            customer.id,
            "Ransomware Recovery"
        )


        opportunity = self.opportunity_service.create(
            "Bank XYZ",
            "Cyber Resilience Project"
        )


        self.opportunity_service.assign_customer(
            opportunity.id,
            customer
        )


        self.opportunity_service.add_requirement(
            opportunity.id,
            "Immutable Backup"
        )


        result = self.intelligence.analyze(
            opportunity
        )


        return result.to_dict()



    def create_opportunity(
        self,
        customer_name,
        industry,
        size,
        requirements
    ):


        customer = self.customer_service.create(
            customer_name,
            industry,
            size
        )


        opportunity = self.opportunity_service.create(
            customer_name,
            "Cyber Resilience Project"
        )


        self.opportunity_service.assign_customer(
            opportunity.id,
            customer
        )


        for requirement in requirements:


            self.opportunity_service.add_requirement(
                opportunity.id,
                requirement
            )


        result = self.intelligence.analyze(
            opportunity
        )


        return result.to_dict()



    def get_dashboard_data(
        self
    ):

        opportunity = self.create_demo_opportunity()


        return {

            "customer": opportunity.get(
                "customer"
            ),

            "analysis": opportunity.get(
                "analysis"
            ),

            "solution": opportunity.get(
                "solution"
            ),

            "poc_plan": opportunity.get(
                "poc_plan"
            ),

            "implementation_plan": opportunity.get(
                "implementation_plan"
            ),

            "demo_plan": opportunity.get(
                "demo_plan"
            ),

            "proposal": opportunity.get(
                "proposal"
            )

        }