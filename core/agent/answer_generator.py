"""
Enterprise AI Sales Platform
Answer Generator

Generates business-oriented answers
from retrieved knowledge.
"""


class AnswerGenerator:
    """
    Generates answers using retrieved knowledge chunks.
    """


    def generate(
        self,
        question: str,
        context: list[dict]
    ) -> str:
        """
        Generate an answer from retrieved chunks.
        """


        if not context:

            return (
                "I could not find relevant information "
                "in the knowledge base."
            )


        answer = []

        answer.append(
            f"Question: {question}\n"
        )

        answer.append(
            "Based on the available knowledge:\n"
        )


        for chunk in context:

            answer.append(
                chunk["content"]
            )


        answer.append(
            "\n\nSummary:\n"
        )

        answer.append(
            "The solution provides capabilities "
            "that address the requested requirements "
            "based on the available product information."
        )


        return "\n".join(answer)