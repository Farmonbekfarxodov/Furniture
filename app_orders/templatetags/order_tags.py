from django import template

from app_products.models import ProductModel

register = template.Library()


@register.filter
def in_cart(request, pk):
    return pk in request.session.get('cart', [])


@register.simple_tag
def get_user_cart(request):
    cart = request.session.get('cart', [])
    products = []
    for pk in cart:
        product = ProductModel.objects.get(id=pk)
        products.append(product)

    return products

@register.simple_tag
def total_sum_in_cart(request):
    cart = request.session.get('cart',[])
    products = ProductModel.objects.filter(id__in=cart)
    summ = 0

    for product in products:
        summ += product.price

    return summ

@register.filter
def in_wishlist(request,pk):
    return pk in request.session.get('wishlist',[])


@register.simple_tag
def get_user_wishlist(request):
    wishlist  = request.session.get('wishlist',[])
    products = ProductModel.objects.filter(id__in=wishlist)

    return products
