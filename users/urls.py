from django.urls import path
from django.contrib.auth import views as auth_views

from .views import logout_view, RegistrationView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html')),
    path('logout/', logout_view),
    path('register/', RegistrationView.as_view()),
]
