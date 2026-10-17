import os
import json
import psycopg
from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv("DATABASE_URL")

def search_existing_entities(name: str, entity_type: str) -> str:

    with psycopg.connect(DB_URL, autocommit=True) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, name, type FROM entities WHERE name ILIKE %s AND type = %s",
                (f"%{name}%", entity_type)
            )
            result = cur.fetchone()
            if result:
                return json.dumps({"status": "found", "id": str(result[0]), "name": result[1], "type": result[2]})
            return json.dumps({"status": "not_found"})

def create_entity(name: str, entity_type: str, sensitivity_level: str = "public", attributes: dict = None) -> str:

    if attributes is None:
        attributes = {}
    
    with psycopg.connect(DB_URL, autocommit=True) as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    """
                    INSERT INTO entities (name, type, sensitivity_level, attributes) 
                    VALUES (%s, %s, %s, %s) RETURNING id
                    """,
                    (name, entity_type, sensitivity_level, json.dumps(attributes))
                )
                entity_id = cur.fetchone()[0]
                return json.dumps({"status": "success", "id": str(entity_id), "message": f"Created {name}"})
            except psycopg.errors.UniqueViolation:
                return json.dumps({"status": "error", "message": f"Entity {name} of type {entity_type} already exists."})

def create_relationship(source_id: str, target_id: str, relation_type: str) -> str:

    with psycopg.connect(DB_URL, autocommit=True) as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO relationships (source_id, target_id, relation_type) VALUES (%s, %s, %s) RETURNING id",
                    (source_id, target_id, relation_type)
                )
                rel_id = cur.fetchone()[0]
                return json.dumps({"status": "success", "id": str(rel_id), "message": f"Linked {source_id} -> {target_id}"})
            except psycopg.errors.UniqueViolation:
                 return json.dumps({"status": "error", "message": "Relationship already exists."})

def finish_extraction() -> str:
    return json.dumps({"status": "complete", "message": "Extraction finished."})