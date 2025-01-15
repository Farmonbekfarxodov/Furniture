
from django.urls import path

from pages import views
app_name = "pages"

urlpatterns = [
    path('blog/',views.BlogTemplateView.as_view(),name='blog'),
    path('product/',views.ProductTemplateView.as_view(),name='product'),
    path('contact/',views.ContactTemplateView.as_view(),name='contact'),
    path('about/',views.AboutTemplateView.as_view(),name='about'),
    path('error/',views.ErrorTemplateView.as_view(),name='error'),
    path('',views.HomeTemplateView.as_view(),name='home'),
]