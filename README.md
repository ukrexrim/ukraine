# [Django Admin Soft](https://github.com/app-generator/django-admin-soft-dashboard) 

Modern template for **Django Admin Interface** coded on top of **Soft UI Dashboard**, an open-source `Boostrap 5` design from `Creative-Tim`.

> Actively supported by [AppSeed](https://appseed.us/) via `Email` and `Discord`.

<br>

**Links & Resources**

- UI Kit: [Soft Dashboard BS5](https://www.creative-tim.com/product/soft-ui-dashboard?AFFILIATE=128200) `v1.0.6` by Creative-Tim
- [Django Soft Dashboard](https://django-soft-ui-dashboard.appseed-srv1.com/) - LIVE Demo
- [Django Soft Dashboard](https://github.com/app-generator/django-admin-soft-dashboard_p) - `playground project`

<br />

![Django Admin Soft - Template project for Django provided by AppSeed.](https://user-images.githubusercontent.com/51070104/175773323-3345d618-0e78-4c85-83fc-f495dc3f0bb0.png)

<br>

## Why `Django Admin Soft`

- Modern `Bootstrap 5` Design
- `Responsive Interface`
- `Minimal Template` overriding
- `Easy integration`

<br />

## How to use it

<br />

> **Install the package** via `PIP` 

```bash
$ pip install django-admin-soft-dashboard
// OR
$ pip install git+https://github.com/app-generator/django-admin-soft-dashboard.git
```

<br />

> Add `admin_soft` application to the `INSTALLED_APPS` setting of your Django project `settings.py` file (note it should be before `django.contrib.admin`):

```python
    INSTALLED_APPS = (
        ...
        'admin_soft.apps.AdminSoftDashboardConfig',
        'django.contrib.admin',
    )
```

<br />

> Add `LOGIN_REDIRECT_URL` and `EMAIL_BACKEND` of your Django project `settings.py` file:

```python
    LOGIN_REDIRECT_URL = '/'
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

<br />

> Add `admin_soft` urls in your Django Project `urls.py` file

```python
    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('admin_soft.urls')),
    ]
```

<br />

> **Collect static** if you are in `production environment`:

```bash
$ python manage.py collectstatic
```

<br />

> **Start the app**

```bash
$ # Set up the database
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Create the superuser
$ python manage.py createsuperuser
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
```

Access the `admin` section in the browser: `http://127.0.0.1:8000/`

<br />

## Screenshots

Designed for those who like bold elements and beautiful websites Soft UI Dashboard is ready to help you create stunning websites and webapps.
this open-source [Bootstrap 5](https://www.admin-dashboards.com/bootstrap-5-templates/) Kit is built with over 70 frontend individual elements, like buttons, inputs, navbars, navtabs, cards or alerts, giving you the freedom of choosing and combining.

<br />

> **[Django Admin Soft](https://github.com/app-generator/django-admin-soft-dashboard)** - `Admin Section` 

![Django Admin Soft (Dark Mode) - Template project for Django provided by AppSeed.](https://user-images.githubusercontent.com/51070104/192209421-c71ebb42-7851-47eb-9942-6054e2010b82.jpg)

<br />

> **[Django Admin Soft](https://github.com/app-generator/django-admin-soft-dashboard)** - `SignIN Page` 

![Django Admin Soft (Login Page) - Template project for Django provided by AppSeed.](https://user-images.githubusercontent.com/51070104/192209441-2182d38f-814e-4123-ad54-7c3b580198fe.jpg) 

<br />

---
**[Django Admin Soft](https://github.com/app-generator/django-admin-soft-dashboard)** - Modern Admin Interface provided by **[AppSeed](https://appseed.us/)**
