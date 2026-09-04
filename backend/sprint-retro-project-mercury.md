# Sprint Retrospective — Project Mercury, Sprint 12

**Project:** Project Mercury
**Attendees:** Sarah Chen, Priya Shah, David Kumar

## Summary

Project Mercury is NovaTech Systems' internal analytics platform. Sarah
Chen joined as technical advisor for Project Mercury in March 2026,
splitting her time between Project Alpha and Project Mercury to help the
team apply lessons learned from Project Alpha's database architecture
decisions.

## What Went Well

- The team migrated the analytics ingestion pipeline to use the same
  PostgreSQL + pgvector pattern validated on Project Alpha, avoiding a
  separate evaluation cycle.
- David Kumar's backup automation work from Project Alpha was reused
  directly for Project Mercury's infrastructure.

## Action Items

- Sarah Chen to review Project Mercury's schema design against Project
  Alpha's patterns.
- Priya Shah to document the ingestion pipeline.
- David Kumar to extend automated backup coverage to Project Mercury.
