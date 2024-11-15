from django.shortcuts import render
from django.http import HttpResponse

def login_new_page(request):
    return render(request, "user_app/login_new.html")
