from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'sahifa.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class SozlamalarPageView(TemplateView):
    template_name = 'sozlamalar.html'