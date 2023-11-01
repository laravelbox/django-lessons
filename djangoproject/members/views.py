from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# EA 31 Oct 2023 - Diplay new view
def members(request):
    return HttpResponse("Hello world!")

# EA 31 Oct 2023 - Diplay new view with template
def members2(request):
    template = loader.get_template('firsttemplate.html')
    return HttpResponse(template.render())