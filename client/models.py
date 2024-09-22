from django.db import models
from authentication.models import User


class Hostel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Hostel Name")
    location = models.CharField(max_length=255, verbose_name="Location")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(
        upload_to='hostel_images/', verbose_name="Hostel Image", default='hostel_images/default.jpg')
    price = models.DecimalField(
        max_digits=10, decimal_places=2,verbose_name="Price")
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Hostel"
        verbose_name_plural = "Hostels"


class Favorite(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='favorites', verbose_name="User")
    hostel = models.ForeignKey(
        Hostel, on_delete=models.CASCADE, related_name='favorites', verbose_name="Hostel")

    def __str__(self):
        return f'Favorite by {self.user.username} for {self.hostel.name}'

    class Meta:
        verbose_name = "Favorite"
        verbose_name_plural = "Favorites"
        unique_together = ('user', 'hostel')


class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings', verbose_name="User")
    hostel = models.ForeignKey(
        Hostel, on_delete=models.CASCADE, related_name='bookings', verbose_name="Hostel")
    check_in_date = models.DateField(verbose_name="Check-in Date")
    check_out_date = models.DateField(verbose_name="Check-out Date")

    def __str__(self):
        return f'Booking by {self.user.username} for {self.hostel.name}'

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        unique_together = ('user', 'hostel', 'check_in_date')


class Review(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews', verbose_name="User")
    hostel = models.ForeignKey(
        Hostel, on_delete=models.CASCADE, related_name='reviews', verbose_name="Hostel")
    rating = models.IntegerField(verbose_name="Rating")
    comment = models.TextField(verbose_name="Comment")

    def __str__(self):
        return f'Review by {self.user.username} for {self.hostel.name}'

    def save(self, *args, **kwargs):
        if not 1 <= self.rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        unique_together = ('user', 'hostel')
