CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    filename TEXT,
    project TEXT,
    author TEXT,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE document_chunks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    document_id UUID REFERENCES documents(id) ON DELETE CASCADE,
    chunk_index INT,
    content TEXT,
    embedding vector(768)
);

CREATE TABLE entities (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT_NULL,
    type TEXT NOT_NULL,
    sensitivity_level TEXT DEFAULT 'public',
    attributes JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ DEFAULT now(),
    UNIQUE(name, type)
);

CREATE TABLE relationships (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source_id UUID REFERENCES entities(id) ON DELETE CASCADE,
    target_id UUID REFERENCES entities(id) ON DELETE CASCADE,
    relation_type TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    UNIQUE(source_id, target_id, relation_type)
)