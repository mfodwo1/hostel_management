from django.urls import path
from . import views

urlpatterns = [
    path('hostel/categories/', views.HostelCategoryListCreateView.as_view(),
         name='hostel/category-list'),
    path('hostel/categories/<int:pk>/',
         views.HostelCategoryDetailView.as_view(), name='hostel-category-detail'),
]
