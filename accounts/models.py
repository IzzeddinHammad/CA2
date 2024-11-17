from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

# Create your models here.
class Customer(AbstractUser):
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    age = models.PositiveIntegerField(null=True, blank=True)