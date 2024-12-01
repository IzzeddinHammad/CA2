from django.shortcuts import redirect, render, get_object_or_404
from shop.models import Coffee
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.http import JsonResponse

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, coffee_id):
    coffee = get_object_or_404(Coffee, id=coffee_id)

    # Check if it's an AJAX request
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
        except Cart.DoesNotExist:
            cart = Cart.objects.create(cart_id=_cart_id(request))
            cart.save()

        try:
            cart_item = CartItem.objects.get(coffee=coffee, cart=cart)
            if cart_item.quantity < coffee.stock:
                cart_item.quantity += 1
                cart_item.save()
                coffee.stock -= 1
                coffee.save()
                return JsonResponse({
                    'success': True,
                    'message': f'{coffee.name} was added to your cart.'
                })
            else:
                return JsonResponse({
                    'success': False,
                    'message': f'Sorry, {coffee.name} is out of stock.'
                })
        except CartItem.DoesNotExist:
            if coffee.stock > 0:
                cart_item = CartItem.objects.create(
                    coffee=coffee,
                    quantity=1,
                    cart=cart
                )
                coffee.stock -= 1
                coffee.save()
                return JsonResponse({
                    'success': True,
                    'message': f'{coffee.name} was added to your cart.'
                })
            else:
                return JsonResponse({
                    'success': False,
                    'message': f'Sorry, {coffee.name} is out of stock.'
                })

    # Handle non-AJAX requests
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

    try:
        cart_item = CartItem.objects.get(coffee=coffee, cart=cart)
        if cart_item.quantity < coffee.stock:
            cart_item.quantity += 1
            messages.success(request, f'{coffee.name} was added to your cart.')
        else:
            messages.warning(request, f'Sorry, {coffee.name} is out of stock.')
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(coffee=coffee, quantity=1, cart=cart)
        messages.success(request, f'{coffee.name} was added to your cart.')

    return redirect(request.META.get('HTTP_REFERER', 'shop:all_products'))

def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.coffee.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total,
        'counter': counter
    })