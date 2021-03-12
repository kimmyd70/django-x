from django.urls import path
from .views import ListView, DetailView

urlpatterns = [
    path('', ListView.as_view(), name = 'pattern_list')
    path('<int:pk>/', DetailView.as_view(), name = 'pattern_detail')
    path('create/', CreateView.as_view(), name = 'pattern_create')
    path('<int:pk>/update', UpdateView.as_view(), name = 'pattern_update')
    path('<int:pk>/delete', DeleteView.as_view(), name = 'pattern_delete')

]