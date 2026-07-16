from core.document.document_loader import DocumentLoader


loader = DocumentLoader()

content = loader.load("knowledge/rubrik.md")

print("Document loaded successfully")
print("----------------------------")
print(content[:300])
print("----------------------------")
print(f"Characters: {len(content)}")