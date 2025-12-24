# SQL to SQLAlchemy – 125 Queries

This repository contains **125 classic SQL queries rewritten using SQLAlchemy ORM and Alembic**.  
The project was created as a **learning-focused deep dive into ORMs**, translating raw SQL logic into Pythonic ORM-based implementations.

It is based on a real **DBMS semester assignment**, reimplemented to understand how relational database concepts map to SQLAlchemy ORM.

---

## 🎯 Purpose of This Project

- Understand **how raw SQL translates to ORM queries**
- Practice **SQLAlchemy ORM models, relationships, and querying**
- Learn **Alembic migrations** in a real, incremental way
- Build strong intuition for **ORM-based database design**
- Create a **public learning reference** for others studying SQLAlchemy

---

## 🧠 What This Project Covers

- SELECT queries
- WHERE conditions
- JOINs
- GROUP BY and HAVING
- Subqueries
- Ordering and filtering
- Multi-table relationships
- Schema evolution using Alembic
- ORM equivalents of classic SQL problems

Each query is implemented with **clear intent**, often mirroring how the SQL solution would be written.

---

## 🛠️ Tech Stack

- **Python**
- **SQLAlchemy (ORM)**
- **Alembic (Migrations)**
- **SQLite**

---



## 🔁 Alembic Migrations

Each Alembic revision corresponds to **specific SQL questions or schema changes**.  
Migration filenames reflect the **question number**, making it easy to trace learning progress.

Example:
278ea1889eb1_sql_95th_question.py



This approach helped reinforce:
- Schema evolution
- Controlled database changes
- Real-world migration workflows

---

## 🚀 How to Run This Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2️⃣ Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Explore queries

- Run scripts inside sem3sqlalchemy/

- Inspect ORM queries in querying_db.py

- Review Alembic migrations in test_alembic/versions/


### 📘 Learning Notes

- This project prioritizes clarity over optimization

- Multiple approaches may exist for the same query

- Some solutions evolved over time (refined versions included)

- Database file is intentionally included for reproducibility

