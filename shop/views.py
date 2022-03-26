from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse
from shop.models import Product, Cart, Order


# Create your views here.
def accueil(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'shop/index.html', context)


def show(request, slug):
    product = Product.objects.get(slug=slug)
    context = {"product": product}
    return render(request, "shop/show.html", context)


def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    pannier, pan = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, ordered=False, product=product)
    if created:
        pannier.orders.add(order)
        pannier.save()
    else:
        order.quantity += 1
        order.save()
    return redirect(reverse("show", kwargs={"slug": slug}))


def panier(request):
    try:
        cart = get_object_or_404(Cart, user=request.user)
    except:
        return HttpResponse("<h1>Votre panier est vide</h1>")
    return render(request, 'shop/cart.html', context={"orders": cart.orders.all()})


def panier_delete(request):
    if cart := request.user.cart:
        cart.delete()
    return redirect('accueil')
