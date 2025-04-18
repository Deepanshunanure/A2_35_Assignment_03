﻿# A2_35_Assignment_03
# 🧩 Assignment 3: Building Web Applications with Flask, Django, and Docker Compose

## 📌 Objective

This project demonstrates how to build and containerize simple web applications using **Flask** and **Django**, and manage them together using **Docker Compose**.

---

## 🗂️ Project Structure

assignment3/ │ ├── flask-app/ # Flask application │ ├── app.py # Flask routes and logic │ ├── templates/ # HTML templates using Bootstrap │ └── Dockerfile # Flask Dockerfile │ ├── mydjango/ # Django project │ ├── manage.py │ ├── mydjango/ # Django settings │ ├── myapp/ # A simple app for item listing │ └── Dockerfile # Django Dockerfile │ └── docker-compose.yml # Docker Compose file to run both apps

yaml
Copy
Edit

---

## 🌐 Flask Application

### 🔧 Features

- Home page: `Hello, World!` message
- Greeting form that takes name and age
- Error handling for invalid or missing inputs
- Styled using Bootstrap for a clean UI

### 🔗 Routes

- `/` – Home page
- `/greet` – Input form and greeting page

---

## 🛠️ Django Application

### 🔧 Features

- Homepage displays a list of items stored in the database
- Admin panel to add/edit/delete items
- A form to add new items from the homepage

### 🔗 URLs

- `/admin` – Django admin panel
- `/` – Item listing and creation form

---

## 🐳 Docker Setup

### 📄 `docker-compose.yml`

Both Flask and Django apps are containerized and run on separate ports:

| Service | URL                     | Port  |
|---------|--------------------------|--------|
| Flask   | http://localhost:5000    | 5000   |
| Django  | http://localhost:8000    | 8000   |

---

## 🚀 How to Run the Project

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/assignment3.git
cd assignment3
2. Build and Start Containers
bash
Copy
Edit
docker-compose up --build
3. Access the Apps
Flask App: http://localhost:5000

Django App: http://localhost:8000

📦 Docker Hub
Images are pushed to Docker Hub:

🐍 Flask: deepanshu1nanure/flask-app

🧱 Django: deepanshu1nanure/django-app

📚 Tech Stack
Python 3

Flask

Django

HTML/CSS (Bootstrap)

Docker

Docker Compose
