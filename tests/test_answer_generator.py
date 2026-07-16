"""
Answer Generator Test
"""

from core.document.document_loader import DocumentLoader
from core.knowledge.chunker import DocumentChunker
from core.knowledge.knowledge_store import KnowledgeStore
from core.knowledge.retriever import KnowledgeRetriever
from core.agent.answer_generator import AnswerGenerator


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


# Store knowledge

store = KnowledgeStore()

store.add_chunks(
    chunks
)


# Retrieve relevant knowledge

retriever = KnowledgeRetriever(
    store
)


question = (
    "How does Rubrik protect against ransomware?"
)


context = retriever.search(
    question
)


# Generate answer

generator = AnswerGenerator()


answer = generator.generate(
    question,
    context
)


print("AI Sales Engineer Answer")
print("========================")
print(answer)