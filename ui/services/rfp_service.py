"""
Enterprise AI Sales Platform
RFP Service

Connects Streamlit UI with RFP Processing engine.
"""

from pathlib import Path
import tempfile
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))


from core.rfp_processor import RFPProcessor


class RFPService:


    def __init__(self):

        self.processor = RFPProcessor()


    def analyze(self, uploaded_file):

        temp_dir = Path(
            tempfile.gettempdir()
        )

        temp_file = temp_dir / uploaded_file.name


        with open(
            temp_file,
            "wb"
        ) as file:

            file.write(
                uploaded_file.getbuffer()
            )


        result = self.processor.analyze_file(
            str(temp_file)
        )


        return result
