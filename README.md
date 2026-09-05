# KnowSphere

**Enterprise Organizational Memory & AI Knowledge Platform**

KnowSphere is a company-specific, privacy-conscious AI platform designed to preserve and retrieve the collective knowledge of an organization — while respecting each employee's access rights. It uses Retrieval-Augmented Generation (RAG), permission-aware retrieval, and (in later stages) a knowledge graph to help employees understand a company's projects, architecture, decisions, and history, acting like an experienced senior employee rather than a generic document chatbot.

---

## Table of Contents
- [What This Project Is](#what-this-project-is)
- [The Problem It Solves](#the-problem-it-solves)
- [The Key Differentiator](#the-key-differentiator)
- [What It Uses](#what-it-uses)
- [What We Are Going to Do](#what-we-are-going-to-do)
- [What a README File Generally Contains](#what-a-readme-file-generally-contains)

---

## What This Project Is

KnowSphere is not positioned as an "AI chatbot for interns" — interns are simply its first and easiest user group. The broader product is an **AI organizational memory layer** meant to serve interns, developers, managers, HR/support teams, and leadership, each with different permissions and capabilities.

It is designed to answer questions the way an experienced colleague would — grounded in real internal evidence, aware of who is asking, and honest about what it doesn't know — rather than acting as a generic search-and-summarize tool.

## The Problem It Solves

- New interns and employees struggle to understand large projects and internal terminology.
- Knowledge is scattered across PDFs, DOCX/PPTX files, repositories, tickets, meeting notes, and wikis.
- When experienced employees leave, undocumented context and reasoning is lost.
- Keyword search fails to capture semantic relationships and organizational context.
- Documentation drifts out of date and becomes inconsistent.
- A generic AI assistant risks exposing information a user isn't authorized to see.
- LLMs hallucinate when answers aren't grounded in trusted company information.
- Employees lose time asking senior staff questions that existing knowledge could already answer.

## The Key Differentiator

A basic RAG chatbot can retrieve documents and generate an answer — but it doesn't understand *why* an organization made a decision, *how* projects are connected, *who* owns a component, whether information is outdated, or whether the current user is even allowed to see it.

KnowSphere is built to answer not only *"What does the documentation say?"* but also:
- *"What does the organization know about this?"*
- *"Why was this decision made?"*
- *"Who has worked on this?"*
- *"What changed?"*
- *"What may be outdated?"*
- *"What other systems could be affected?"*

**Example — basic RAG vs. KnowSphere:**
Asked *"How does the payment service work?"*, a basic RAG system retrieves chunks and generates an answer. KnowSphere instead explains the service, identifies related services, points to relevant source code, cites the architecture document and ADR, shows when the information was last updated, gives a confidence indicator, and hides restricted production details from an intern-level user.

## What It Uses

| Component | Recommended Option | Purpose |
|---|---|---|
| LLM runtime | Ollama + open-weight model | Local LLM inference |
| Embeddings | BGE/Nomic-family open embedding model | Semantic retrieval |
| RAG framework | LangChain or LlamaIndex | Retrieval/orchestration |
| Vector DB | Qdrant | Vector/hybrid retrieval |
| Knowledge Graph | Neo4j Community Edition | Graph storage/query |
| Backend | Python + FastAPI | Application/API layer |
| Frontend | React | Web interface |
| Relational DB | PostgreSQL | Users, roles, metadata, application data |
| File parsing | PyMuPDF, python-docx, python-pptx | Document ingestion |
| Git integration | GitPython / Git provider APIs | Repository knowledge |
| Containers | Docker | Packaging and reproducibility |
| Reverse proxy | Nginx | Routing and deployment |

The entire stack is free/open-source for local development — the primary constraint is hardware for LLM inference, not software licensing. The LLM sits behind an abstraction layer so the provider (local or cloud) can be swapped without redesigning the system, and sensitive company knowledge never has to leave the organization's own infrastructure.

## What We Are Going to Do

**Phase 1 — MVP**
Company authentication · roles and basic RBAC · project creation · document upload and parsing · chunking and embeddings · vector search · RAG chatbot · source citations · project-specific knowledge isolation · conversation history

**Phase 2 — Differentiation**
Knowledge Graph · hybrid retrieval (vector + keyword + metadata + graph) · Git ingestion · knowledge freshness tracking · conflict detection · confidence scoring · people/project relationships · knowledge timeline · AI onboarding mode

**Phase 3 — Advanced AI**
The "Why Engine" (explaining *why* a decision was made, not just what it says) · agentic multi-step investigation · codebase understanding (tracing a request through frontend → API → service → database) · project dependency impact analysis · meeting-to-memory extraction · Knowledge Health dashboard · cross-project organizational analytics

**Phase 4 — Enterprise Security**
Project/document-level access policies · attribute-based access control (ABAC) · audit logging · PII detection/redaction · prompt injection protection · retrieval poisoning defenses · private/local LLM deployment

**Immediate next steps:**
1. Freeze the problem statement and product scope
2. Define user roles and permission rules
3. Design the knowledge model — entities and relationships
4. Choose the local development stack
5. Build document ingestion and a clean data pipeline
6. Implement basic RAG and citations
7. Add permission-aware retrieval
8. Introduce Qdrant and Neo4j together
9. Build the knowledge graph explorer
10. Add freshness/conflict detection
11. Add the AI mentor/onboarding mode
12. Connect a Git repository for code/project knowledge
13. Build the Why Engine
14. Create an evaluation dataset and measure quality
15. Harden security and audit logging
16. Package the system with Docker and prepare a polished demonstration

**Design principles guiding all of the above:**
- Evidence over confidence — prefer verifiable evidence to fluent guesses
- Authorization before retrieval — never fetch data a user isn't allowed to see
- Hybrid intelligence — use deterministic software, vector search, graphs, and LLMs for what each does best
- Knowledge is temporal — track when information was created, updated, and verified
- Explain why — preserve decision context, not just final documentation
- Local-first development — keep the prototype free and privacy-friendly
- Evaluation is mandatory — measure retrieval quality, answer quality, security, and latency
- Start small — a reliable MVP before agents and advanced automation

## What a README File Generally Contains

A README is usually the first thing anyone sees when they open a repository, so it typically covers:

- **Project title & short description** — what the project is, in one or two lines
- **Badges** *(optional)* — build status, license, version, code coverage, etc.
- **Table of contents** — for longer READMEs, so readers can jump to a section
- **Problem statement / motivation** — why the project exists, what it solves
- **Features** — a bullet list of what the project does or will do
- **Tech stack** — languages, frameworks, databases, and tools used
- **Architecture / how it works** — a diagram or short explanation of how the pieces fit together
- **Installation / setup instructions** — prerequisites and step-by-step setup
- **Usage examples** — how to actually run or use the project, sample commands or code
- **API reference** *(if applicable)* — endpoints, inputs, outputs
- **Configuration** — environment variables, config files, secrets handling
- **Roadmap** — planned features or milestones
- **Contributing guidelines** — how others can contribute, coding standards, PR process
- **Testing** — how to run tests
- **License** — how others are allowed to use the code
- **Credits / acknowledgments** — team members, references, third-party resources
- **Contact / support** — how to reach the maintainers or report issues

Not every README needs all of these — smaller or personal projects usually keep it to description, features, stack, setup, and usage, while larger or open-source projects tend to include most of the list above.