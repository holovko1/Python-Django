from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse("Головна сторінка")
    return render(request, "home.html")

def contact(request):
    # return HttpResponse("Контакти")
    return render(request, "contact.html")