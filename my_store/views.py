from django.http import HttpResponse


def newsletter(request):
    return HttpResponse("Subscribe to our newsletter")
