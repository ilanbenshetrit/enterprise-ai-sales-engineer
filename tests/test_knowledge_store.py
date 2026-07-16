"""
Knowledge Store Test
"""

from core.document.document_loader import DocumentLoader
from core.knowledge.chunker import DocumentChunker
from core.knowledge.knowledge_store import KnowledgeStore


# Load document

loader = DocumentLoader()

document = loader.load(
    "knowledge/rubrik.md"
)


# Create chunks

chunker = DocumentChunker(
    chunk_size=100
)

chunks = chunker.split(
    document,
    source="rubrik.md"
)


# Store chunks

store = KnowledgeStore()

store.add_chunks(
    chunks
)


# Validate

print("Knowledge Store loaded successfully")
print("==============================")

print(
    f"Total chunks stored: {store.count()}"
)


print("\nStored knowledge:")

for item in store.get_all():

    print("------------------------------")
    print(f"Chunk ID: {item['chunk_id']}")
    print(f"Source: {item['source']}")
    print(item["content"])