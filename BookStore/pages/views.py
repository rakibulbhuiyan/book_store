from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class Homeview(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = "about.html"
