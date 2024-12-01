from django.db import models
from django.urls import reverse
import uuid
# Create your models here.

class Coffee(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    cover = models.ImageField(upload_to='coffee_covers/',blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'coffee'
        verbose_name_plural = 'Coffee'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:coffee_detail',args=[str(self.id)])