# meeting_app
Here's a complete `README.md` for a **Meeting Application** with **User Authentication** using Django REST Framework and JWT. This version is professional, clean, and suitable for documentation, GitHub projects, or internal presentations.

---

# 📅 Meeting App Backend – Django REST Framework

A RESTful backend for a Meeting Scheduler Application built with **Django**, **Django REST Framework**, and **JWT Authentication**. This application supports full **User Authentication (Signup/Login/Logout)**, **Token Logging**, and **User Activity Logs**.

---

## 🚀 Features

* ✅ User Signup with JWT Token generation
* ✅ Secure Login with authentication logs
* ✅ JWT-based authentication (access/refresh tokens)
* ✅ Token history tracking (`TokenLog`)
* ✅ Activity/event logging (`Log`)
* ✅ Admin-restricted user list API
* 🔐 Protected endpoints with role-based access
* 📦 Easily extensible for meeting creation, invitation, calendar integration

---

## 🛠️ Tech Stack

* Python 3.10+
* Django 4.x
* Django REST Framework
* Simple JWT (`djangorestframework-simplejwt`)
* SQLite (default, can be replaced with PostgreSQL)
* DRF permissions, generics

---

## 🧩 Project Structure

```
meeting_app/
│
├── meeting_app/         # Main Django project settings
├── api/                 # All core API logic
│   ├── models.py        # User, TokenLog, Log
│   ├── serializers.py   # User, Signup, Logs
│   ├── views.py         # Signup, Login, List Users
│   ├── urls.py          # API endpoint routing
│
├── manage.py
└── requirements.txt
```

---

## 🔐 User Authentication Flow

### 🔸 Signup

`POST /api/auth/signup/`

**Payload:**

```json
{
  "username": "john",
  "email": "john@example.com",
  "password": "password123"
}
```

**Response:**

```json
{
  "access": "jwt-access-token",
  "refresh": "jwt-refresh-token"
}
```

### 🔸 Login

`POST /api/auth/login/`

**Payload:**

```json
{
  "username": "john",
  "password": "password123"
}
```

**Response:**

```json
{
  "access": "jwt-access-token",
  "refresh": "jwt-refresh-token",
  "username": "john"
}
```

### 🔸 Get All Users (Admin Only)

`GET /api/auth/users/`

**Header:**

```
Authorization: Bearer <access_token>
```

---

## 📦 Models Overview

### ✅ `User` (Custom User Model)

* `username`, `email`, `bio`, `password`
* Created using `get_user_model()`

### ✅ `TokenLog`

* Stores access & refresh tokens for each login/signup
* Fields: `user`, `access_token`, `refresh_token`, `timestamp`

### ✅ `Log`

* Logs signup, login, and other user actions
* Fields: `user`, `event`, `description`, `timestamp`

---

## 🧪 Running the Project

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/meeting-app-backend.git
cd meeting-app-backend
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run migrations:**

```bash
python manage.py migrate
```

4. **Start server:**

```bash
python manage.py runserver
```

---

## 🔒 JWT Authentication Notes

* Add JWT token to **Authorization header** in protected routes:

  ```
  Authorization: Bearer <access_token>
  ```

* Token refresh endpoint (optional):

  ```
  POST /api/token/refresh/
  {
    "refresh": "<your_refresh_token>"
  }
  ```

---

## ✅ Sample Test Users

You can create test users via the `/signup/` endpoint or via Django admin:

```bash
python manage.py createsuperuser
```

---

## 🌐 Future Enhancements

* 🗓️ Meeting creation and invitation APIs
* 🔔 Email reminders or push notifications
* 🧑‍🤝‍🧑 Meeting participants and roles
* 📅 Calendar integrations (Google, Outlook)
* 📈 Dashboard for admins

---

## 👨‍💻 Author

**Mustakim Shaikh**
📧 [mustakim.shaikh.prof@gmail.com](mailto:mustakim.shaikh.prof@gmail.com)
📍 Bhusawal, Maharashtra

---

## 📄 License

MIT License. Use freely for educational and commercial purposes.

---

Would you like me to generate a visual project architecture diagram or a Postman collection for testing this API?
