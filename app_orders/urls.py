from django.urls import path

from app_orders.views import add_or_remove_cart, UserCartListView, CheckoutFormView,add_or_remove_wishlist,WishlistListView

app_name = "orders"

urlpatterns = [
    path('cart/', UserCartListView.as_view(), name='cart'),
    path('checkout/', CheckoutFormView.as_view(), name='checkout'),
    path('wishlist/', WishlistListView.as_view(), name='wishlist'),
    path('cart/add-or-remove/<int:pk>/', add_or_remove_cart, name='add-or-remove-cart'),
    path('wishlist/add-or-remove/<int:pk>/', add_or_remove_wishlist, name='add-or-remove-wishlist'),
]
