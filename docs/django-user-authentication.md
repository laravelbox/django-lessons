# User Authentication and Permissions

[Back to Main](../README.md)


## Add Project URL

Add site authentication url for secured access pages like login, logout, password and restricted pages

```
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
```
