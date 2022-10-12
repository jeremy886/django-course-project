from django.http import HttpResponse
from django.shortcuts import render


def newsletter(request):
    return render(request, 'newsletter.html')


def about(request):
    return HttpResponse("About us: we run this store")


def home(request):
    return HttpResponse("Welcome to the store. This is our homepage.")
