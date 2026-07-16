"""
Enterprise AI Sales Platform
Agent Service

Connects Streamlit UI with Enterprise Agent.
"""


import sys
from pathlib import Path


# Add project root to Python path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(
        str(PROJECT_ROOT)
    )


from agents.main_agent import EnterpriseAgent



class AgentService:


    def __init__(self):

        self.agent = EnterpriseAgent(
            "Enterprise Sales Engineer Agent"
        )



    def ask(self, question: str):


        response = self.agent.execute(
            question
        )


        return response
