from django.shortcuts import render
from .models import *
from django.views.generic import DetailView,ListView

# Create your views here.
class NiveauListView(ListView):
    context_object_name = 'niveaux'
    model = Niveau
    template_name = 'programmes/niveau_list.html'
