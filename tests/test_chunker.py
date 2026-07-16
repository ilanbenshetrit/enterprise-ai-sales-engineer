from core.knowledge.chunker import DocumentChunker


chunker = DocumentChunker(
    chunk_size=50
)

text = """
Rubrik is a Cyber Resilience platform.

Main capabilities:
Immutable Backup.
Ransomware Recovery.
Cloud Data Protection.
"""


chunks = chunker.split(text)


print("Chunks created successfully")
print("--------------------------")


for index, chunk in enumerate(chunks):
    print(f"Chunk {index + 1}:")
    print(chunk)
    print("--------------------------")


print(f"Total chunks: {len(chunks)}")