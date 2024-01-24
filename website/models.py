import time
from urllib.parse import urlparse

import requests
from django.core.validators import URLValidator
from django.db import models
from selenium import webdriver

from users.models import CustomUser


class Site(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.name
    def get_content(self):
        try:
            driver = webdriver.Chrome()
            # Використовуйте бібліотеку requests для отримання вмісту зовнішнього сайту
            response = driver.get(self.url)
            time.sleep(3)
            response.raise_for_status()  # Викидає виняток, якщо отримано неприпустимий код статусу

            # Повертаємо вміст зовнішнього сайту
            return response.text
        except requests.exceptions.RequestException as e:
            # Обробка помилок під час отримання вмісту
            print(f"Error retrieving content for {self.name}: {e}")
            return None
