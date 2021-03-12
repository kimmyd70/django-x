from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView, 
    DeleteView, 
    CreateView, 
    UpdateView,
)   

from .models import Pattern
# CRUD

class PatternCreateView(CreateView):
    template_name = 'pattern-create.html'
    model = Pattern
    fields = []

class PatternListView(ListView):
    template_name = 'pattern-list.html'
    model = Pattern
    
class PatternDetailView(DetailView):
    template_name = 'pattern-detail.html'
    model = Pattern
    
class PatternUpdateView(UpdateView):
    template_name = 'pattern-update.html'
    model = Pattern
    fields = []
    
class PatternDeleteView(DeleteView):
    template_name = 'pattern-delete.html'
    model = Pattern
    success_url = reverse_lazy("pattern_list")
    



