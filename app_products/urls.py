from django.urls import path

from app_products import views
app_name = "products"

urlpatterns = [
    path('product/',views.ProductDetailView.as_view(),name='product'), 
    path('',views.ProductsListView.as_view(),name='list'),
]