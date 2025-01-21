from django.views.generic import  ListView , DetailView
from app_blogs.models import BlogModel , BlogTagModel,BlogCategoryModel

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

class BlogDetailView(DetailView):
    model = BlogModel
    template_name = 'blog/blog-detail.html'
    context_object_name = 'blog'