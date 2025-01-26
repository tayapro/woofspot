from django.shortcuts import render
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseForbidden, HttpResponseNotFound,
                         HttpResponseServerError)


# Custom error handlers


def custom_400(request, exception):
    """
    Handle 400 Bad Request errors by rendering the custom 400 error page.

    Parameters:
        request: The HTTP request object.
        exception: The exception that triggered the error.
    """
    return HttpResponseBadRequest(render(request, "400.html"))


def custom_403(request, exception):
    """
    Handle 403 Forbidden errors by rendering the custom 403 error page.

    Parameters:
        request: The HTTP request object.
        exception: The exception that triggered the error.
    """
    return HttpResponseForbidden(render(request, "403.html"))


def custom_404(request, exception):
    """
    Handle 404 Not Found errors by rendering the custom 404 error page.

    Parameters:
        request: The HTTP request object.
        exception: The exception that triggered the error.
    """
    return HttpResponseNotFound(render(request, "404.html"))


def custom_500(request):
    """
    Handle 500 Internal Server errors by rendering the custom 500 error page.

    Parameters:
        request: The HTTP request object.
    """
    return HttpResponseServerError(render(request, "500.html"))


def custom_403_csrf(request, reason=""):
    """
    Custom view to handle CSRF failures.

    Parameters:
        request: The HTTP request object.
        reason: A string explaining the reason for the CSRF failure.
    """
    context = {"reason": reason}
    return HttpResponseForbidden(render(request, "403.html", context))
