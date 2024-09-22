from rest_framework import generics, permissions, status, filters
from rest_framework.response import Response
from django.db.models import Avg, Q
from .models import Hostel, Favorite, Booking, Review
from .serializers import (
    HostelSerializer, FavoriteSerializer, BookingSerializer, ReviewSerializer)


class HostelListCreateView(generics.ListCreateAPIView):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HostelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HostelListAPIView(generics.ListAPIView):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'location']
    ordering_fields = ['name', 'price', 'location', 'average_rating']

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter by top ratings
        if self.request.query_params.get('top_ratings'):
            queryset = queryset.annotate(avg_rating=Avg(
                'reviews__rating')).order_by('-avg_rating')

        # Filter by booked hostels
        if self.request.query_params.get('booked_hostels'):
            queryset = queryset.filter(bookings__isnull=False).distinct()

        # Filter by favourite hostels
        if self.request.query_params.get('favourite_hostels'):
            queryset = queryset.filter(favorites__isnull=False).distinct()

        # Filter by user's favourite hostels
        if self.request.query_params.get('my_favourite_hostels'):
            queryset = queryset.filter(
                favorites__user=self.request.user).distinct()

        # Filter by user's booked hostels
        if self.request.query_params.get('my_booked_hostels'):
            queryset = queryset.filter(
                bookings__user=self.request.user).distinct()

        # Filter by user's reviews
        if self.request.query_params.get('my_reviews'):
            queryset = queryset.filter(
                reviews__user=self.request.user).distinct()

        return queryset


class FavoriteListCreateView(generics.ListCreateAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Set the user field to the authenticated user
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FavoriteDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)


class BookingListCreateView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Set the user field to the authenticated user
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        # Check if the hostel is already booked within the specified date range
        check_in_date = request.data.get("check_in_date")
        check_out_date = request.data.get("check_out_date")
        hostel_id = request.data.get("hostel")

        existing_booking = Booking.objects.filter(
            Q(hostel=hostel_id) &
            (
                Q(check_in_date__range=[check_in_date, check_out_date]) |
                Q(check_out_date__range=[check_in_date, check_out_date]) |
                (
                    Q(check_in_date__lte=check_in_date) &
                    Q(check_out_date__gte=check_out_date)
                )
            )
        )

        if existing_booking.exists():
            return Response({'Detail': 'Hostel is already booked within the specified date range'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Set the user field to the authenticated user
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        request.data['user'] = self.request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)
