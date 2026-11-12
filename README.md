
# Django eCommerce Application – Part 1

## Project Overview

This project is a Django-based eCommerce application developed as part of the ASU Software Engineering Bootcamp.

The application supports buyer and vendor accounts, online stores,
product listings, shopping carts, checkout, order management,
product reviews, and password reset functionality.

## Features

- Buyer and vendor registration and login
- Vendor store and product management
- Product listings and shopping cart
- Buyer checkout and order confirmation
- Product reviews and verified purchase indicators
- Password reset functionality

## Technologies Used

- Python
- Django
- MariaDB 11.8
- mysqlclient
- HTML

## Installation Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/tonyyoung2611/django-ecommerce-part1.git
cd ecommerce_project
```

Replace `YOUR_REPOSITORY_URL` with the actual GitHub repository URL. If the repository contains an additional project folder, navigate into the folder containing `manage.py`.

### 2. Create a Virtual Environment

```bash
python -m venv myenv
```

### 3. Activate the Virtual Environment

Windows PowerShell:

```powershell
.\myenv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Configure MariaDB

Install MariaDB Server 11.8 and log in as the root user.

Create the database and application user:

```sql
CREATE DATABASE ecommerce_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER 'ecommerce_user'@'localhost' IDENTIFIED BY 'YOUR_SECURE_PASSWORD';

GRANT ALL PRIVILEGES ON ecommerce_db.* TO 'ecommerce_user'@'localhost';
```

Replace `YOUR_SECURE_PASSWORD` with your own secure password.

In Windows PowerShell, set the database password:

```powershell
$env:ECOMMERCE_DB_PASSWORD = Read-Host "Enter your MariaDB ecommerce_user password"
```

The password must match the one configured in MariaDB.

Keep this environment variable set in the terminal used to run Django.

Do not commit passwords or other sensitive credentials to GitHub.

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Create an Administrator Account

```bash
python manage.py createsuperuser
```

### 8. Start the Django Server

```bash
python manage.py runserver 8001
```

Open the application at:

http://127.0.0.1:8001/

## Authentication and Authorization

Store and product creation require an authenticated vendor account.

Vendors can only add products to stores they own.

Product review retrieval is restricted to vendors who own the corresponding product.


## Project Status

The Django eCommerce Application Part 1 has been developed
and configured to use MariaDB as its database.

Database connectivity has been verified, all migrations
are applied, and Django system checks pass without errors.

The application includes buyer and vendor functionality,
product management, shopping carts, checkout, orders,
and product reviews.

## Author

Tony Young

ASU Software Engineering Bootcamp