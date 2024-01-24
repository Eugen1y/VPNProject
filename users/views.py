from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic.base import View, TemplateView

from users.forms import UserSignUpForm, UserProfileUpdateForm
from users.models import CustomUser
from website.views import SiteCreateView, SiteListView


class UserSignUpView(CreateView):
    """User sign up view implementation"""

    template_name = "registration/sign-up.html"
    form_class = UserSignUpForm
    success_url = reverse_lazy("login")


class UserLoginView(LoginView):
    """User login view implementation"""

    def get_success_url(self):
        """Return an URL to redirect to"""

        return self.request.GET.get("next") or reverse_lazy("home")


class UserLogoutView(View):
    """User logout view implementation"""

    def get(self, *args, **kwargs):
        """Handle GET request"""

        logout(self.request)

        redirect_url = reverse_lazy("home")
        return HttpResponseRedirect(redirect_url)


class UserProfileView(LoginRequiredMixin, TemplateView):
    """"User profile view implementation"""

    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_site_form'] = SiteCreateView.form_class()
        context['site_list'] = SiteListView.model.objects.filter(user=self.request.user)
        return context

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'update_profile.html'
    form_class = UserProfileUpdateForm
    success_url = reverse_lazy('profile')

    def get_object(self):
        return CustomUser.objects.get(pk=self.request.user.pk)



