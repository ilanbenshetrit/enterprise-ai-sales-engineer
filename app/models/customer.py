from datetime import datetime
import uuid



class Customer:


    def __init__(
        self,
        name,
        industry="",
        size=""
    ):

        self.id = str(uuid.uuid4())

        self.name = name

        self.industry = industry

        self.size = size


        self.environment = {}

        self.compliance = []

        self.challenges = []

        self.business_goals = []


        self.created_at = datetime.now()



    def set_environment(
        self,
        environment
    ):

        self.environment = environment



    def add_compliance(
        self,
        compliance
    ):

        self.compliance.append(
            compliance
        )



    def add_challenge(
        self,
        challenge
    ):

        self.challenges.append(
            challenge
        )



    def add_business_goal(
        self,
        goal
    ):

        self.business_goals.append(
            goal
        )



    def to_dict(self):

        return {

            "id": self.id,

            "name": self.name,

            "industry": self.industry,

            "size": self.size,

            "environment": self.environment,

            "compliance": self.compliance,

            "challenges": self.challenges,

            "business_goals": self.business_goals,

            "created_at": self.created_at.isoformat()

        }