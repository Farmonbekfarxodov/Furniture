from django.urls import path

from pages import views
app_name = "app_products"

urlpatterns = [
    path('',views.ProductTemplateView.as_view(),name='product'),
]