# User API - Django REST Framework

A simple and clean REST API for user management, built using Django and Django REST Framework. This project allows creation, retrieval, updating, and deletion of user records through secure and scalable API endpoints.

## 🚀 Features

- User Listing
- User Detail View
- Update User
- Delete User
- RESTful API architecture
- Modular Django app structure

## 📂 Project Structure

```
userAPI/
├── manage.py
├── userAPI/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── users/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

## ⚙️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/Yuvaraj0609/userAPI.git
cd userAPI
```

2. **Create and activate a virtual environment**

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. **Apply migrations**

```bash
python manage.py migrate
```

4. **Run the development server**

```bash
python manage.py runserver
```

5. **Access the API**

Visit http://127.0.0.1:8000/ in your browser or use an API tool like Postman.

## 🔗 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/users/` | GET | List all users |
| `/api/users/` | POST | Create a new user |
| `/api/users/<id>/` | GET | Retrieve a specific user |
| `/api/users/<id>/` | PUT | Update a user |
| `/api/users/<id>/` | DELETE | Delete a user |

## ✅ Example JSON (POST Request)

```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "first_name": "John",
  "last_name": "Doe"
}
```

## 📌 Requirements

- Python 3.8+
- Django 3.2+ or 4.x
- Django REST Framework

## 🙋 Author

Yuvaraj – [GitHub](https://github.com/Yuvaraj0609)

## 🤝 Contributing

Contributions, issues and feature requests are welcome. Feel free to check the issues page if you want to contribute.

## 📄 API Documentation

For detailed API documentation, run the server and visit `/api/docs/` (if DRF documentation features are enabled).

## 📧 Contact

For any inquiries or issues, please open an issue on GitHub or contact the project maintainer.
