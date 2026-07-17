from app.models.opportunity import Opportunity



class OpportunityService:


    def __init__(self):

        self.opportunities = {}



    def create(
        self,
        customer_name,
        title,
        description=""
    ):

        opportunity = Opportunity(
            customer_name,
            title,
            description
        )


        self.opportunities[
            opportunity.id
        ] = opportunity


        return opportunity



    def get(
        self,
        opportunity_id
    ):

        return self.opportunities.get(
            opportunity_id
        )



    def assign_customer(
        self,
        opportunity_id,
        customer
    ):

        opportunity = self.get(
            opportunity_id
        )


        if not opportunity:
            return None


        opportunity.set_customer(
            customer
        )


        return opportunity



    def add_requirement(
        self,
        opportunity_id,
        requirement
    ):

        opportunity = self.get(
            opportunity_id
        )


        if not opportunity:
            return None


        opportunity.add_requirement(
            requirement
        )


        return opportunity



    def update_analysis(
        self,
        opportunity_id,
        analysis
    ):

        opportunity = self.get(
            opportunity_id
        )


        if not opportunity:
            return None


        opportunity.set_analysis(
            analysis
        )


        return opportunity



    def list_all(self):

        return [

            opportunity.to_dict()

            for opportunity in self.opportunities.values()

        ]