import re
from urllib.parse import urlparse, urljoin

import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Site
from .forms import SiteForm


class SiteCreateView(CreateView):
    model = Site
    form_class = SiteForm
    template_name = 'create_site.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})

    def post(self, request, *args, **kwargs):
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
    def get(self, request, user_site_name, original_path, *args, **kwargs):

        content = self.get_content(original_path)
        domain = self.find_domain(original_path)
        if content:
            modified_content = self.replace_links(content, domain, user_site_name, 'http://127.0.0.1:8000')
            return render(request, 'proxy_site.html', {'content': modified_content})
        else:
            return render(request, 'proxy_site.html', {'content': 'Content not found'})

    def find_domain(self, url):
        if 'https' not in url:
            url = 'https://' + url
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        return domain

    def modify_content(self, html_content, user_site, user_site_name):
        # ищем все линки
        regex = r'href=["\'](https?://\S+?)["\']'
        selectors = ['.js', '.css']
        domain = self.find_domain(user_site)
        # находим ссылки которые надо заменить
        links_to_replace = []
        links = re.findall(regex, html_content)
        for link in links:
            for selector in selectors:
                if selector in link:
                    continue
                else:
                    links_to_replace.append(link)
        for item in links_to_replace:
            if domain in item:
                new_item = item.replace(domain, f'//localhost/{user_site_name}/{domain}')
                html_content = html_content.replace(item, new_item)
        return html_content

    def replace_links(self, html_content, domain, user_site_name, base_url):
        soup = BeautifulSoup(html_content, 'html.parser')

        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']

            # Проверяем, содержит ли ссылка указанный домен
            if domain in href:
                # Заменяем домен в ссылке, используя urljoin
                new_href = urljoin(base_url, f'{user_site_name}/{domain}{urlparse(href).path}')
                a_tag['href'] = new_href
            elif href.startswith('/'):
                new_href = urljoin(base_url, f'{user_site_name}/{domain}{urlparse(href).path}')
                a_tag['href'] = new_href
        return str(soup)

    def get_content(self, url):
        try:
            if 'https' not in url:
                url = 'https://' + url
            headers = {
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', }
            response = requests.get(url, headers=headers)
            content = response.text

            return content
        except requests.exceptions.RequestException as e:
            # обработка ошибок
            print(f"Error retrieving content for {url}: {e}")
            return None
