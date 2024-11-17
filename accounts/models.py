from django.contrib.auth.models import AbstractUser
from django.db import models

class Customer(AbstractUser):
    age = models.PositiveBigIntegerField(null=True, blank=True)