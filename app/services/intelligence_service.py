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