from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings



urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('product/',include('app_products.urls',namespace='products')),
    path('', include('pages.urls', namespace='pages')),

)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
