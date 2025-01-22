
from django.views.generic import TemplateView,CreateView
from django.contrib import messages
from django.shortcuts import redirect


from pages.forms import ContactModelForm
from pages.models import ContactModel


class HomeTemplateView(TemplateView):
    template_name = 'pages/home.html'


class ContactCreateView(CreateView):
    template_name = 'pages/contact.html'
    form_class = ContactModelForm
    model = ContactModel
    success_url = "/contact"

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Muvaffaqiyatli o'tdingiz")
        return redirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, "Formani to'ldirishda muammo yuz berdi")
        return self.render_to_response(self.get_context_data(form=form))




class AboutTemplateView(TemplateView):
    template_name = 'pages/about-us.html'

class ErrorTemplateView(TemplateView):
    template_name = 'pages/404.html'
