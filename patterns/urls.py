from django.urls import path
from .views import PatternListView, PatternDetailView, PatternCreateView, PatternUpdateView, PatternDeleteView

urlpatterns = [
    path('', PatternListView.as_view(), name = 'pattern_list'),
    path('<int:pk>/', PatternDetailView.as_view(), name = 'pattern_detail'),
    path('create/', PatternCreateView.as_view(), name = 'pattern_create'),
    path('<int:pk>/update', PatternUpdateView.as_view(), name = 'pattern_update'),
    path('<int:pk>/delete', PatternDeleteView.as_view(), name = 'pattern_delete'),
]