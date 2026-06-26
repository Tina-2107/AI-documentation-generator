🤖 AI Documentation Generator
An AI-powered documentation generator that automatically analyzes source code and generates high-quality technical documentation using FastAPI, Python AST, and Large Language Models (LLMs).

🚀 Features
* Upload source code files
* Analyze Python code using AST
* Generate documentation with AI
* Generate README files
* Explain functions and classes
* Semantic code search (coming soon)
* Repository analysis (coming soon)

🛠️ Tech Stack

### Backend

* Python
* FastAPI

### AI

* OpenAI API (planned)
* Python AST
* ChromaDB (planned)

### Frontend

* React (planned)

## 📂 Project Structure

```
ai-documentation-generator/
│
├── app/
│   ├── main.py
│   ├── routes/
│   ├── services/
│   ├── models/
│   ├── utils/
│   └── config.py
│
├── uploads/
├── tests/
├── docs/
├── requirements.txt
└── README.md
```

---

## ▶️ Installation

Clone the repository

```bash
git clone <repository-url>
cd ai-documentation-generator
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the server

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

* Project initialized
* FastAPI backend created
* Basic API endpoints
* GitHub repository created
* Project structure established

---

## 📌 Upcoming Features

* AST parser
* AI documentation generation
* README generation
* RAG
* Vector database
* Authentication
* React frontend
* Deployment

---

## 👩‍💻 Author

Built by Tina as part of an AI Engineering learning journey.
