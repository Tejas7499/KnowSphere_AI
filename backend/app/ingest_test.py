from app.extract import extract_text
from app.chunk import chunk_text
from app.embed import embed_text
from app.store import store_document

text = extract_text("../adr-001.md")
chunks = chunk_text(text)

chunks_with_embeddings = []
for c in chunks:
    vector = embed_text(c)
    chunks_with_embeddings.append((c, vector))

document_id = store_document("adr-001.md", "Project Alpha", "Rahul Mehta", chunks_with_embeddings)
print(f"Stored document with id: {document_id}")
print(f"Chunks stored: {len(chunks_with_embeddings)}")