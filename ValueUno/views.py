from django.shortcuts import render
from django.views.generic import TemplateView
import uploads

class Home(TemplateView):
    template_name = 'valueuno/home.html'


def addNew():
    return render()