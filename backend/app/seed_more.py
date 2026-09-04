

from extract import extract_text
from chunk import chunk_text
from embed import embed_text
from store import store_document

# filename -> (project, author) — place these .md files in backend/ (same
# folder as adr-001.md) before running this script.
DOCS = {
    "architecture-guide-project-alpha.md": ("Project Alpha", "Sarah Chen"),
    "sprint-retro-project-mercury.md": ("Project Mercury", "Priya Shah"),
}

for filename, (project, author) in DOCS.items():
    path = f"../{filename}"
    text = extract_text(path)
    chunks = chunk_text(text)
    chunks_with_embeddings = [(c, embed_text(c)) for c in chunks]
    document_id = store_document(filename, project, author, chunks_with_embeddings)
    print(f"Stored {filename} -> id={document_id}, chunks={len(chunks_with_embeddings)}")

print("Done.")
