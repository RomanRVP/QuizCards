from django.urls import path

from .views import RegistrationAndLogin, UserLogOut


urlpatterns = [
    path('registration_and_login/', RegistrationAndLogin.as_view(),
         name='reg_and_log'),
    path('user_logout', UserLogOut.as_view(), name='user_logout'),
]
