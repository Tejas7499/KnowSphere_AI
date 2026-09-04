import psycopg
from pgvector.psycopg import register_vector

def store_document(filename, project, author, chunks_with_embeddings):

    conn = psycopg.connect(
        "postgresql://knowsphere:knowsphere@localhost:5433/knowsphere",
        autocommit=True
    )
    register_vector(conn)
    
    with conn.cursor() as cur:

        cur.execute(
            "INSERT INTO documents (filename, project, author) VALUES (%s, %s, %s) RETURNING id",
            (filename, project, author)
        )
        document_id = cur.fetchone()[0]
        

        for chunk_index, (chunk_text, embedding_vector) in enumerate(chunks_with_embeddings):
            cur.execute(
                "INSERT INTO document_chunks (document_id, chunk_index, content, embedding) VALUES (%s, %s, %s, %s)",
                (document_id, chunk_index, chunk_text, embedding_vector)
            )
            

    conn.close()
    
    return document_id