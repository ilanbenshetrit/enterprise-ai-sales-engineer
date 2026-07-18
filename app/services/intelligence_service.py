import json

from app.database.database import Database



class IntelligenceService:


    def __init__(
        self
    ):

        self.database = Database()



    def save(
        self,
        opportunity
    ):

        self.database.execute(
            """
            INSERT INTO opportunity_intelligence
            (
                id,
                opportunity_id,
                analysis,
                solution,
                poc_plan,
                implementation_plan,
                demo_plan,
                proposal,
                created_at
            )

            VALUES
            (
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?
            )
            """,
            (

                opportunity.id,

                opportunity.id,

                json.dumps(
                    opportunity.analysis
                ),

                json.dumps(
                    opportunity.solution
                ),

                json.dumps(
                    opportunity.poc_plan
                ),

                json.dumps(
                    opportunity.implementation_plan
                ),

                json.dumps(
                    opportunity.demo_plan
                ),

                json.dumps(
                    getattr(
                        opportunity,
                        "proposal",
                        {}
                    )
                ),

                opportunity.created_at.isoformat()

            )
        )


        return opportunity



    def list_all(
        self
    ):
        """
        Read every persisted intelligence package, joined with its
        opportunity and customer, newest first.
        """

        rows = self.database.fetch_all(
            """
            SELECT
                opportunity_intelligence.id,
                opportunity_intelligence.opportunity_id,
                opportunity_intelligence.analysis,
                opportunity_intelligence.solution,
                opportunity_intelligence.poc_plan,
                opportunity_intelligence.implementation_plan,
                opportunity_intelligence.demo_plan,
                opportunity_intelligence.proposal,
                opportunity_intelligence.created_at,
                opportunities.title,
                customers.name,
                customers.industry,
                customers.size

            FROM opportunity_intelligence

            LEFT JOIN opportunities
                ON opportunity_intelligence.opportunity_id = opportunities.id

            LEFT JOIN customers
                ON opportunities.customer_id = customers.id

            ORDER BY opportunity_intelligence.created_at DESC
            """
        )

        results = []

        for row in rows:

            results.append(
                {
                    "id": row[0],
                    "opportunity_id": row[1],
                    "analysis": json.loads(row[2]) if row[2] else {},
                    "solution": json.loads(row[3]) if row[3] else {},
                    "poc_plan": json.loads(row[4]) if row[4] else {},
                    "implementation_plan": json.loads(row[5]) if row[5] else {},
                    "demo_plan": json.loads(row[6]) if row[6] else {},
                    "proposal": json.loads(row[7]) if row[7] else {},
                    "created_at": row[8],
                    "title": row[9] or "Untitled Opportunity",
                    "customer": {
                        "name": row[10] or "Unknown",
                        "industry": row[11] or "",
                        "size": row[12] or "",
                    },
                }
            )

        return results



    def get_latest(
        self
    ):

        records = self.list_all()

        return records[0] if records else None