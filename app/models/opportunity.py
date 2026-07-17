from datetime import datetime
import uuid



class Opportunity:


    def __init__(
        self,
        customer_name,
        title,
        description=""
    ):

        self.id = str(uuid.uuid4())

        # Backward compatibility
        self.customer_name = customer_name

        # Future customer entity relation
        self.customer = None

        self.title = title

        self.description = description


        self.requirements = []

        self.environment = {}

        self.analysis = {}

        self.solution = {}

        self.poc_plan = {}


        self.created_at = datetime.now()



    def set_customer(
        self,
        customer
    ):

        self.customer = customer



    def add_requirement(
        self,
        requirement
    ):

        self.requirements.append(
            requirement
        )



    def set_environment(
        self,
        environment
    ):

        self.environment = environment



    def set_analysis(
        self,
        analysis
    ):

        self.analysis = analysis



    def set_solution(
        self,
        solution
    ):

        self.solution = solution



    def set_poc_plan(
        self,
        poc
    ):

        self.poc_plan = poc



    def to_dict(self):

        return {

            "id": self.id,

            "customer_name": self.customer_name,

            "customer": (
                self.customer.to_dict()
                if self.customer
                else None
            ),

            "title": self.title,

            "description": self.description,

            "requirements": self.requirements,

            "environment": self.environment,

            "analysis": self.analysis,

            "solution": self.solution,

            "poc_plan": self.poc_plan,

            "created_at": self.created_at.isoformat()

        }