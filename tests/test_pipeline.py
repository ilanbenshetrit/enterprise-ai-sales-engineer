"""
Enterprise AI Sales Platform
Document Processing Pipeline Test
"""

from core.document.document_loader import DocumentLoader
from core.knowledge.chunker import DocumentChunker


# Step 1 - Load document

loader = DocumentLoader()

document = loader.load(
    "knowledge/rubrik.md"
)


print("Document loaded successfully")
print("============================")
print(f"Characters: {len(document)}")


# Step 2 - Create chunks

chunker = DocumentChunker(
    chunk_size=100
)


chunks = chunker.split(
    document,
    source="rubrik.md"
)


print("\nChunks created successfully")
print("============================")


# Step 3 - Display chunks with metadata

for chunk in chunks:

    print(f"\nChunk ID: {chunk['chunk_id']}")
    print(f"Source: {chunk['source']}")
    print("----------------------------")
    print(chunk["content"])


print(
    f"\nTotal chunks: {len(chunks)}"
)