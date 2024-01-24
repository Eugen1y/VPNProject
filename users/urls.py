from django.urls import path

from users.views import (UserSignUpView, UserLogoutView, UserLoginView,
                        UserProfileView, UserUpdateView, )

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserSignUpView.as_view(), name='register'),
    path('profile/<int:pk>', UserProfileView.as_view(), name='profile'),
    path('update-profile/', UserUpdateView.as_view(), name='update-profile')
]
