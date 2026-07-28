from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil

from config.settings import settings
from src.document_processing.chunker import DocumentProcessor
from src.ml.predictor import DocumentClassifier

app = FastAPI(
    title="AI Research Assistant & RAG API",
    version="1.0.0",
    description="Backend API for document ingestion, classification, and RAG-powered research queries."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize modules
doc_processor = DocumentProcessor()
classifier = DocumentClassifier(model_path=settings.MODEL_PATH)

os.makedirs("./data/uploads", exist_ok=True)

@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "AI Research Assistant API is up and running!"
    }

@app.post("/api/v1/documents/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    file_path = os.path.join("./data/uploads", file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    # Extract text and process chunks
    doc_id = file.filename.split(".")[0]
    pages = doc_processor.extract_text_with_metadata(file_path, doc_id)
    
    if not pages:
        raise HTTPException(status_code=400, detail="Could not extract text from the PDF.")
        
    chunks = doc_processor.create_chunks(pages)
    
    # Classify based on first page snippet
    sample_text = pages[0]["text"][:500]
    category = classifier.predict_category(sample_text)
    
    return {
        "filename": file.filename,
        "doc_id": doc_id,
        "total_pages": len(pages),
        "total_chunks": len(chunks),
        "predicted_category": category,
        "message": "Document successfully uploaded, parsed, and classified!"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)