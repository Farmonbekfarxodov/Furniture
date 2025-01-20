from django.views.generic import TemplateView , ListView
from app_blogs.models import BlogCategoryModel, BlogModel, BlogTagModel

class HomeTemplateView(TemplateView):
    template_name = 'pages/home.html'

class BlogTemplateView(ListView):
    queryset = BlogModel.objects.filter()
    template_name = 'blog/blog-list-sidebar-left.html'
    context_object_name = 'blogs'


    def get_context_data(self, *,object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        blogs = self.get_queryset()
        tag = self.request.GET.get('tag')
        category = self.request.GET.get('category')

        if tag:
            blogs = blogs.filter(tags=tag)
        if category:
            blogs = blogs.filter(categories=category)

        context['blogs'] = blogs
        context["categories"] = BlogCategoryModel.objects.all()
        context["recent_blogs"] = BlogModel.objects.order_by('-created_at')[:2]
        context["tags"] = BlogTagModel.objects.all()
        return context

class ProductTemplateView(TemplateView):
    template_name = 'product/product-list-sidebar-left.html'
    

class ContactTemplateView(TemplateView):
    template_name = 'pages/contact.html'

class AboutTemplateView(TemplateView):
    template_name = 'pages/about-us.html'

class ErrorTemplateView(TemplateView):
    template_name = 'pages/404.html'
