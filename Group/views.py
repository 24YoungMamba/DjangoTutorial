from django.shortcuts import render
from django.contrib.auth.models import User

def user_view(request):
    users = User.objects.all()

    context = {
        "users": users
    }


    return render(request, "users.html", context)