from django.shortcuts import render
from eshop.models import Customer, Product, Cart, Wishlist

def details(request, prid):
    current_user = request.user
    product = Product.objects.get(id=prid)
    carts = Cart.objects.filter(user_id=current_user.id)
    wishlist = Wishlist.objects.filter(user_id=current_user.id, product_id=prid)

    customer = []
    try:
        customer = Customer.objects.get(user_id=current_user.id)
    except:
        pass

    try:
        product_quantity = Cart.objects.get(user_id=current_user.id, product_id=prid)
        product_quantity = product_quantity.qty
    except:
        product_quantity = 0


    desc = product.description
    descs = list(desc.split("#"))

    qty = 0
    total = 0
    for cart in carts:
        total = total + cart.amount
        qty = qty + cart.qty
    
    details = {
        'customer':customer,
        'product':product,
        'descs':descs,
        'qty':qty,
        'total':total,
        'carts':carts,
        'wishlist':wishlist,
        'product_quantity':product_quantity
    }
    
    return render(request, 'productdetail.html', details)