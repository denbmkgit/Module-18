from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def func_template(request):
    return render(request, 'func_template.html')

class class_template(TemplateView):
    template_name = 'class_template.html'

def check():
    print('I am from UrbanDjango.task2.views import check')

    #        python manage.py startapp task3