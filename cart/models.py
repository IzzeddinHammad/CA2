from shop.models import Coffee
from django.db import models

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.coffee.price * self.quantity

    def __str__(self):
        return self.coffee
