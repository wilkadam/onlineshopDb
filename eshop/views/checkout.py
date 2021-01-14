from django.contrib.auth.decorators import login_required
from django.contrib import messages
from eshop.models import Customer, Order, OrderProduct, Cart
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string

@login_required(login_url='/login')
def checkout(request):
    currentuser = request.user
    carts = Cart.objects.filter(user_id=currentuser.id)
    customer = Customer.objects.get(user_id=currentuser.id)
    myuser = User.objects.get(id=currentuser.id)

    total = 0
    qty = 0
    shipping = 14.99
    for cart in carts:
        total = total + cart.amount
        qty = qty + cart.qty
    
    grand_total = total + shipping

    if request.method == "POST":
        firstname = request.POST['Imię']
        lastname = request.POST['Nazwisko']
        phone = request.POST['Telefon']
        house_no = request.POST['Numer domu']
        street = request.POST['Ulica']
        city = request.POST['Miasto']
        postal_code = request.POST['Kod pocztowy']
        code = "OD-" + get_random_string(10).upper()

        order = Order(
            user_id = currentuser.id,
            first_name = firstname,
            last_name = lastname,
            phone = phone,
            house_no = house_no,
            street = street,
            city = city,
            postal_code = postal_code,
            total = grand_total,
            code = code
        )
        order.save()

        for cart in carts:
            orderpr = OrderProduct(
                order_id = order.id,
                user_id = currentuser.id,
                product_id = cart.product_id,
                qty = cart.qty,
                price = cart.product.price,
                amount = cart.amount
            )
            orderpr.save()
        
        Cart.objects.filter(user_id=currentuser.id).delete()
        messages.success(request, "Zamówienie zostało złożone")
        return redirect('ShopHome')
    
    details = {
        'myuser':myuser,
        'customer':customer,
        'carts':carts,
        'qty':qty,
        'total':total,
        'grand_total':grand_total,
        'shipping':shipping
    }
    
    return render(request, 'checkout.html', details)