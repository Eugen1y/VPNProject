from django.urls import path

from static.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),

]
