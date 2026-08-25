# Django E-commerce Platform — Major Project

A complete internship-ready e-commerce foundation using Django, SQLite for development, Django authentication, sessions, cart, orders, search/filtering, admin customization, and Stripe sandbox integration.

## Modules
1. Django setup and configuration
2. Categories and Products
3. User registration/login/logout/profile
4. Product listing/detail/search/filter
5. Session cart for guests
6. Authenticated cart
7. Checkout and address
8. Order management
9. Stripe sandbox payment
10. Django Admin
11. Static files and environment configuration
12. Deployment-ready structure

## Run
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Environment
Copy `.env.example` to `.env` and configure secret key and Stripe test keys.

## Git
```bash
git init
git add .
git commit -m "Initial Django ecommerce platform"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/django-ecommerce-platform.git
git push -u origin main
```

## Deployment
Use a production database such as PostgreSQL, collect static files, set DEBUG=False, configure ALLOWED_HOSTS/CORS/CSRF, and provide Stripe test/production environment variables through the hosting platform.

## Important
Payment code is sandbox-oriented. Never store raw card details. Use Stripe Checkout/PaymentIntent and test keys.
