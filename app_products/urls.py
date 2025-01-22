from django.urls import path

from app_products import views
app_name = "products"

urlpatterns = [
    path('product/',views.ProductTemplateView.as_view(),name='product'), 
    path('',views.ProductsTemplateView.as_view(),name='products'),
]