from django.shortcuts import redirect, render , get_object_or_404
from shop.models import Coffee
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, coffee_id):
    coffee = Coffee.objects.get(id=coffee_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    try:
        cart_item = CartItem.objects.get(coffee=coffee, cart=cart)
        if (cart_item.quantity < cart_item.coffee.stock):
            cart_item.quantity +=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(coffee=coffee, quantity=1,cart=cart)
    return redirect('cart:cart_detail')

def cart_detail(request, total=0, counter=0, cart_items = None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.coffee.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html',
                    {'cart_items':cart_items,
                    'total':total,
                    'counter':counter
                    })


def cart_remove(request, coffee_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    coffee = get_object_or_404(Coffee, id=coffee_id)
    cart_item = CartItem.objects.get(coffee=coffee, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')



def full_remove(request, coffee_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    coffee = get_object_or_404(Coffee, id=coffee_id)
    cart_item = CartItem.objects.get(coffee=coffee, cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')