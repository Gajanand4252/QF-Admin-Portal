# QF-Admin-Portal

# Admin Dashboard Backend (Flask + MySQL)

## Overview
Flask backend built to support a pre-existing Admin Dashboard UI without modifying the frontend.  
Handles authentication and opportunity management with MySQL storage.

---

## Features
- Signup and login (session-based)
- Forgot password (mock)
- Logout
- Create, view, update, delete opportunities

---

## Tech Stack
Flask  
MySQL  
SQLAlchemy  

---

## Setup

### 1. Clone
```bash
git clone https://github.com/Gajanand4252/QF-Admin-Portal.git
QF-Admin-Portal
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment
Create `.env` file:
```
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_NAME=certifyme
SECRET_KEY=secret
```

### 4. Create database
```sql
CREATE DATABASE certifyme;
```

### 5. Run
```bash
python app.py
```

Open:
http://127.0.0.1:5000

---

## API

POST /signup  
POST /login  
POST /forgot-password  
POST /logout  

GET /opportunity  
POST /opportunity  
GET /opportunity/<id>  
PUT /opportunity/<id>  
DELETE /opportunity/<id>  

---

## Notes
Frontend UI was not modified.
UI integrated
Ready for submission
