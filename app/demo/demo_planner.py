class DemoPlanner:


    def create_plan(
        self,
        context
    ):


        requirements = context.get(
            "requirements",
            []
        )


        customer_context = context.get(
            "customer_context",
            {}
        )


        demo_plan = {


            "objective": "",


            "storyline": [

            ],


            "demo_flows": [

            ],


            "customer_value": [

            ],


            "questions_to_validate": [

            ]

        }



        if "Immutable Backup" in requirements:


            demo_plan["objective"] = (
                "Demonstrate cyber resilience "
                "and ransomware recovery capabilities"
            )


            demo_plan["storyline"] = [

                "Understand current data protection challenges",

                "Show ransomware attack scenario",

                "Demonstrate recovery capabilities",

                "Validate business continuity"

            ]


            demo_plan["demo_flows"] = [

                {

                    "name": "Ransomware Recovery Demo",

                    "steps": [

                        "Show protected workload",

                        "Simulate ransomware event",

                        "Recover clean data copy",

                        "Validate recovery outcome"

                    ]

                },


                {

                    "name": "Policy Management Demo",

                    "steps": [

                        "Create protection policy",

                        "Apply security controls",

                        "Review compliance status"

                    ]

                }

            ]


            demo_plan["customer_value"] = [

                "Reduce business downtime",

                "Improve ransomware readiness",

                "Increase cyber resilience"

            ]


            demo_plan["questions_to_validate"] = [

                "What workloads are most critical?",

                "What recovery time is required?",

                "Which compliance requirements must be met?"

            ]



        return demo_plan