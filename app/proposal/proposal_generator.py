class ProposalGenerator:


    def generate(
        self,
        context
    ):


        customer_context = context.get(
            "customer_context",
            {}
        )


        analysis = context.get(
            "analysis",
            {}
        )


        solution = context.get(
            "solution",
            {}
        )


        poc_plan = context.get(
            "poc_plan",
            {}
        )


        implementation_plan = context.get(
            "implementation_plan",
            {}
        )


        demo_plan = context.get(
            "demo_plan",
            {}
        )



        proposal = {


            "executive_summary": (

                "This proposal provides a recommended "
                "solution approach based on customer "
                "requirements and business objectives."

            ),


            "customer_challenge": (

                analysis.get(
                    "technical_risks",
                    []
                )

            ),


            "recommended_solution": (

                analysis.get(
                    "solution_direction",
                    []
                )

            ),


            "architecture_overview": solution,


            "implementation_approach": (

                implementation_plan.get(
                    "phases",
                    []
                )

            ),


            "poc_scope": (

                poc_plan.get(
                    "scope",
                    []
                )

            ),


            "demo_strategy": demo_plan,


            "success_metrics": (

                poc_plan.get(
                    "success_criteria",
                    []
                )

            ),


            "next_steps": (

                analysis.get(
                    "next_steps",
                    []
                )

            )

        }


        return proposal