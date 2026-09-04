import httpx
from retrieve import retrieve_chunks

def answer_question(question):
    retrieved_chunks = retrieve_chunks(question)
    
    evidence_text = ""
    for chunk in retrieved_chunks:
        evidence_text += f"[{chunk['filename']}]: {chunk['content']}\n\n"
        
    prompt = f"""Answer the question using ONLY the evidence below.

Evidence:
{evidence_text}

Question:
{question}

Answer concisely and mention which document the answer comes from.
"""

    response = httpx.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:3b",
            "prompt": prompt,
            "stream": False
        },
        timeout=60.0
    )
    
    answer = response.json()["response"]
    return answer

if __name__ == "__main__":
    question = "Why was PostgreSQL selected for Project Alpha?"
    print(answer_question(question))