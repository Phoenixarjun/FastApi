# 🚀 FastAPI Blog API – Practice Project

This is a **practice project** built to get familiar with **FastAPI**, one of the fastest and most modern web frameworks for Python. The project includes **CRUD operations for blogs**, **user authentication**, and a fully interactive **Swagger UI** for exploring the API.
![image](https://github.com/user-attachments/assets/03f87723-325f-4c30-b81c-76a06f75aabb)

---

## 📚 About the Project

This project was created to **learn and explore** FastAPI fundamentals. It covers:

* Creating API endpoints with path and query parameters
* Structuring models and schemas with **Pydantic**
* Connecting and interacting with a database
* Implementing **JWT-based authentication**
* Organizing routes using API routers
* Serving API documentation with Swagger UI

---

## 🛠️ Tech Stack

* **FastAPI** – the core web framework
* **Pydantic** – for data validation and type hints
* **SQLAlchemy** – ORM for database access
* **Passlib (bcrypt)** – for password hashing
* **Python-Jose** – to create and verify JWT tokens
* **Uvicorn** – ASGI server for running the app

---

## 🚦 Getting Started

### 🔧 Installation

```bash
git clone https://github.com/Phoenixarjun/FastApi
cd FastApi
pip install -r requirements.txt
```

### ▶️ Running the Server

```bash
uvicorn main:app --reload
```

Once running, navigate to:

👉 [http://127.0.0.1:8000/docs#/Blogs](http://127.0.0.1:8000/docs) for the Swagger UI.

---

## 🔐 Authentication

The app uses **JWT** for securing routes. Obtain a token via the login endpoint and include it in the Authorization header (`Bearer <token>`) for protected routes.

---

## 💡 Why This Project?

I built this project to:

* Explore FastAPI hands-on
* Practice building modern, scalable APIs
* Understand how FastAPI handles dependency injection, routing, and security

---

## 📎 License

This project is open source and free to use under the [MIT License](LICENSE).


