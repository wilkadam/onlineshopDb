from django.contrib import messages
from django.http.response import HttpResponseRedirect
from eshop.models import OrderProduct


def cancelProduct(request, orid, prid):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    product = OrderProduct.objects.get(order_id=orid, user_id=current_user.id, product_id=prid)
    product.status = 'Anulowany'
    product.save()
    messages.success(request, product.product.product_name + " został anulowany")
    return HttpResponseRedirect(url)
