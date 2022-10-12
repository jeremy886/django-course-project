from django.http import HttpResponse


def newsletter(request):
    return HttpResponse("Subscribe to our newsletter")


def about(request):
    return HttpResponse("About us: we run this store")


def home(request):
    return HttpResponse("Welcome to the store. This is our homepage.")
