"""
Enterprise AI Sales Platform
Document Chunker v2

Splits documents while preserving semantic structure.
"""


class DocumentChunker:
    """
    Splits documents into meaningful chunks.
    """

    def __init__(self, chunk_size: int = 500):

        self.chunk_size = chunk_size


    def split(self, text: str, source: str = "unknown") -> list[dict]:
        """
        Split text into chunks and keep metadata.
        """

        if not text:
            return []


        paragraphs = [
            paragraph.strip()
            for paragraph in text.split("\n\n")
            if paragraph.strip()
        ]


        chunks = []
        current_chunk = ""
        chunk_id = 1


        for paragraph in paragraphs:

            # Check if adding paragraph exceeds limit

            if (
                len(current_chunk) + len(paragraph)
                > self.chunk_size
            ):

                if current_chunk:

                    chunks.append(
                        {
                            "chunk_id": chunk_id,
                            "source": source,
                            "content": current_chunk.strip()
                        }
                    )

                    chunk_id += 1

                    current_chunk = ""


            current_chunk += paragraph + "\n\n"


        # Add remaining content

        if current_chunk.strip():

            chunks.append(
                {
                    "chunk_id": chunk_id,
                    "source": source,
                    "content": current_chunk.strip()
                }
            )


        return chunks