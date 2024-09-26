
# Customer Orders Management API

## Overview

This project is a simple REST API built using Django and PostgreSQL that allows users to manage customer data and orders. It includes authentication via OpenID Connect and provides SMS notifications for new orders using the Africa's Talking SMS gateway.

### Features
- RESTful API for managing customers and orders
- User authentication and authorization using OpenID Connect
- SMS notifications for new orders
- Automated testing and Continuous Integration/Continuous Deployment (CI/CD) pipeline
- Deployed on [Heroku](https://www.heroku.com/)

## Table of Contents
1. [Technologies Used](#technologies-used)
2. [Getting Started](#getting-started)
3. [Project Structure](#project-structure)
4. [API Endpoints](#api-endpoints)
5. [Authentication](#authentication)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Contributing](#contributing)
9. [References](#references)

## Technologies Used

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design. [Learn more](https://www.djangoproject.com/)
- **Django REST Framework**: A powerful toolkit for building Web APIs in Django. [Learn more](https://www.django-rest-framework.org/)
- **PostgreSQL**: An open-source relational database system. [Learn more](https://www.postgresql.org/)
- **Gunicorn**: A Python WSGI HTTP Server for UNIX. [Learn more](https://gunicorn.org/)
- **Whitenoise**: A Django middleware for serving static files. [Learn more](http://whitenoise.evans.io/en/stable/)
- **Heroku**: A cloud platform as a service (PaaS) supporting several programming languages. [Learn more](https://www.heroku.com/)

## Getting Started

### Prerequisites
To run this project locally, you will need:
- Python 3.9 or higher
- PostgreSQL installed locally
- pip (Python package installer)

### Clone the Repository
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### Create a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Up PostgreSQL
1. Open the PostgreSQL command line interface:
   ```bash
   sudo -u postgres psql
   ```

2. Create a database and user:
   ```sql
   CREATE DATABASE mydatabase;
   CREATE USER myuser WITH PASSWORD 'mypassword';
   GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
   ```

3. Update your Django settings in `settings.py` to connect to PostgreSQL:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'mydatabase',
           'USER': 'myuser',
           'PASSWORD': 'mypassword',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

### Run Migrations
```bash
python manage.py migrate
```

### Run the Development Server
```bash
python manage.py runserver
```

The application should now be running at `http://127.0.0.1:8000/`.

## Project Structure

```
your-repo-name/
│
├── your_project_name/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── your_app_name/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── requirements.txt
├── Procfile
└── README.md
```

## API Endpoints

### Customers
- **Create a Customer**
  - **POST** `/api/customers/`
  
- **Retrieve a Customer**
  - **GET** `/api/customers/{id}/`
  
- **Update a Customer**
  - **PUT** `/api/customers/{id}/`
  
- **Delete a Customer**
  - **DELETE** `/api/customers/{id}/`

### Orders
- **Create an Order**
  - **POST** `/api/orders/`
  
- **Retrieve an Order**
  - **GET** `/api/orders/{id}/`
  
- **Update an Order**
  - **PUT** `/api/orders/{id}/`
  
- **Delete an Order**
  - **DELETE** `/api/orders/{id}/`

## Authentication

The API uses OpenID Connect for authentication. When making requests to protected endpoints, include the authentication token in the `Authorization` header:

```
Authorization: Bearer your_access_token
```

To obtain a token, you need to authenticate through your OpenID provider and retrieve the token.

## Testing

To run the tests for the API, use the following command:
```bash
python manage.py test
```

The tests will provide coverage information and report any failing tests.

## Deployment

This application is deployed on Heroku. To deploy to Heroku, follow these steps:

1. Create a new Heroku app:
   ```bash
   heroku create your-app-name
   ```

2. Push your code to Heroku:
   ```bash
   git push heroku Dev-1:main
   ```

3. Run migrations on Heroku:
   ```bash
   heroku run python manage.py migrate
   ```

4. Open the application:
   ```bash
   heroku open
   ```

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to create a pull request.

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add a new feature'
   ```
4. Push the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Create a pull request.

## References

- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [OpenID Connect](https://openid.net/connect/)
- [Africa's Talking API](https://africastalking.com/docs/)
- [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python)

