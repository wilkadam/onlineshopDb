"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index, signup, login, details, products, cartoptions, buynow, checkout, logout, cart, account, productdetail, wishlist
from .views import search, updateprofile, changepassword, cancelproduct

urlpatterns = [
    path("", index.index, name="ShopHome"),
    path("signup/", signup.Signup.as_view(), name="SignUp"),
    path("login/", login.Login.as_view(), name="LogIn"),
    path("products/", products.products, name="Products"),
    path("search/", search.search, name="Search"),
    path("details/<int:prid>", details.details, name="Details"),
    path("addtocart/<int:prid>", cartoptions.addtocart, name="AddtoCart"),
    path("buynow/<int:prid>", buynow.buynow, name="BuyNow"),
    path("productdetail/<int:prid>", productdetail.productdetail, name="ProductDetail"),
    path("deletefromcart/<int:prid>", cartoptions.deletefromcart, name="DeletefromCart"),
    path("deleteallfromcart/<int:prid>", cartoptions.deleteallfromcart, name="DeleteAllfromCart"),
    path("addtowishlist/<int:prid>", wishlist.addtowishlist, name="AddfromWishlist"),
    path("cart/", cart.cart, name="Cart"),
    path("clearcart/", cartoptions.clearcart, name="ClearCart"),
    path("checkout/", checkout.checkout, name="CheckOut"),
    path("cancelproduct/<int:orid>/<int:prid>", cancelproduct.cancelProduct, name="CancelProduct"),
    path("account/", account.account, name="Account"),
    path("account/updateprofile/", updateprofile.updateprofile, name="UpdateProfile"),
    path("account/changepassword/", changepassword.changepassword, name="ChangePassword"),
    path("logout/", logout.logout_view, name="Logout")
]