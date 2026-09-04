"""
KnowSphere API — thin FastAPI wrapper around the RAG core YOU built
(extract.py, chunk.py, embed.py, store.py, retrieve.py, generate.py).

This file doesn't reimplement your logic — it imports and calls it.
Run from backend/app/:  uvicorn main:app --reload --port 8000
"""

import shutil
import tempfile
from pathlib import Path

import psycopg
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pgvector.psycopg import register_vector
from pydantic import BaseModel

from extract import extract_text
from chunk import chunk_text
from embed import embed_text
from store import store_document
from retrieve import retrieve_chunks
from generate import answer_question
from graph_data import GRAPH

DB_URL = "postgresql://knowsphere:knowsphere@localhost:5433/knowsphere"

app = FastAPI(title="KnowSphere AI — Prototype")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)




DEMO_USERS = {
    "sarah@novatech.demo": {"name": "Sarah Chen", "role": "admin", "projects": None},
    "viewer@novatech.demo": {
        "name": "Restricted Viewer",
        "role": "viewer",
        "projects": ["Project Mercury"],  
    },
}


class LoginRequest(BaseModel):
    email: str


@app.post("/auth/login")
def login(req: LoginRequest):
    user = DEMO_USERS.get(req.email)
    if not user:
        return {"error": "unknown demo user"}
    return {"email": req.email, **user}




@app.post("/documents/upload")
async def upload_document(
    file: UploadFile = File(...),
    project: str = Form(...),
    author: str = Form(...),
):
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir) / file.filename
        with open(tmp_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        text = extract_text(str(tmp_path))
        chunks = chunk_text(text)
        chunks_with_embeddings = [(c, embed_text(c)) for c in chunks]
        document_id = store_document(file.filename, project, author, chunks_with_embeddings)

    return {"document_id": str(document_id), "chunks_created": len(chunks)}



class ChatRequest(BaseModel):
    question: str
    user_email: str | None = None


def retrieve_with_permission(question: str, allowed_projects: list[str], top_k: int = 3):
    """Same retrieval logic as retrieve.py's retrieve_chunks, but filtered
    to only the caller's allowed projects. Kept as a separate function
    here rather than editing retrieve.py, so your original file and its
    test block stay untouched.
    """
    question_vector = embed_text(question)
    conn = psycopg.connect(DB_URL, autocommit=True)
    register_vector(conn)

    results = []
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT dc.content, d.filename
            FROM document_chunks dc
            JOIN documents d ON d.id = dc.document_id
            WHERE d.project = ANY(%s)
            ORDER BY dc.embedding <=> %s::vector
            LIMIT %s
            """,
            (allowed_projects, question_vector, top_k),
        )
        for content, filename in cur.fetchall():
            results.append({"content": content, "filename": filename})
    conn.close()
    return results


@app.post("/chat")
def chat(req: ChatRequest):
    allowed_projects = None
    if req.user_email:
        user = DEMO_USERS.get(req.user_email)
        if user:
            allowed_projects = user["projects"]

    if allowed_projects is None:
        return {"answer": answer_question(req.question)}

    evidence = retrieve_with_permission(req.question, allowed_projects)
    if not evidence:
        return {"answer": "I don't have any accessible knowledge that addresses this question."}

    import httpx

    evidence_text = "".join(f"[{e['filename']}]: {e['content']}\n\n" for e in evidence)
    prompt = f"""Answer the question using ONLY the evidence below.

Evidence:
{evidence_text}

Question:
{req.question}

Answer concisely and mention which document the answer comes from.
"""
    response = httpx.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3.2:3b", "prompt": prompt, "stream": False},
        timeout=60.0,
    )
    return {"answer": response.json()["response"]}




@app.get("/graph")
def get_graph():
    return GRAPH


@app.get("/health")
def health():
    return {"status": "ok"}
