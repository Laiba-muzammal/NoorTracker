# 🕌 NoorTracker
Track your Salah. Align your Qibla. Fix your posture.
An intelligent, backend-driven prayer tracking system for Muslims — built with FastAPI, designed for real-world faith discipline.

---

## ⚠️ Project Status
🛠️ This is a private, personal project currently under development.
This project reflects my experimental ideas,and I actively shape it further during creative bursts and breaks.
It's not production-ready yet — but it’s growing into something meaningful over time.

📌 Expect future improvements, better UI, and added features — whenever inspiration strikes!

---

## ✨ Features

🔐 JWT-based Authentication (Register/Login)

🧎 Salah Logging (Name, Status, Timestamp)

📈 Prayer History (Daily/Weekly)

🕋 Qibla Direction Detection (Mock or real, pluggable)

🧍 Posture Accuracy Module (MediaPipe-powered)

📊 Analytics Dashboard (Coming Soon)

---

## 📌 Why NoorTracker?

Faith deserves infrastructure.
NoorTracker isn’t just another backend app — it’s a tool to help Muslims digitally track, correct, and stay consistent in their salah — securely and privately.

---

## 🧠 Tech Stack
Tech	Purpose
FastAPI	Backend API framework
SQLAlchemy	ORM for DB interaction
SQLite	Lightweight DB (swap-ready)
Pydantic	Schema validation
Passlib	Password hashing (bcrypt)
Python-Jose	JWT encoding/decoding
MediaPipe (planned)	Posture detection

---

#🗂️ Project Structure
```
app/
├── routes/
│   ├── auth.py          # Register/Login
│   ├── salah.py         # Salah log/history
│   ├── qibla.py         # Qibla direction
│   └── posture.py       # Posture tracking
├── models.py            # SQLAlchemy models
├── schemas.py           # Pydantic schemas
├── database.py          # DB connection
├── config.py            # JWT & env configs
├── utils/
│   ├── hashing.py       # Password hashing utils
│   └── oauth2.py        # JWT validation
|   └── token.py 
main.py                  # FastAPI app init
.env                     # Environment variables
requirements.txt         # Dependencies
README.md                # You're here.
```

---
## 🚀 Getting Started

### 1. Clone the repo
```
git clone https://github.com/your-username/noortracker.git
cd noortracker
```

### 2. Set up virtual environment
```
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Create .env file
```
JWT_SECRET_KEY=your-secret-key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Run the server
```
uvicorn main:app --reload
```

### 6. Open API docs
```
Visit http://127.0.0.1:8000/docs
```

---

## 🔒 Auth Flow
POST /auth/register → Create account

POST /auth/login → Get JWT token

Use token as Authorization: Bearer <token> in headers to access:

/salah → Log prayer

/salah/history → View logged prayers

/qibla/direction → Get Qibla direction

/posture/track (planned) → Log posture accuracy

---

📄 License
This project is licensed under the MIT License. See LICENSE for more details.
