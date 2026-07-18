from app.models.opportunity import Opportunity
from app.database.database import Database



class OpportunityService:


    def __init__(self):

        self.opportunities = {}

        self.database = Database()



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



        self.database.execute(
            """
            INSERT INTO opportunities
            (
                id,
                customer_id,
                title,
                description,
                created_at
            )

            VALUES
            (
                ?,
                ?,
                ?,
                ?,
                ?
            )
            """,
            (
                opportunity.id,
                None,
                opportunity.title,
                opportunity.description,
                opportunity.created_at.isoformat()
            )
        )


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


        self.database.execute(
            """
            UPDATE opportunities

            SET customer_id = ?

            WHERE id = ?
            """,
            (
                customer.id,
                opportunity_id
            )
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



    def list_all(
        self
    ):

        return [

            opportunity.to_dict()

            for opportunity in self.opportunities.values()

        ]



    def load_all(
        self
    ):
        """
        Read persisted opportunities from the database, joined with
        their customer record. Unlike list_all(), this survives
        across service instances/reruns.
        """

        rows = self.database.fetch_all(
            """
            SELECT
                opportunities.id,
                opportunities.title,
                opportunities.description,
                opportunities.created_at,
                customers.id,
                customers.name,
                customers.industry,
                customers.size

            FROM opportunities

            LEFT JOIN customers
                ON opportunities.customer_id = customers.id

            ORDER BY opportunities.created_at DESC
            """
        )

        results = []

        for row in rows:

            results.append(
                {
                    "id": row[0],
                    "title": row[1],
                    "description": row[2],
                    "created_at": row[3],
                    "customer": {
                        "id": row[4],
                        "name": row[5] or "Unknown",
                        "industry": row[6] or "",
                        "size": row[7] or "",
                    } if row[4] else None,
                }
            )

        return results