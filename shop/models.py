from django.db import models
from django.urls import reverse
from uuid import uuid4
# Create your models here.


class coffee(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    price = models.PositiveIntegerField()






    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('coffee_detail',args=[str(self.id)])