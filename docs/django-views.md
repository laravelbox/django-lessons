# Views

A view function takes a web request and returns a web response, that is view.py.

[Back to Main](../README.md)


## Create View

1. Create a new view in view.py

```
from django.http import HttpResponse, HttpResponseNotFound

def show_message(request):
    #html = "<html><body>Hello!</body></html>"
    #return HttpResponse(html)
    if foo:
        return HttpResponseNotFound("<h1>Page not found</h1>")
    else:
        return HttpResponse("<h1>Page was found</h1>")

```

2. Add url in urls.py
```
urlpatterns = [
    path('show-message/', views.show_message, name='show-message'),
    
]
```