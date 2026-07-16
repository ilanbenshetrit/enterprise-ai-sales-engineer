"""
Enterprise AI Sales Platform
Retriever v2 Test
"""

from core.document.document_loader import DocumentLoader
from core.knowledge.chunker import DocumentChunker
from core.knowledge.knowledge_store import KnowledgeStore
from core.knowledge.retriever import KnowledgeRetriever


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
print(f"Total chunks: {len(chunks)}")


# Step 3 - Store chunks

store = KnowledgeStore()

store.add_chunks(
    chunks
)


print("\nKnowledge Store ready")
print("============================")


# Step 4 - Create Retriever

retriever = KnowledgeRetriever(
    store
)


# Step 5 - Search query

query = "How does Rubrik protect cyber attacks"


print("\nSearch Query:")
print(query)

print("\nRetrieval Results")
print("============================")


results = retriever.search(
    query,
    top_k=3
)


print(
    f"Results found: {len(results)}"
)


# Step 6 - Display results

for result in results:

    print("----------------------------")
    print(f"Chunk ID: {result['chunk_id']}")
    print(f"Source: {result['source']}")
    print(result["content"])