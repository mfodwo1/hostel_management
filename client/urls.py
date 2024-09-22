from django.urls import path
from . import views

urlpatterns = [
    # Hostel URLs
    path('hostels/', views.HostelListCreateView.as_view(), name='hostel-list'),
    path('hostels/<int:pk>/', views.HostelDetailView.as_view(), name='hostel-detail'),
    path('hostels/search/', views.HostelListAPIView.as_view(), name='hostel-search'),


    # Favorite URLs
    path('favorites/', views.FavoriteListCreateView.as_view(), name='favorite-list'),
    path('favorites/<int:pk>/', views.FavoriteDetailView.as_view(),
         name='favorite-detail'),

    # Booking URLs
    path('bookings/', views.BookingListCreateView.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', views.BookingDetailView.as_view(),
         name='booking-detail'),

    # Review URLs
    path('reviews/', views.ReviewListCreateView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
]
