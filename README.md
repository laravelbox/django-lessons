# Django Lessons

References

- https://www.w3schools.com/django/django_getstarted.php
- https://www.djangoproject.com
- https://realpython.com/get-started-with-django-1
- https://opensource.com/article/19/5/python-3-default-mac
- https://pypi.org/project/certifi/
- https://sqlitebrowser.org/dl/
- https://www.geeksforgeeks.org/django-tutorial/
- https://www.geeksforgeeks.org/django-rest-framework-installation/
- https://www.geeksforgeeks.org/how-to-create-a-basic-api-using-django-rest-framework/


## Quick Start

1. Run commands to start virtual environment and server

```
django-virtual-env\Scripts\activate.bat

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py test # Run the standard tests. These should all pass.
python manage.py createsuperuser # Create a superuser
python manage.py runserver
```

2. Open admin site on web browser http://127.0.0.1:8000/admin/

3. Open main site on web browser http://127.0.0.1:8000/


## Lesson Modules

Basics

- [Set up Virtual Environment](#set-up-virtual-environment)
- [Create New Project](#create-new-project)
- [Create New App and Page](#create-new-app-and-page)
- [Create New Template](#create-new-template)
- [Create New Model](#create-new-model)
- [View SQL and Add Records](#view-sql-and-add-records)
- [Update and Delete Records](#update-and-delete-records)
- [Create Update Model](#create-update-model)

Admin

- [Create Admin User](#create-admin-user)
- [Include Member in Admin and Display List](#include-member-in-admin-and-display-list)

Display Template

- [Create Template](#create-template)
- [Create Details Link](#create-details-link)
- [Create Master Template](#create-master-template)
- [Create Main Index Page](#create-main-index-page)
- [Create Error Page](#create-error-page)


Database

- [Connect to Database](#connect-to-database)
- [](#)

Authentication and Session
- [User Authentication and Permissions](docs/django-user-authentication.md)

Views
- [Create Views](docs/django-views.md)



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

django-virtual-env\Scripts\activate.bat
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

4. Run migrate command to create new table
```
python manage.py migrate

python manage.py sqlmigrate members 0001 # to check only
```

### View SQL and Add Records

1. Check djangoproject/members/migrations/0001_initial.py output
```
python manage.py sqlmigrate members 0001
```
2. Use Python Shell to run python codes to add records
```
python manage.py shell
```

3. Add records using shell

Query to view records of table
```
from members.models import Member
Member.objects.all()
```

Add a new record to the table
```
member = Member(firstname='Mary', lastname='Chan')
member.save()
```

Query to view records of the table
```
from members.models import Member
Member.objects.all()
Member.objects.all().values()
```

Add multiple records
```
member1 = Member(firstname='Apple', lastname='Tay')
member2 = Member(firstname='Betty', lastname='Uma')
member3 = Member(firstname='Catherine', lastname='Vera')
members_list = [member1, member2, member3]
for x in members_list:
    x.save()

Member.objects.all().values()
```

### Update and Delete Records

1. Update record

Display first record's first name
```
from members.models import Member
member1 = Member.objects.all()[0]
member1.firstname
```

Update firstname of first record
```
from members.models import Member
member1 = Member.objects.all()[0]
member1.firstname = "Zero"
member1.save()

member1.firstname
Member.objects.all().values()

```

2. Delete record

Display first name of 2nd record
```
from members.models import Member
member2 = Member.objects.all()[1]
member2.firstname
```

Delete 2nd record
```
member2.delete()
Member.objects.all().values()
```



### Create Update Model

1. Add 2 new fields to the model
```
from django.db import models

# EA 31 Oct 2023 - Added member model class
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  # EA 1 Nov 2023 - Added 2 new fields
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

```

2. Run makemigration to create migration file 
```
python manage.py makemigrations members
```

3. View newly created file at djangoproject/members/migrations/0002_member_joined_date_member_phone.py

4. Run migrate command to add new fields to the table
```
python manage.py migrate
```

5. Open shell to update fields

```
python manage.py shell
```
```
from members.models import Member
member1 = Member.objects.all()[0]
member1.phone = 91939393
member1.joined_date = '2023-11-1'

member1.save()
Member.objects.all().values()
```


### Create Admin User

1. Enter username, email and password to create a new admin user
```
python manage.py createsuperuser
```
2. Start server
```
python manage.py runserver
```

3. Open a new web browser and run http://127.0.0.1:8000/admin

### Include Member in Admin and Display List

1. Edit djangoproject/members/admin.py
```
from django.contrib import admin
from .models import Member

# Register your models here.

# EA 1 Nov 2023 - Registered member model
admin.site.register(Member)
```

2. Refresh admin page to see Members module in the admin dashboard
http://127.0.0.1:8000/admin

3. Set string representation of object in Python if only one default column in list display 

Edit djangoproject/members/models.py:
```
# EA 1 Nov 2023 - Set string representation of object in Python
def __str__(self):
    return f"{self.firstname} {self.lastname}"
```

4. Set list display with specified columns

Edit djangoproject/members/admin.py:

```
# EA 1 Nov 2023 - Set list display for member
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
  
admin.site.register(Member, MemberAdmin)
```

5. Add, Update and Delete functions are automatically included in the module by default

### Connect to Database

1. To connect to MySQL, install mySQL Server at https://dev.mysql.com/downloads/mysql/ and then install mysqlclient

```
brew install mysql pkg-config
pip install mysqlclient
```

2. Update database setting to connect to mysql database

Edit djangoproject/djangoproject/settings.py:
```
# EA 1 Nov 2023 - Updated to connect to mysql database instead of sqlite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testing',
        'USER': 'sail',
        'PASSWORD': 'password',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    },
    'default2': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

3. Run migrate command to create tables
```
python manage.py migrate
```

4. Check out new tables using phpmyadmin at http://127.0.0.1:8080/index.php?route=/database/structure&db=testing

Note: I use Docker to run phpmyadmin server for mysql database (See Laravel project separately)


### Create Template

1. Create a new template 

djangoproject/members/templates/all_members.html:
```
<!DOCTYPE html>
<html>
<body>

<h1>Members</h1>
  
<ul>
  {% for x in mymembers %}
    <li>{{ x.firstname }} {{ x.lastname }}</li>
  {% endfor %}
</ul>

</body>
</html>
```

2. Update view

Edit djangoproject/members/views.py:
```
# EA 12 Nov 2023 - Display new view with all members template
def members3(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
```
3. Add url

Edit djangoproject/members/urls.py:

```
# EA 31 Oct 2023 - Create new urls file
urlpatterns = [
    path('members/', views.members, name='members'),
    path('members2/', views.members2, name='members2'),
    path('members3/', views.members3, name='members3'),
]
```

4. Run http://127.0.0.1:8000/members3/


### Create Details Link

1. Create new template

djangoproject/members/templates/details.html
```
<!DOCTYPE html>
<html>

<body>

<h1>{{ mymember.firstname }} {{ mymember.lastname }}</h1>
  
<p>Phone: {{ mymember.phone }}</p>
<p>Member since: {{ mymember.joined_date }}</p>

<p>Back to <a href="/members3">Members</a></p>

</body>
</html>
```

2. Create details link

Edit djangoproject/members/templates/all_members.html:
```
<!DOCTYPE html>
<html>
<body>

<h1>Members</h1>
  
<ul>
  {% for x in mymembers %}
    <li><a href="details/{{ x.id }}">{{ x.firstname }} {{ x.lastname }}</a></li>
  {% endfor %}
</ul>

</body>
</html>
```

3. Create new view

Edit djangoproject/members/views.py:
```
# EA 13 Nov 2023 - Display new view for displaying details
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
```
4. Add url

Edit djangoproject/members/urls.py:
```
path('members3/details/<int:id>', views.details, name='details'),
```

### Create Master Template

1. Create master template

djangoproject/members/templates/master.html:
```
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}{% endblock %}</title>
</head>
<body>

<h1>{% block title2 %}{% endblock %}</h1>

{% block content %}
{% endblock %}

</body>
</html>
```

2. Edit view templates

djangoproject/members/templates/all_members2.html:
```
{% extends "master.html" %}

{% block title %}
  List of all members
{% endblock %}

{% block title2 %}
  Showing list of all members
{% endblock %}


{% block content %}
  <h1>Members3</h1>
  
  <ul>
    {% for x in mymembers %}
      <li><a href="details2/{{ x.id }}">{{ x.firstname }} {{ x.lastname }}</a></li>
    {% endfor %}
  </ul>
{% endblock %}
```

djangoproject/members/templates/details2.html:
```
{% extends "master.html" %}

{% block title %}
  Details about {{ mymember.firstname }} {{ mymember.lastname }}
{% endblock %}

{% block title2 %}
  Showing Details about {{ mymember.firstname }} {{ mymember.lastname }}
{% endblock %}


{% block content %}
  <h1>{{ mymember.firstname }} {{ mymember.lastname }}</h1>
  
  <p>Phone {{ mymember.phone }}</p>
  <p>Member since: {{ mymember.joined_date }}</p>
  
  <p>Back to <a href="/members4">Members</a></p>
  
{% endblock %}
```
3. Edit views and urls


### Create Main Index Page

1. Create main template (homepage view)

djangoproject/members/templates/main.html:
```
{% extends "master.html" %}

{% block title %}
  My List of Members
{% endblock %}

{% block title2 %}
  Showing List of Members
{% endblock %}

{% block content %}

  <h3>Members4</h3>
  
  <p>Check out all our <a href="members4/">members</a></p>
  
{% endblock %}
```

2. Edit view

Edit djangoproject/members/views.py:
```
# EA 13 Nov 2023 - Display new view for displaying main
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
```

3. Edit url

Edit djangoproject/members/urls.py:
```
path('', views.main, name='main'),
```

### Create Error Page

1. Set debug to false

Edit djangoproject/djangoproject/settings.py:
```
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']
```

2. Create error page

djangoproject/members/templates/404.html:
```
<!DOCTYPE html>
<html>
<title>404 Error</title>
<body>

<h1>Ooops!</h1>

<h2>Sorry, we are unable to find the file you requested!</h2>

</body>
</html>
```
