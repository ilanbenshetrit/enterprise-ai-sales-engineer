from core.rfp_processor import RFPProcessor


processor = RFPProcessor()


result = processor.analyze_file(
    "knowledge/rubrik.md"
)


print(result)
