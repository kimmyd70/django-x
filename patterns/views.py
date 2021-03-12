from django.shortcuts import render
from django.urls import reverse_lazy
from django.generic.views import ListView, DetailView, DeleteView, CreateView, UpdateView

from .models import Pattern
# CRUD

class PatternCreateView(CreateView):
    template_name = 'patterns/pattern-create.html'
    model = Pattern
    fields = []

class PatternListView(ListView):
    template_name = 'patterns/pattern-list.html'
    model = Pattern
    
class PatternDetailView(DetailView):
    template_name = 'patterns/pattern-detail.html'
    model = Pattern
    
class PatternUpdateView(UpdateView):
    template_name = 'patterns/pattern-update.html'
    model = Pattern
    fields = []
    
class PatternDeleteView(DeleteView):
    template_name = 'patterns/pattern-delete.html'
    model = Pattern
    success_url = reverse_lazy("snack_list")
    



