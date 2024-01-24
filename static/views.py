from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'static/home.html'


class About(TemplateView):
    template_name = 'static/about.html'


class Contacts(TemplateView):
    template_name = 'static/contacts.html'
