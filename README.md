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

---

## 🎯 Roadmap

- [x] Project setup
- [x] FastAPI backend
- [x] File upload system
- [x] AST parser
- [x] AI documentation generation
- [ ] README generation
- [ ] Semantic search with RAG
- [ ] ChromaDB integration
- [ ] Authentication
- [ ] React frontend
- [ ] Deployment

---

## 📄 License

This project is licensed under the MIT License.
