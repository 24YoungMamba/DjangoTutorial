from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html")

def about(request, name, age): 
    context = {
        "person": {
            "name": name,
            "age": age,
        }
    }

    return render(request, "about.html", context)

def contact(request):
    return HttpResponse("<h1>Contact Page</h1>")