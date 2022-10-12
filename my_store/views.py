from django.shortcuts import render
from django.views.generic import TemplateView


def about(request):
    return render(request, 'about.html')


class Home(TemplateView):
    template_name = 'home.html'
