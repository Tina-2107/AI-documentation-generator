# 🤖 AI Documentation Generator

An AI-powered application that analyzes source code and automatically generates high-quality technical documentation using FastAPI, Python AST, Large Language Models (LLMs), and Retrieval-Augmented Generation (RAG).

---

## 🚀 Project Goal

The goal of this project is to help developers generate documentation automatically instead of writing it manually.

The application will be able to generate:

- README files
- Function documentation
- Class documentation
- API documentation
- Project summaries
- Code explanations

Users will upload their project, and the AI will analyze the codebase to produce well-structured documentation.

---

## 🛠️ Tech Stack

### Current Stack

- Python
- FastAPI

### Planned Stack

**AI**

- OpenAI API
- Python AST
- ChromaDB

**Frontend**

- React

---

## 📁 Project Structure

```text
ai-documentation-generator/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── routes/
│   ├── services/
│   ├── models/
│   └── utils/
│
├── docs/
├── tests/
├── uploads/
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone <your-repository-url>
cd ai-documentation-generator
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the server

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 📅 Development Progress

### ✅ Day 1

- Initialized the project
- Created the FastAPI backend
- Configured the virtual environment
- Designed the initial project structure
- Initialized the GitHub repository
- Created the first API endpoints
- Added project documentation and MIT License

### ✅ Day 2

- Added file upload endpoint
- Implemented file storage service
- Organized backend into routes and services
- Added basic file validation

## Day 3 Progress

- Implemented Python AST parser
- Extracted functions and classes
- Parsed import statements
- Added code analysis endpoint

## Day 4 Progress

- Integrated Google Gemini API
- Added AI documentation generation service
- Created documentation generation endpoint
- Improved prompts for Markdown output

## Day 5 Progress

- Added prompt templates
- Built documentation service
- Generated Markdown files
- Saved documentation automatically

## Day 6 Progress

- Added ZIP project upload support
- Implemented project extraction and recursive directory scanning
- Added filtering for ignored directories such as `.git`, `venv`, `node_modules`, and `__pycache__`
- Integrated AST analysis for all Python files in an uploaded project
- Added repository-level project analysis endpoint

## Day 7 Progress

- Completed the end-to-end AI documentation pipeline:

- Project ZIP → Secure Extraction → Repository Scanner → AST Analysis → Context Builder → Gemini → Markdown Documentation

## Day 8 Progress

- Added AST-aware source code chunking
- Added deterministic chunk identifiers
- Added local embedding generation
- Integrated persistent ChromaDB vector storage
- Added project-level re-indexing
- Added repository indexing endpoint
- Added metadata-aware code chunk storage
- Added unit tests for embedding

## Day 9 Progress

- Semantic Retrieval
- Vector Search
- Query Embedding
- Chroma Similarity Search
- Project Filtering
- Search API
- Test for chunking_service and indexing_service

## Day 10 Progress

- Implemented Retrieval-Augmented Generation (RAG)
- Added AI-powered codebase question answering
- Connected semantic retrieval with Gemini
- Added grounded repository context
- Added source references for generated answers
- Added codebase chat API
- Added RAG unit tests

## 🎯 Roadmap

- [x] FastAPI backend
- [x] File upload system
- [x] AST parser
- [x] Gemini integration
- [x] Documentation engine
- [x] Repository scanner
- [x] End-to-end documentation pipeline
- [x] ChromaDB + Embeddings
- [x] Semantic Search + RAG
- [x] Chat with Codebase
- [ ] Database
- [ ] React frontend
- [ ] Testing + Security
- [ ] Docker + CI/CD
- [ ] Deployment

---

## 📄 License

This project is licensed under the MIT License.
