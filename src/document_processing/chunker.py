import fitz  # PyMuPDF
from typing import List, Dict, Any

class DocumentProcessor:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 150):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def extract_text_with_metadata(self, pdf_path: str, doc_id: str) -> List[Dict[str, Any]]:
        """Extracts text page-by-page from a PDF document."""
        doc = fitz.open(pdf_path)
        extracted_pages = []

        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text("text").strip()
            if text:
                extracted_pages.append({
                    "doc_id": doc_id,
                    "page_number": page_num + 1,
                    "text": text
                })
        doc.close()
        return extracted_pages

    def create_chunks(self, pages_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Splits page text into overlapping chunks while preserving page metadata."""
        chunks = []
        chunk_id = 0

        for page in pages_data:
            text = page["text"]
            start = 0
            while start < len(text):
                end = start + self.chunk_size
                chunk_text = text[start:end]

                chunks.append({
                    "chunk_id": f"{page['doc_id']}_c{chunk_id}",
                    "doc_id": page["doc_id"],
                    "page_number": page["page_number"],
                    "text": chunk_text
                })

                chunk_id += 1
                start += (self.chunk_size - self.chunk_overlap)

        return chunks