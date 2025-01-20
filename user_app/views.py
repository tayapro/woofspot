"""
Views for the `user_app`.

All views in this module should be protected by the @login_required decorator, 
ensuring that only authenticated users can access them.
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    """
    Render the user profile page.

    This view retrieves the authenticated user's details and displays their profile information.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered profile page.
    """

    # Get the 'next' parameter for redirection 
    # or default to the root URL
    next = request.GET.get('next', '/')

    return render(request, "user_app/profile.html", {
        "next": next,
        "user": request.user,
    })
