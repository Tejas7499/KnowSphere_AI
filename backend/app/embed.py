import httpx

def embed_text(text):
    
    response = httpx.post(
        "http://localhost:11434/api/embeddings",
        json={
            "model": "nomic-embed-text",
            "prompt": text
        }
    )
    
    
    data = response.json()
    
    
    return data["embedding"]


if __name__ == "__main__":
    vector = embed_text("Hello world")
    print(f"Vector length: {len(vector)}")
    print(vector[:5]) 