"""
Enterprise AI Sales Platform
RFP Analyzer Tool v2

Analyzes customer RFP content.
"""


class RFPAnalyzerTool:


    KEYWORDS = {

        "requirements": [
            "backup",
            "recovery",
            "ransomware",
            "security",
            "cloud",
            "compliance",
            "resilience"
        ],


        "risks": [
            "gap",
            "risk",
            "challenge",
            "limitation",
            "failure"
        ]

    }



    def run(self, rfp_text: str):


        result = {

            "requirements": [],

            "technical_questions": [],

            "risks": [],

            "solution_direction": []

        }


        text = rfp_text.lower()



        # Requirement extraction

        for keyword in self.KEYWORDS["requirements"]:

            if keyword in text:

                result["requirements"].append(
                    keyword
                )



        # Risk detection

        for keyword in self.KEYWORDS["risks"]:

            if keyword in text:

                result["risks"].append(
                    keyword
                )



        # Generate discovery questions

        if "backup" in text:

            result["technical_questions"].append(
                "What is your current backup architecture?"
            )


        if "recovery" in text:

            result["technical_questions"].append(
                "What are your RTO and RPO requirements?"
            )


        if "cloud" in text:

            result["technical_questions"].append(
                "Which cloud platforms are currently in use?"
            )


        # Solution mapping

        if "ransomware" in text:

            result["solution_direction"].append(
                "Implement ransomware recovery strategy"
            )


        if "backup" in text:

            result["solution_direction"].append(
                "Design immutable backup architecture"
            )


        if "cloud" in text:

            result["solution_direction"].append(
                "Integrate hybrid cloud protection"
            )


        return result
