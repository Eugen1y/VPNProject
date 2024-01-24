from django.urls import path
from .views import SiteCreateView, ProxySiteView, RedirectOriginalSiteView

urlpatterns = [
    path('create-site/', SiteCreateView.as_view(), name='create_site'),
    path('<str:user_site_name>/<path:original_path>', ProxySiteView.as_view(), name='proxy_site'),
    path('redirect/<str:user_site_name>/<path:original_path>/', RedirectOriginalSiteView.as_view(),
         name='redirect_original_site'),
]
