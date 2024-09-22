# Hostel Management System

A comprehensive hostel management system built with Django. This project allows users to manage hostels, bookings, reviews, and favorites.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction

This project provides a platform for managing hostels, allowing users to book rooms, leave reviews, and mark their favorite hostels. The application includes features for searching and filtering hostels based on various criteria.

## Features

- User authentication and authorization
- Hostel management (CRUD)
- Booking management
- Reviews and ratings
- Favorites
- Search and filter functionality

## Installation

### Prerequisites

- Python 3.8+
- Django 3.2+
- MySQL
- pip

### Steps

1.  Clone the repository:

    ```
    git clone https://github.com/your/repository.git
    cd project-directory
    ```

2.  Create and activate a virtual environment:

    ```
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3.  Install dependencies:

    ```
    pip install -r requirements.txt
    ```

4.  Set up environment variables:

        Create a `.env` file in the root directory:

        ```env
        DJANGO_SECRET_KEY=your-secret-key
        DJANGO_DEBUG=False
        DJANGO_ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
        DB_NAME=your_db_name
        DB_USER=your_db_user
        DB_PASSWORD=your_db_password
        DB_HOST=your_db_host
        DB_PORT=your_db_port
        DJANGO_SECURE_SSL_REDIRECT=True

        EMAIL_HOST=your_host
        EMAIL_PORT=your_host_port
        EMAIL_HOST_USER=your_gmail_address
        EMAIL_HOST_PASSWORD=your_host_password
        EMAIL_USE_TLS=True
    ```

5.  Apply migrations:

    ```
    python manage.py migrate
    ```

6.  Collect static files:

    ```
    python manage.py collectstatic
    ```

7.  Run the development server:

    ```
    python manage.py runserver
    ```

## Usage

- Visit `http://127.0.0.1:8000` to access the application.
- Use the Django admin interface for administrative tasks.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
