"""
Enterprise AI Sales Platform
RFP Processor

Connects documents with RFP analysis.
"""


from core.document.document_loader import DocumentLoader
from tools.rfp_tool import RFPAnalyzerTool



class RFPProcessor:


    def __init__(self):

        self.loader = DocumentLoader()

        self.analyzer = RFPAnalyzerTool()



    def analyze_file(self, file_path: str):


        # Load document

        text = self.loader.load(
            file_path
        )


        # Analyze RFP content

        result = self.analyzer.run(
            text
        )


        return result
