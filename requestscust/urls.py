from django.urls import path
from .views import (CustomerRequestListCreateView,CustomerRequestDetailView,)

urlpatterns = [
    path('',CustomerRequestListCreateView.as_view(),name='request-list-create'),
    path('<int:pk>/',CustomerRequestDetailView.as_view(),name='request-detail'),
]