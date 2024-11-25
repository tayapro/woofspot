from django.shortcuts import render
from django.http import HttpResponse

def my_signin_page(request):
    next = request.GET.get('next', '/')
    return render(request, "user_app/my_signin.html", 
    {
        "next": next,
    })

def my_signup_page(request):
    next = request.GET.get('next', '/')
    return render(request, "user_app/my_signup.html", 
    {
        "next": next,
    })


def my_signout_page(request):
    return render(request, "user_app/my_signout.html")