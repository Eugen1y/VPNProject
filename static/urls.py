from django.urls import path

from static.views import Home, About, Contacts

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('contacts/', Contacts.as_view(), name='contacts')
]
