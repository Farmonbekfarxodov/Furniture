from django.db.models import Q
from django.views.generic import ListView, DetailView

from app_products.models import (ProductManufactureModel,ProductCategoryModel,ProductColorModel,
                                ProductModel,ProductSizeModel,ProductTagModel)


class ProductListView(ListView):
    template_name = 'product/product-grid-sidebar-left.html'
    context_object_name = "products"
    paginate_by = 3

    def get_queryset(self):
        products = ProductModel.objects.all()
        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')
        tag = self.request.GET.get('tag')
        color = self.request.GET.get('color')
        size = self.request.GET.get('size')
        brand = self.request.GET.get('brand')
        sort = self.request.GET.get('sort')
        if q:
            products = products.filter(
                Q(title__icontains=q) | Q(short_description__icontains=q) |
                Q(long_description__icontains=q)
            )
        if cat:
            products = products.filter(categories=cat)
        if tag:
            products = products.filter(tags=tag)
        if color:
            products = products.filter(colors=color)
        if size:
            products = products.filter(sizes=size)
        if brand:
            products = products.filter(brands=brand)
        if sort:
            products = products.order_by(sort)
        return products

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sizes"] = ProductSizeModel.objects.all()
        context["colors"] = self.format_colors()
        context["categories"] = ProductCategoryModel.objects.all()
        context["brands"] = ProductManufactureModel.objects.all()
        context["tags"] = ProductTagModel.objects.all()
        context["products_count"] = ProductTagModel.objects.count()
        return context

    @staticmethod
    def format_colors():
        colors = ProductColorModel.objects.all()
        result = []
        temp_list = []

        for color in colors:
            temp_list.append(color)
            if len(temp_list) == 2:
                result.append(temp_list)
                temp_list = []

        if len(temp_list) == 1:
            result.append(temp_list)
        return result


class ProductDetailView(DetailView):
    template_name = 'product/product-detail.html'
    model = ProductModel
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        product = self.object

        categories = product.categories.all()

        related_products = ProductModel.objects.filter(categories__in=categories).exclude(id=product.id).distinct()

        context['related_products'] = related_products
        return context

