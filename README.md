# 🤖 Multi-Agent AI Business Assistant

An enterprise-grade Multi-Agent AI Business Assistant powered by FastAPI, Streamlit, LangChain, ChromaDB, and Google Gemini.

The system intelligently routes user queries to specialized AI agents such as Finance, HR, Sales, Marketing, Research, Analytics, Reports, Documents, and General Assistant.

---

# 🚀 Features

- Multi-Agent AI Architecture
- Intelligent Query Routing
- Retrieval-Augmented Generation (RAG)
- Enterprise Knowledge Base
- Finance Analytics
- HR Assistant
- Sales Assistant
- Marketing Assistant
- Research Agent
- Business Analytics
- Executive Report Generation
- User Authentication
- Permission Management
- Modern Enterprise Dashboard
- REST API
- Streamlit Frontend

---

# 🏗️ Project Architecture

```
Multi-Agent-AI-Business-Assistant
│
├── backend
│   ├── app
│   │   ├── agents
│   │   ├── api
│   │   ├── core
│   │   ├── database
│   │   ├── memory
│   │   ├── orchestrator
│   │   ├── prompts
│   │   ├── rag
│   │   ├── repositories
│   │   ├── schemas
│   │   ├── services
│   │   └── tools
│   │
│   ├── data
│   ├── reports
│   ├── requirements.txt
│   └── main.py
│
├── frontend
│   ├── agents
│   ├── dashboard
│   ├── views
│   ├── components
│   ├── assets
│   ├── auth.py
│   └── main.py
│
├── docs
├── reports
├── tests
├── assets
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# 🧠 AI Agents

| Agent | Description |
|--------|-------------|
| Finance | Revenue, Profit, Expenses |
| HR | Leave Policies, Benefits |
| Sales | Sales Insights |
| Marketing | Marketing Analytics |
| Research | Knowledge Research |
| Analytics | Business Analytics |
| Report | Executive Business Reports |
| Document | RAG Document Search |
| General | General Purpose Assistant |

---

# 🛠 Tech Stack

### Backend

- FastAPI
- Python 3.11
- SQLAlchemy
- SQLite
- LangChain
- ChromaDB
- Google Gemini API

### Frontend

- Streamlit
- Custom CSS
- REST API

### AI

- Gemini 2.5 Flash
- LangChain
- ChromaDB
- Sentence Transformers

---

# 📂 RAG Pipeline

```
PDF Upload
      │
      ▼
Text Extraction
      │
      ▼
Chunking
      │
      ▼
Embeddings
      │
      ▼
Chroma Vector DB
      │
      ▼
Retriever
      │
      ▼
LLM
      │
      ▼
Answer
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/sundar66kalyan/Multi-Agent-AI-Business-Assistant.git

cd Multi-Agent-AI-Business-Assistant
```

---

## Backend

```bash
cd backend

pip install -r requirements.txt

python init_db.py

python seed_finance.py

uvicorn main:app --reload
```

Runs on

```
http://localhost:8000
```

---

## Frontend

```bash
cd frontend

pip install -r requirements.txt

streamlit run main.py
```

Runs on

```
http://localhost:8501
```

---

# API Documentation

```
http://localhost:8000/docs
```

---

# Supported Queries

```
Revenue this month

Show finance summary

Generate employee report

Business analytics

What is the leave policy?

Tell me a joke

Who is Sundar Pichai?
```

---

# Screenshots

Add screenshots here.

```
assets/screenshots/dashboard.png

assets/screenshots/chat.png

assets/screenshots/report.png
```

---

# Future Improvements

- Docker Deployment
- PostgreSQL Support
- Redis Memory
- JWT Authentication
- User Management
- Role Based Access Control
- Multi-LLM Support
- Voice Assistant

---

# License

MIT License

---

# Author

**Kalyana Sundar**

AI Engineer

GitHub

https://github.com/sundar66kalyan

LinkedIn
www.linkedin.com/in/kalyana-sundar-912403285