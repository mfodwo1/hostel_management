from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    username = models.CharField(max_length=100, null=True, unique=True)
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    student_id = models.CharField(max_length=50, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        if self.student_id:
           return f'{self.student_id}'
        else:
            return f'{self.username}'