#  SHOPKART – E-commerce REST API

SHOPKART is a full-featured **E-commerce REST API** built with **Django REST Framework (DRF)**.
The project follows **real-world backend best practices** and implements complete e-commerce workflows including authentication, product management, cart handling, orders, reviews, and image support.



---

##  Features

* User authentication & authorization (JWT)
* Product & category management
* Cart management (one cart per user)
* Order placement & order history
* Product reviews & ratings
* Image handling for products
* API documentation with Swagger & ReDoc

---

##  Technologies Used

* **Django** – Backend framework
* **Django REST Framework (DRF)** – API development
* **Djoser** – Authentication system
* **Simple JWT** – JWT-based authentication
* **drf-yasg** – API documentation (Swagger)
* **PostgreSQL / SQLite** – Database

---

## Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/shopkart.git
cd shopkart
```

### 2️⃣ Create & activate virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations

```bash
python manage.py migrate
```

### 5️⃣ Create superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the development server

```bash
python manage.py runserver
```

---

##  API Documentation

Swagger UI:

```
http://127.0.0.1:8000/swagger/
```

ReDoc:

```
http://127.0.0.1:8000/redoc/
```

---

## Environment Variables

Create a `.env` file in the root directory and add:

```env
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url
ALLOWED_HOSTS=*
EMAIL_HOST=your_email_host
```

---

##  Project Purpose

This project is built to:

* Practice **real-world e-commerce backend architecture**
* Demonstrate **REST API design & authentication**
* Showcase skills for **junior backend / full-stack developer roles**

---

## 👨‍💻 Author

**Jahid Alam**
Backend / Full Stack Developer

---

 If you like this project, don’t forget to give it a star on GitHub!
