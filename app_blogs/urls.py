from django.urls import path

from app_blogs import views

app_name = "blogs"

urlpatterns = [
    path('<int:pk>/',views.BlogDetailView.as_view(),name='detail'),
    path('', views.BlogTemplateView.as_view(), name='blog'),
    
]