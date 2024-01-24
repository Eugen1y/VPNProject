from urllib.parse import urlparse

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.forms import URLField

from .models import Site


class SiteForm(forms.ModelForm):
    url = forms.CharField()

    class Meta:
        model = Site
        fields = ['name', 'url']

    def clean_url(self):
        url = self.cleaned_data.get('url')

        # Додайте префікс, якщо його немає
        if not urlparse(url).scheme:
            url = 'http://' + url

        return url