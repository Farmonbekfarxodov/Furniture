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
