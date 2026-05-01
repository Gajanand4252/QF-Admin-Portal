# QF-Admin-Portal

Admin Dashboard Backend (Flask + MySQL)

Project Overview
This project is a Flask backend built to support a pre-existing Admin Dashboard UI.
The main requirement was to implement backend functionality without changing the frontend.

The system handles authentication and opportunity management with data stored in MySQL.

---

Features

Authentication

* Signup
* Login using session
* Forgot password (mock)
* Logout

Opportunity Management

* Create opportunity
* Get all opportunities
* Get single opportunity
* Update opportunity
* Delete opportunity

Database

* MySQL database
* SQLAlchemy ORM

---

Tech Stack
Backend: Flask (Python)
Database: MySQL
ORM: SQLAlchemy
Frontend: Provided UI (unchanged)

---

Project Structure

project/

app.py
models.py
config.py
.env

static/
admin.css
admin.js

templates/
admin.html

---

Setup Instructions

1. Clone repository
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. Create virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install flask flask_sqlalchemy pymysql python-dotenv

4. Create .env file

DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_NAME=certifyme
SECRET_KEY=secret

5. Create MySQL database
   CREATE DATABASE certifyme;

6. Run project
   python app.py

Open in browser
http://127.0.0.1:5000

---

API Endpoints

Authentication
POST /signup
POST /login
POST /forgot-password
POST /logout

Opportunities
GET /opportunity
POST /opportunity
GET /opportunity/<id>
PUT /opportunity/<id>
DELETE /opportunity/<id>

---

Important Notes
Frontend UI was not modified
Session-based authentication used for compatibility
Backend integrates directly with existing JavaScript

---

Final Status
Backend completed
Database connected
UI integrated
Ready for submission
