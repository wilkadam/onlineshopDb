from django.contrib.auth.decorators import login_required
from django.contrib import messages
from eshop.models import Product, Wishlist
from django.http.response import HttpResponseRedirect

@login_required(login_url='/login')
def addtowishlist(request, prid):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    wishlist = Wishlist(
        user_id = current_user.id,
        product_id = prid
    )
    wishlist.save()
    messages.success(request, wishlist.product.product_name + " został dodany do listy życzeń.")
    return HttpResponseRedirect(url)

@login_required(login_url='/login')
def removefromwishlist(request, prid):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    product = Product.objects.get(id=prid)
    Wishlist.objects.get(user_id = current_user.id, product_id = prid).delete()
    messages.success(request, product.product_name + " został usunięty z listy życzeń.")
    return HttpResponseRedirect(url)