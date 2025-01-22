from django.views.generic import TemplateView

class ProductsTemplateView(TemplateView):
    template_name = 'product/product-grid-sidebar-left.html'

class ProductTemplateView(TemplateView):
    template_name = 'product/product-detail.html'