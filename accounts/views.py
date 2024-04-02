from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


class SignupView (generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

