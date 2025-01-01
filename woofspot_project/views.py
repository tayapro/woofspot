from django.http import HttpResponse

def trigger_500(request):
    raise Exception("This is a test exception for the 500 error page.")
