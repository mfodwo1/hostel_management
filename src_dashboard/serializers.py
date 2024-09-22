from rest_framework import serializers
from .models import HostelCategory, Hostel


class HostelCategorySerializer(serializers.ModelSerializer):
    hostels = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Hostel.objects.all())

    class Meta:
        model = HostelCategory
        fields = ['id', 'name', 'hostels']
