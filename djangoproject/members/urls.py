from django.urls import path
from . import views

# EA 31 Oct 2023 - Create new urls file
urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members2/', views.members2, name='members2'),
    path('members3/', views.members3, name='members3'),
    path('members3/details/<int:id>', views.details, name='details'),
    path('members4/', views.members4, name='members4'),
    path('members4/details2/<int:id>', views.details2, name='details2'),
]

