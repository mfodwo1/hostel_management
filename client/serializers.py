from rest_framework import serializers
from .models import Hostel, Favorite, Booking, Review
from django.db.models import Avg


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    hostel = serializers.PrimaryKeyRelatedField(queryset=Hostel.objects.all())

    class Meta:
        model = Review
        fields = ['id', 'user', 'hostel', 'rating', 'comment']

    def validate_rating(self, value):
        if not 1 <= value <= 5:
            raise serializers.ValidationError("Rating must be between 1 and 5")
        return value


class HostelSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Hostel
        fields = ['id', 'name', 'location', 'description',
                  'image', 'price', 'reviews', 'average_rating',]

    def get_average_rating(self, obj):
        return obj.reviews.aggregate(Avg('rating'))['rating__avg']


class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    hostel = serializers.PrimaryKeyRelatedField(queryset=Hostel.objects.all())

    class Meta:
        model = Favorite
        fields = ['id', 'user', 'hostel']


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    hostel = serializers.PrimaryKeyRelatedField(queryset=Hostel.objects.all())

    class Meta:
        model = Booking
        fields = ['id', 'user', 'hostel', 'check_in_date', 'check_out_date']
