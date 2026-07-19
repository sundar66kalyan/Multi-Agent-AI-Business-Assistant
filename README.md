# 🤖 Multi-Agent AI Business Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![LangChain](https://img.shields.io/badge/LangChain-AI-orange)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-red)
![Gemini](https://img.shields.io/badge/LLM-Google%20Gemini-blueviolet)
![License](https://img.shields.io/badge/License-MIT-green)

### 🚀 Enterprise AI Business Assistant Powered by Multiple AI Agents

Developed by **Kalyana Sundar**  
**AI Engineer | Machine Learning Engineer | Data Scientist**

</div>

---

# 📌 Project Overview

The **Multi-Agent AI Business Assistant** is an enterprise-grade AI platform that combines multiple specialized AI agents into a single intelligent business system.

Instead of relying on one AI model for every task, the system intelligently routes each request to the most suitable AI agent.

The application integrates:

- Business Analytics
- Financial Analysis
- Retrieval-Augmented Generation (RAG)
- Enterprise Reporting
- Business Memory
- Knowledge Base Management
- JWT Authentication
- REST APIs
- Google Gemini AI

---

# 🎯 Business Objective

The application helps organizations to:

- Analyze business performance
- Query company documents
- Generate AI-powered reports
- Maintain organizational knowledge
- Retrieve business insights
- Automate financial analysis
- Centralize AI-driven decision making

---

# 🏗 System Architecture

```

                   User
                     │
                     ▼
            FastAPI REST API
                     │
                     ▼
           Gemini AI Router
                     │
         ┌───────────┼───────────┐
         │           │           │
         ▼           ▼           ▼
   Finance      Analytics    Document(RAG)
      │              │             │
      ▼              ▼             ▼
 SQLite DB      Dashboard     ChromaDB
                                     │
                                     ▼
                             PDF Knowledge Base

         ┌───────────────────────────────┐
         │        Report Agent           │
         │  PDF | DOCX | Excel Reports   │
         └───────────────────────────────┘

                     │
                     ▼
               Memory Service

```

---

# 🧠 AI Agents

## 📊 Finance Agent

Responsible for:

- Revenue Analysis
- Expense Analysis
- Profit Calculation
- Business Financial Summary
- KPI Analysis

---

## 📈 Analytics Agent

Provides:

- Business Analytics
- Dashboard Metrics
- Document Statistics
- Finance Statistics
- System Monitoring

---

## 📄 Document Agent

Powered by:

- LangChain
- ChromaDB
- HuggingFace Embeddings

Capabilities:

- PDF Question Answering
- Document Summarization
- Semantic Search
- Business Knowledge Retrieval

---

## 📑 Report Agent

Generates:

- Executive Reports
- PDF Reports
- DOCX Reports
- Excel Reports
- Business Recommendations

---

## 🧠 Memory Agent

Maintains:

- Conversation History
- User Queries
- Agent Responses
- Session Memory

---

# ⚙ Features

## ✅ Authentication

- User Registration
- User Login
- JWT Authentication
- Protected APIs

---

## 📂 Document Management

- Upload PDF
- Delete Documents
- Knowledge Base
- Duplicate Detection
- Metadata Management

---

## 🔍 RAG Pipeline

- PDF Loader
- Text Chunking
- Embedding Generation
- ChromaDB Vector Storage
- Semantic Retrieval
- Context-based Answering

---

## 📊 Dashboard

Provides:

- Revenue
- Expenses
- Profit
- Registered Agents
- Documents Indexed
- Chunks Indexed
- Business Health
- System Status

---

## 📈 Analytics

- AI Analytics
- Dashboard Summary
- Usage Statistics
- Business Metrics

---

## 📑 Report Generation

Export Reports as:

- PDF
- DOCX
- Excel

---

## 🧠 Memory

- Store Conversations
- Retrieve History
- Clear Memory

---

## 🤖 Gemini AI

Integrated with:

- Google Gemini
- Intelligent Agent Routing
- AI Report Generation
- Business Recommendations

---

# 🛠 Technology Stack

## Backend

- Python 3.11
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn

---

## AI

- Google Gemini
- LangChain
- HuggingFace Embeddings

---

## Database

- SQLite
- ChromaDB

---

## Authentication

- JWT
- Passlib
- bcrypt

---

## Reports

- ReportLab
- python-docx
- OpenPyXL

---

## Deployment

- Cloudflare Tunnel
- Swagger UI
- GitHub

---

# 📁 Project Structure

```

backend/

│

├── app/

│ ├── agents/

│ ├── api/

│ ├── database/

│ ├── memory/

│ ├── models/

│ ├── orchestrator/

│ ├── rag/

│ ├── repositories/

│ ├── services/

│ ├── tools/

│ └── utils/

│

├── data/

├── reports/

├── requirements.txt

├── Procfile

└── main.py

```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Multi-Agent-AI-Business-Assistant.git

cd Multi-Agent-AI-Business-Assistant
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r backend/requirements.txt
```

---

## Configure Environment

Create

```
backend/.env
```

Example

```env
GOOGLE_API_KEY=YOUR_API_KEY

SECRET_KEY=YOUR_SECRET_KEY

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

DATABASE_URL=sqlite:///business_assistant.db
```

---

## Run Server

```bash
cd backend

python -m uvicorn main:app --reload
```

Server

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# 📚 API Endpoints

## Authentication

- POST /register
- POST /login

---

## Chat

- POST /chat

---

## Upload

- POST /upload-pdf

---

## Knowledge Base

- GET /knowledge-base
- DELETE /delete-document

---

## Dashboard

- GET /dashboard/summary
- GET /dashboard/metrics
- GET /dashboard/agents
- GET /dashboard/health

---

## Reports

- GET /report/pdf
- GET /report/docx
- GET /report/excel

---

## Memory

- GET /memory
- DELETE /memory

---

# 💡 Example Prompt

```
Analyze business performance.
```

```
Summarize the uploaded document.
```

```
Generate executive report.
```

```
Show finance summary.
```

---

# 📸 Screenshots

Add screenshots here:

- Home
- Swagger UI
- Dashboard
- Chat API
- Upload PDF
- Knowledge Base
- Memory
- Reports

---

# 🔮 Future Enhancements

- Multi-User Support
- PostgreSQL
- Docker Deployment
- Kubernetes
- Redis Cache
- Email Agent
- Calendar Agent
- Voice Assistant
- MCP Integration
- Multi-LLM Support

---

# 👨‍💻 Developer

## Kalyana Sundar

**AI Engineer | Machine Learning Engineer | Data Scientist**

### Skills

- Artificial Intelligence
- Machine Learning
- Deep Learning
- NLP
- Computer Vision
- LLM Applications
- Multi-Agent Systems
- FastAPI
- LangChain
- ChromaDB
- SQLAlchemy

GitHub:

```
https://github.com/sundar66kalyan
```

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the MIT License.