import psycopg
from pgvector.psycopg import register_vector
from embed import embed_text

def retrieve_chunks(question, top_k=3):
    question_vector = embed_text(question)
    
    
    conn = psycopg.connect(
        "postgresql://knowsphere:knowsphere@localhost:5433/knowsphere",
        autocommit=True
    )
    register_vector(conn)
    
    results = []
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT dc.content, d.filename
            FROM document_chunks dc
            JOIN documents d ON d.id = dc.document_id
            ORDER BY dc.embedding <=> %s::vector
            LIMIT %s
            """,
            (question_vector, top_k)
        )
        
        
        for row in cur.fetchall():
            results.append({"content": row[0], "filename": row[1]})
            
    conn.close()
    return results


if __name__ == "__main__":
    test_question = "What database are we using for Project Alpha?"
    print(f"Question: {test_question}\n")
    
    closest_chunks = retrieve_chunks(test_question, top_k=1)
    
    print("--- Top Match Found ---")
    for chunk in closest_chunks:
        print(f"[{chunk['filename']}] {chunk['content'][:150]}...")