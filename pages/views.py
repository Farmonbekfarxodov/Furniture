from django.views.generic import TemplateView
class HomeTemplateView(TemplateView):
    template_name = 'pages/home.html'

class ProductTemplateView(TemplateView):
    template_name = 'product/product-list-sidebar-left.html'
    

class ContactTemplateView(TemplateView):
    template_name = 'pages/contact.html'

class AboutTemplateView(TemplateView):
    template_name = 'pages/about-us.html'

class ErrorTemplateView(TemplateView):
    template_name = 'pages/404.html'
