from django.urls import path

from .views import RegistrationAndLogin


urlpatterns = [
    path('registration_and_login/', RegistrationAndLogin.as_view(),
         name='reg_and_log'),
]
