from django.urls import path
from .views import (UserProfileUpdateView, UserRegistrationView, UserLoginView,
                    UserLogoutView, UserProfileView,
                    ChangePasswordView, DeleteAccountView,
                    PasswordResetRequestView, PasswordResetConfirmView)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profile/update/', UserProfileUpdateView.as_view(), name='user-profile-update'),
    path('password/change/', ChangePasswordView.as_view(), name='change-password'),
    path('password/reset/', PasswordResetRequestView.as_view(),
         name='reset-password'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(),
         name='reset-password-confirm'),
    path('user/delete/', DeleteAccountView.as_view(), name='delete-account'),
]

