from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import SubscriberForm
from .models import Subscriber


def newsletter(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subscriber = Subscriber(name=name, email=email)
            subscriber.save()
            messages.success(
                request,
                "Thanks for signing up to our newsletter!",
            )
            return redirect("/")
    else:
        form = SubscriberForm()
    return render(request, "newsletter.html", {"form": form})
