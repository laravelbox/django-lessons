# Django Lessons

Reference: 
- https://www.w3schools.com/django/django_getstarted.php
- https://www.djangoproject.com
- https://realpython.com/get-started-with-django-1
- https://opensource.com/article/19/5/python-3-default-mac
- https://pypi.org/project/certifi/

## Lesson Modules

- [Set up Virtual Environment](#set-up-virtual-environment)
- [Create New Project](#create-new-project)
- [Create New App and Page](#create-new-app-and-page)
- [Create New Template](#create-new-template)
- [Create New Model](#create-new-model)
- [](#)

### Set up Virtual Environment

1. Install Python and PIP
- Install Python Version 3.12.0 at https://www.python.org/downloads/macos/
- Package manager like PIP (included  in Python from Version 3.4)
```
echo "alias python=/usr/local/bin/python3" >> ~/.bash_profile
python --version

echo "alias pip=/usr/local/bin/pip3" >> ~/.bash_profile
pip -V
```

Check if the alias has been inserted into the bash profile:
```
vi ~/.bash_profile
```

Install pip cert:
```
pip install certifi
```

2. Create a new virtual environment

Create virtual environment folder first and enter the virtual environment:
```
python -m venv django-virtual-env
source django-virtual-env/bin/activate
```
Install Django in the virtual environment:
```
python -m pip install Django
django-admin --version
```

### Create New Project

1. Create and start a new project in any directory:
```
cd django-lessons
django-admin startproject djangoproject
```

2. Run the Django Project
```
cd djangoproject
python manage.py runserver
```

3. Open a new browser window at http://127.0.0.1:8000

### Create New App and Page

1. Create new app for members
```
cd djangoproject
python manage.py startapp members
```

2. Create new view

Edit djangoproject/members/views.py
```
from django.http import HttpResponse
from django.shortcuts import render

# EA 31 Oct 2023 - Diplay new view
def members(request):
    return HttpResponse("Hello world!")

```

3. Create new urls file

Create djangoproject/members/urls.py:
```
from django.urls import path
from . import views

# EA 31 Oct 2023 - Create new urls file
urlpatterns = [
    path('members/', views.members, name='members'),
]
```

4. Edit main urls file

Edit djangoproject/djangoproject/urls.py:
```
from django.contrib import admin
from django.urls import include, path

# EA 31 Oct 2023 - Added url include for members
urlpatterns = [
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
]
```

5. Open the web browser at http://127.0.0.1:8000/members

### Create New Template

1. Create a new folder called djangoproject/members/templates

2. Create a new template html file called djangoproject/members/templates/firsttemplate.html
```
<!DOCTYPE html>
<html>
<body>

<h1>Hello World!</h1>
<p>Welcome to my first Django project!</p>

</body>
</html>
```

3. Edit member urls file

Edit djangoproject/members/urls.py:
```
from django.urls import path
from . import views

# EA 31 Oct 2023 - Create new urls file
urlpatterns = [
    path('members/', views.members, name='members'),
    path('members2/', views.members2, name='members2'),
]

```

4. Change settings to add members and templates path

Edit djangoproject/djangoproject/settings.py:
```
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # EA 31 Oct 2023 - Changed settings to add members
    'members',
]

... 

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # EA 31 Oct 2023 - Added path to templates
        "DIRS": [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```
5. Run migrate command to apply changes

```
python manage.py migrate
python manage.py runserver
```

6. Open the web browser at http://127.0.0.1:8000/members2

### Create New Model

1. Edit djangoproject/members/models.py

```
from django.db import models

# EA 31 Oct 2023 - Added member model class
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
```

2. Run makemigrations command to make migration file
```
python manage.py makemigrations members
```

3. Check new migration file at djangoproject/members/migrations/0001_initial.py

4. Run migrate command
```
python manage.py migrate

python manage.py sqlmigrate members 0001 # to check only
```