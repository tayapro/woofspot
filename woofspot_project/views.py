from django.shortcuts import render
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseForbidden, HttpResponseNotFound,
                         HttpResponseServerError)
from django.urls import reverse


PUBLIC_HOME_URL = "https://woofspot.taya.one/"


def robots_txt(request):
    sitemap_url = PUBLIC_HOME_URL.rstrip("/") + reverse("sitemap_xml")
    return HttpResponse(
        f"User-agent: *\nDisallow:\n\nSitemap: {sitemap_url}\n",
        content_type="text/plain; charset=utf-8",
    )


def sitemap_xml(request):
    return HttpResponse(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"  <url><loc>{PUBLIC_HOME_URL}</loc></url>\n"
        "</urlset>\n",
        content_type="application/xml; charset=utf-8",
    )


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
    return HttpResponseForbidden(render(request, "403.html"), status=403)


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
