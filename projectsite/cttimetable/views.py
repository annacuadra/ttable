from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import TemplateView


# Create your views here.
    
class HomePageView(TemplateView):
    # model = Play
    # context_object_name = 'play'
    template_name = "landingpage/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context