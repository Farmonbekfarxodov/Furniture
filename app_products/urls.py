from django.urls import path

from app_products import views
app_name = "products"

urlpatterns = [
    path('<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    path('',views.ProductListView.as_view(),name='list'),
]