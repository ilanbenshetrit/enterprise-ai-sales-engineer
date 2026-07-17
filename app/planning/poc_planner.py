class POCPlanner:


    def create_plan(
        self,
        context
    ):


        solution = context.get(
            "solution",
            {}
        )


        customer_context = context.get(
            "customer_context",
            {}
        )


        poc_plan = {


            "duration": "4 weeks",


            "scope": [

                "Deploy solution components",

                "Configure protection policies",

                "Execute recovery validation"

            ],


            "test_cases": [

                "Ransomware recovery test",

                "Backup restore validation",

                "RTO/RPO validation"

            ],


            "success_criteria": [

                "Successful workload recovery",

                "Meet defined RTO targets",

                "Validate operational readiness"

            ],


            "required_resources": [

                "Customer IT Team",

                "Solution Engineer",

                "Infrastructure Owner"

            ]

        }


        return poc_plan