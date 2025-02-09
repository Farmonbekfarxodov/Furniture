from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from app_orders.forms import CheckoutForm
from app_orders.models import OrderModel, OrderItem
from app_products.models import ProductModel


def add_or_remove_cart(request, pk):
    cart: list = request.session.get('cart', [])
    if pk in cart:
        cart.remove(pk)
    else:
        cart.append(pk)

    request.session["cart"] = cart
    next_url = request.GET.get('next', reverse_lazy('products:list'))
    return redirect(next_url)


def add_or_remove_wishlist(request, pk):
    wishlist = request.session.get('wishlist',[])
    if pk in wishlist:
        wishlist.remove(pk)
    else:
        wishlist.append(pk)
    
    next_url = request.GET.get('next',reverse_lazy('product:product-grid-sidebar-left.html'))
    request.session['wishlist'] = wishlist
    return redirect(next_url)

class WishlistListView(ListView):
    template_name = 'product/user-wishlist.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        wishlist = self.request.session.get('wishlist',[])

        products = ProductModel.objects.filter(id__in=wishlist)

        return products


class UserCartListView(ListView):
    template_name = "product/product-cart.html"
    context_object_name = "products"
    paginate_by = 10

    def get_queryset(self):
        cart = self.request.session.get('cart', [])
        products = ProductModel.objects.filter(id__in=cart)
        return products

class CartListView(ListView):
    template_name = 'product/product-cart.html'
    context_object_name =  'products'
    paginate_by = 10

    def get_queryset(self):
        cart = self.request.session.get('cart',[])
        products = ProductModel.objects.filter(id__in=cart)

        return products

def calculate_price(products):
    total = 0
    for product in products:
        total += product.price
        return total


class CheckoutFormView(LoginRequiredMixin, FormView):
    template_name = "product/product-checkout.html"
    form_class = CheckoutForm
    success_url = reverse_lazy("users:account")

    def calculate_total_price(self, products):
        total = 0
        for product in products:
            total += product.price
        return total

    def form_valid(self, form):
        user = self.request.user
        cart = self.request.session.get('cart', [])
        products = ProductModel.objects.filter(id__in=cart)
        if len(products) == 0:
            messages.info(self.request, "Add some products")
            return redirect(reverse_lazy("products:list"))
        else:
            order = OrderModel.objects.create(
                user=user,
                status=False,
                total_amount=self.calculate_total_price(products),
                total_product=len(products)
            )
            for product in products:
                product_info = ProductModel.objects.get(id=product.id)
                OrderItem.objects.create(
                    order=order,
                    quantity=1,
                    product=product,
                    product_name=product_info.title,
                    product_price=product_info.price
                )
            self.request.session["cart"] = []
            return redirect(reverse_lazy("users:account"))

    def form_invalid(self, form):
        return super().form_invalid(form)
