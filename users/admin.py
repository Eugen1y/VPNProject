from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.forms import UserSignUpForm, UserProfileUpdateForm
from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = UserSignUpForm
    form = UserProfileUpdateForm
    model = CustomUser
    list_display = ['email', 'username',]