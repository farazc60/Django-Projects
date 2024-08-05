from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_id = request.session.get('cart_id')
    if not cart_id:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
    else:
        cart = get_object_or_404(Cart, id=cart_id)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('cart:cart_detail')

def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if request.method == 'POST':
        cart_item.quantity = int(request.POST.get('quantity', 1))
        cart_item.save()
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart_id = request.session.get('cart_id')
    if not cart_id:
        return render(request, 'cart_detail.html', {'cart': None, 'total_price': 0})

    cart = get_object_or_404(Cart, id=cart_id)
    total_price = sum(item.total_price() for item in cart.cartitem_set.all())

    return render(request, 'cart_detail.html', {'cart': cart, 'total_price': total_price})

def remove_from_cart(request, product_id):
    cart_id = request.session.get('cart_id')
    cart = get_object_or_404(Cart, id=cart_id)
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
    cart_item.delete()
    return redirect('cart:cart_detail')
