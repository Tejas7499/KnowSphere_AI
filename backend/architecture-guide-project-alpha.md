# Project Alpha — Architecture Guide

**Maintained by:** Sarah Chen, Rahul Mehta
**Project:** Project Alpha

## Overview

Project Alpha is NovaTech Systems' e-commerce platform. Backend: Python +
FastAPI. Primary database: PostgreSQL (see ADR-001 for selection
rationale). Caching layer: Redis. Frontend: React.

## Changes Since ADR-001

After the initial PostgreSQL decision, the following changes were made as
traffic grew:

1. Priya Shah led the introduction of Redis as a caching layer in front of
   PostgreSQL to reduce read load on product catalog queries.
2. David Kumar configured PostgreSQL read replicas to handle growing
   search and catalog browsing traffic separately from order processing.
3. Rahul Mehta tuned the pgvector HNSW index parameters after benchmarking
   flagged slow vector search at scale, improving semantic search latency
   by roughly 40%.

## Related Technologies

PostgreSQL, Redis, FastAPI, React, Docker.
