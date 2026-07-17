class SalesReasoningEngine:


    def analyze(
        self,
        context
    ):


        task = context["task"]

        knowledge = context["knowledge"]


        result = {

            "task": task,

            "discovery_questions": [],

            "technical_risks": [],

            "solution_direction": [],

            "next_steps": []

        }



        if task == "solution_design":


            result["discovery_questions"] = [

                "What is your current backup architecture?",

                "What are your RTO and RPO requirements?",

                "Which cloud platforms are currently in use?"

            ]



            result["technical_risks"] = [

                "No immutable backup strategy",

                "Insufficient ransomware recovery plan"

            ]



            result["solution_direction"] = [

                "Design immutable backup architecture",

                "Implement ransomware recovery strategy",

                "Integrate hybrid cloud protection"

            ]



            result["next_steps"] = [

                "Schedule technical discovery session",

                "Review current environment",

                "Define target architecture"

            ]



        return result