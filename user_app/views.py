from django.shortcuts import render
from django.contrib.auth.decorators import login_required 


@login_required
def profile(request):
    user = request.user
    next = request.GET.get('next', '/')

    return render(request, "user_app/profile.html", 
    {
        "next": next,
        "user": user,
    })
