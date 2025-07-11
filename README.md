# 🏡 Real Estate Platform

A full-stack rental and sales platform for managing and listing:

- 🏠 Houses
- 🏢 Apartments
- 📍 Land Plots
- 🚗 Cars

Built with a modern tech stack using **React (frontend)** and **FastAPI (backend)**.

---

## 📁 Project Structure


---

## ⚙️ Tech Stack

| Layer      | Tech            |
|------------|-----------------|
| Frontend   | React, CSS/HTML |
| Backend    | FastAPI (Python)|
| Database   | SQLite / PostgreSQL (optional) |
| API Format | RESTful         |
| Image Handling | File Uploads (via FastAPI) |

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Node.js & npm
- Python 3.8+
- pip or poetry
- Git

---

### 🖥️ Run the Frontend (React)

```bash
cd real_estate_frontend
npm install
npm start

cd real_estate_backend
pip install -r requirements.txt
uvicorn main:app --reload
# BACKEND (.env)
DATABASE_URL=sqlite:///./realestate.db
SECRET_KEY=your_secret_key

# FRONTEND (.env)
REACT_APP_API_BASE_URL=http://127.0.0.1:8000
👤 Author
MANZI Fred


