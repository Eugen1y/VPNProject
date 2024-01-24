from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from slugify import slugify

from .models import Site
from .forms import SiteForm


class SiteCreateView(CreateView):
    model = Site
    form_class = SiteForm
    template_name = 'create_site.html'

    # Замініть 'user_profile' на URL вашого профілю користувача

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})

    def post(self, request, *args, **kwargs):
        # Викликати метод form_valid для обробки POST-запиту
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class SiteListView(ListView):
    model = Site
    template_name = 'site_list.html'
    context_object_name = 'sites'


class SiteUpdateView(UpdateView):
    model = Site
    form_class = SiteForm
    template_name = 'update_site.html'
    success_url = reverse_lazy('site_list')


class SiteDeleteView(DeleteView):
    model = Site
    template_name = 'delete_site.html'
    success_url = reverse_lazy('site_list')


class ProxySiteView(View):
    def get(self, request, user_site_name, *args, **kwargs):

        # Отримати дані сайту користувача за ім'ям
        user_site = get_object_or_404(Site, name=user_site_name)

        # Замініть атрибути посилань на внутрішній роут
        content = user_site.get_content()  # Ваш метод отримання контенту зовнішнього сайту
        if content:
            modified_content = content.replace('href="', f'href="/localhost/{user_site_name}/')
            return render(request, 'proxy_site.html', {'content': modified_content})
        else:
            # Обробити випадок, коли вміст не знайдено
            return render(request, 'proxy_site.html', {'content': 'Content not found'})

class RedirectOriginalSiteView(View):
    def get(self, request, user_site_name, original_path, *args, **kwargs):
        # Отримати дані сайту користувача за ім'ям
        user_site = Site.objects.get(name=user_site_name)

        # Створити повний URL оригінального сайту
        original_url = f'{user_site.external_url}/{original_path}'

        # Перенаправити користувача на оригінальний сайт
        return redirect(original_url)
