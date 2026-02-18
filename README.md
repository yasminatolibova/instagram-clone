Instagram Clone

This is a backend Instagram Clone project built with Django and Django REST Framework.

## 🚀 Features

- User Registration & Login
- JWT Authentication
- Create Post
- Like & Comment System
- Follow / Unfollow Users
- Stories
- Chat System
- Reels

---

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- JWT Authentication

---

## ⚙️ Installation

Clone the repository:

git clone https://github.com/yasminatolibova/instagram-clone.git
cd instagram-clone

Create virtual environment:

```
python -m venv env
```
Activate environment Windows: env\Scripts\activate

Install dependencies:

```
pip install -r requirements.txt
```

If requirements.txt doesn't exist:
```
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install pillow
pip install django-filter
```

Project and apps should be created:
```

django-admin startproject config .
django-admin startapp apps
py manage.py startapp accounts apps/accounts
py manage.py startapp posts apps/posts
py manage.py startapp reels apps/reels
py manage.py startapp story apps/story
py manage.py startapp chat apps/chat
py manage.py startapp comment apps/comment
```
All the apps should be inserted to config/settings.py
```
INSTALLED APPS=[
# packages
    'rest_framework',
    'rest_framework_simplejwt',
    'django_filters',
    'drf_yasg',

    # local apps
    'apps.accounts',
    'apps.posts',
    'apps.chat',
    'apps.reels',
    'apps.story',
    'apps.comment',
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',  
        'rest_framework.filters.SearchFilter',                
        'rest_framework.filters.OrderingFilter',              
    ],
}
```

The first thing after that filling models.py is crucial if not you cant makemigrations.
Then register all the models 
Run migrations:

```
python manage.py makemigrations
python manage.py migrate
```

Run server:

python manage.py runserver

---

## 🔑 Authentication

This project uses JWT authentication.

Get token:
/api/token/

Refresh token:
/api/token/refresh/

---

## 📌 API Endpoints

### 🔐 Authentication
- POST /api/token/
- POST /api/token/refresh/

### 👤 Accounts
- POST /api/register/
- GET /api/profile/

### 📝 Posts
- POST /api/posts/
- GET /api/posts/
- DELETE /api/posts/{id}/

### 💬 Comments
- POST /api/comments/
- GET /api/comments/?post_id=1

### ❤️ Likes
- POST /api/posts/{id}/like/

### 👥 Follow
- POST /api/follow/{user_id}/
  

## 📑 API Documentation

Swagger UI available at:
/swagger/
![sw](https://github.com/user-attachments/assets/0d639ca1-5a2c-4a89-92f2-4f1406561897)



## 📂 Project Structure

apps/

 ├── accounts/
 
 ├── posts/
 
 ├── comment/
 
 ├── story/
 
 ├── chat/
 
 ├──reels/
 

---
## 🏗 Architecture

- Modular apps structure
- JWT based authentication
- Pagination enabled
- Filtering, Search, Ordering
- Separate comment app
- Separate chat app
Dont forget to add requirements.txt
```
pip freeze > requirements.txt
```




## 👩‍💻 Author

Yasmina Tolibova
