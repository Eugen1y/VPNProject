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


