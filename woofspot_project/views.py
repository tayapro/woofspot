from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden


def trigger_400(request):
    print("TRIGGER_400")
    return HttpResponseBadRequest(render(request, "400.html"))


def trigger_403(request):
    print("TRIGGER_403")
    return HttpResponseForbidden(render(request, "403.html"))


def trigger_500(request):
    raise Exception("This is a test exception for the 500 error page.")
