
from django.urls import path

from pages import views
app_name = "pages"

urlpatterns = [
    path('contact/',views.ContactCreateView.as_view(),name='contact'),
    path('about/',views.AboutTemplateView.as_view(),name='about'),
    path('error/',views.ErrorTemplateView.as_view(),name='error'),
    path('',views.HomeTemplateView.as_view(),name='home'),
]