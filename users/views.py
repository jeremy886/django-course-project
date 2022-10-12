from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render

from .forms import RegistrationForm


def logout_view(request):
    logout(request)
    return redirect("/")


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request,
                "Thanks for creating an account!",
            )
            return redirect("/")
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form})
