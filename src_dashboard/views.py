from rest_framework import generics, permissions
from .models import HostelCategory
from .serializers import HostelCategorySerializer


class HostelCategoryListCreateView(generics.ListCreateAPIView):
    queryset = HostelCategory.objects.all()
    serializer_class = HostelCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HostelCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HostelCategory.objects.all()
    serializer_class = HostelCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
