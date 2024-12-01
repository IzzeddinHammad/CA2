from django.db import models
from django.urls import reverse
import uuid
# Create your models here.

class Coffee(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    price = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'coffee'
        verbose_name_plural = 'Coffee'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:home',args=[str(self.id)])