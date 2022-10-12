from django import forms


class SubscriberForm(forms.Form):
    """Form for newsletter subscriber."""

    name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(max_length=254)
