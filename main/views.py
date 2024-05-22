from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView


# Create your views here.

class IndexView(TemplateView):
    template_name = 'main/index.html'