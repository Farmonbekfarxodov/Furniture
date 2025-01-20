from django.views.generic import TemplateView

class ProductsTemplateView(TemplateView):
    template_name = 'product/product-list-sidebar-left.html'