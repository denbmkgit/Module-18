from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class main_page(TemplateView):
    template_name = 'main_page.html'

class shope(TemplateView):
    template_name = 'shope.html'

class basket(TemplateView):
    template_name = 'basket.html'
