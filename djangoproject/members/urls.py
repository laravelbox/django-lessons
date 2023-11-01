from django.urls import path
from . import views

# EA 31 Oct 2023 - Create new urls file
urlpatterns = [
    path('members/', views.members, name='members'),
    path('members2/', views.members2, name='members2'),
]
