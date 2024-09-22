from django.db import models
from client.models import Hostel

class HostelCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Category Name")
    hostels = models.ManyToManyField(Hostel, related_name='categories', verbose_name="Hostels")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Hostel Category"
        verbose_name_plural = "Hostel Categories"
