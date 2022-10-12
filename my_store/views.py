from django.shortcuts import render


def newsletter(request):
    return render(request, 'newsletter.html')


def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'home.html')
