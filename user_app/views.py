from django.shortcuts import render
from django.http import HttpResponse

def get_started_page(request):
    return render(request, "user_app/get_started.html")

def logout_new_page(request):
    return render(request, "user_app/logout_new.html")