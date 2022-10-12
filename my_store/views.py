from django.http import HttpResponse
from django.template.loader import get_template


def newsletter(request):
    template = get_template('newsletter.html')
    return HttpResponse(template.render())


def about(request):
    return HttpResponse("About us: we run this store")


def home(request):
    return HttpResponse("Welcome to the store. This is our homepage.")
