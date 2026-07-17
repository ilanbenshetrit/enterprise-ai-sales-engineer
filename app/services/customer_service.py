from app.models.customer import Customer



class CustomerService:


    def __init__(self):

        self.customers = {}



    def create(
        self,
        name,
        industry="",
        size=""
    ):

        customer = Customer(
            name,
            industry,
            size
        )


        self.customers[
            customer.id
        ] = customer


        return customer



    def get(
        self,
        customer_id
    ):

        return self.customers.get(
            customer_id
        )



    def set_environment(
        self,
        customer_id,
        environment
    ):

        customer = self.get(
            customer_id
        )


        if not customer:
            return None


        customer.set_environment(
            environment
        )


        return customer



    def add_compliance(
        self,
        customer_id,
        compliance
    ):

        customer = self.get(
            customer_id
        )


        if not customer:
            return None


        customer.add_compliance(
            compliance
        )


        return customer



    def add_challenge(
        self,
        customer_id,
        challenge
    ):

        customer = self.get(
            customer_id
        )


        if not customer:
            return None


        customer.add_challenge(
            challenge
        )


        return customer



    def add_business_goal(
        self,
        customer_id,
        goal
    ):

        customer = self.get(
            customer_id
        )


        if not customer:
            return None


        customer.add_business_goal(
            goal
        )


        return customer



    def list_all(self):

        return [

            customer.to_dict()

            for customer in self.customers.values()

        ]