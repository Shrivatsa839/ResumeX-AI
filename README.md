# 🚀 ResumeX AI

> AI-powered Resume Analyzer & ATS Score Checker built with FastAPI, React, and Artificial Intelligence.

---

## 📌 About

ResumeX AI is an intelligent resume analysis platform that helps job seekers optimize their resumes for Applicant Tracking Systems (ATS) while providing AI-driven feedback and insights.

The project follows a production-ready backend architecture using FastAPI, SQLAlchemy, Alembic, and secure authentication practices.

---

## ✨ Current Progress

### ✅ Backend Foundation Completed

- FastAPI Backend
- REST API Architecture
- Project Modular Structure
- Environment Configuration (.env)
- SQLAlchemy ORM
- SQLite Database
- Alembic Database Migrations
- Password Hashing (bcrypt)
- Swagger API Documentation
- Health Check API

---

## 🚧 Upcoming Features

- User Registration
- JWT Authentication
- Login System
- Resume Upload (PDF/DOCX)
- Resume Parsing
- ATS Score Calculation
- AI Resume Analysis
- Resume Improvement Suggestions
- Dashboard
- PostgreSQL Support
- Docker Deployment

---

# 🏗️ Backend Architecture

```
backend/
│
├── app/
│   ├── api/
│   │   └── v1/
│   │
│   ├── core/
│   │
│   ├── db/
│   │
│   ├── models/
│   │
│   ├── schemas/
│   │
│   ├── repositories/
│   │
│   ├── services/
│   │
│   ├── middleware/
│   │
│   └── main.py
│
├── requirements/
├── alembic.ini
└── .env
```

---

# ⚙️ Tech Stack

### Backend

- Python 3.13
- FastAPI
- SQLAlchemy
- Alembic
- SQLite
- Pydantic
- Uvicorn
- Passlib
- bcrypt

### Frontend *(In Progress)*

- React
- Vite
- Tailwind CSS

---

# 📖 API Documentation

After running the server:

```
http://127.0.0.1:8000/docs
```

OpenAPI Schema:

```
http://127.0.0.1:8000/openapi.json
```

---

# 🚀 Running the Project

Clone the repository

```bash
git clone https://github.com/Shrivatsa839/ResumeX-AI.git
```

Go to backend

```bash
cd ResumeX-AI/backend
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements/requirements.txt
```

Run the backend

```bash
uvicorn app.main:app --reload
```

---

# 📊 Development Roadmap

- [x] FastAPI Setup
- [x] Project Architecture
- [x] SQLAlchemy Setup
- [x] Alembic Migrations
- [x] User Model
- [x] Password Hashing
- [ ] User Registration
- [ ] JWT Authentication
- [ ] Login API
- [ ] Resume Upload
- [ ] Resume Parsing
- [ ] ATS Score Engine
- [ ] AI Resume Analysis
- [ ] Dashboard
- [ ] Docker Deployment

---

# 👨‍💻 Author

**Shrivatsa Khandare**

- GitHub: https://github.com/Shrivatsa839
- LinkedIn: https://linkedin.com/in/shrivatsa-khandare-ba4520369

---

⭐ If you like this project, consider giving it a star.
