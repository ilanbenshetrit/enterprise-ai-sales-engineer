from datetime import datetime

from app.models.customer import Customer
from app.database.database import Database



class CustomerService:


    def __init__(self):

        self.customers = {}

        self.database = Database()



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



        self.database.execute(
            """
            INSERT INTO customers
            (
                id,
                name,
                industry,
                size,
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
                customer.id,
                customer.name,
                customer.industry,
                customer.size,
                customer.created_at.isoformat()
            )
        )


        return customer



    def get(
        self,
        customer_id
    ):

        return self.customers.get(
            customer_id
        )



    def load_all(
        self
    ):

        rows = self.database.fetch_all(
            """
            SELECT
                id,
                name,
                industry,
                size,
                created_at

            FROM customers
            """
        )


        customers = []


        for row in rows:

            customer = Customer(
                row[1],
                row[2],
                row[3]
            )


            customer.id = row[0]


            customer.created_at = datetime.fromisoformat(
                row[4]
            )


            self.customers[
                customer.id
            ] = customer


            customers.append(
                customer
            )


        return customers



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



    def list_all(
        self
    ):

        return [

            customer.to_dict()

            for customer in self.customers.values()

        ]