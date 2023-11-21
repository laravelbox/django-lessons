from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Member

# EA 31 Oct 2023 - Diplay new view
def members(request):
    return HttpResponse("Hello world!")

# EA 31 Oct 2023 - Diplay new view with template
def members2(request):
    template = loader.get_template('firsttemplate.html')
    return HttpResponse(template.render())

# EA 12 Nov 2023 - Display new view with all members template
def members3(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


# EA 13 Nov 2023 - Display new view with all members template
def members4(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members2.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

# EA 13 Nov 2023 - Display new view for displaying details
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

# EA 13 Nov 2023 - Display new view for displaying details
def details2(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details2.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

# EA 13 Nov 2023 - Display new view for displaying main
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

# EA 21 Nov 2023 - Test a simple view
from django.http import HttpResponse, HttpResponseNotFound

def show_message(request):
    #html = "<html><body>Hello!</body></html>"
    #return HttpResponse(html)
    #return HttpResponseNotFound("<h1>Page not found</h1>")
    