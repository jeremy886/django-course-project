from django.shortcuts import render


def newsletter(request):
    return render(request, 'newsletter.html')
