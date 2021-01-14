from eshop.models import Customer, Cart
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='/login')
def cart(request):
    current_user = request.user
    customer = Customer.objects.get(user_id=current_user.id)
    carts = Cart.objects.filter(user_id=current_user.id)

    total = 0
    qty = 0
    shipping = 14.99
    for cart in carts:
        total = total + cart.amount
        qty = qty + cart.qty
    

    grand_total = total + shipping
    
    cart = {
        'customer':customer,
        'carts':carts,
        'qty':qty,
        'total':total,
        'grand_total':grand_total,
        'shipping':shipping,
    }
    
    return render(request, 'cart.html', cart)