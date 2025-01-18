from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound, HttpResponseServerError


# Custom error handlers
def custom_400(request, exception):
    return  HttpResponseBadRequest(render(request, "400.html"))

def custom_403(request, exception):
    return HttpResponseForbidden(render(request, "403.html"))

def custom_404(request, exception):
    return HttpResponseNotFound(render(request, "404.html"))

def custom_500(request):
    return HttpResponseServerError(render(request, "500.html"))
