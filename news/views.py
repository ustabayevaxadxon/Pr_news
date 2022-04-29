from django.shortcuts import render
from django.views.generic import ListView
from .models import POST


# Create your views here.

class HomePageView(ListView):
    model = POST
    template_name = 'home.html'
