from django.urls import path, include

from .views import HomePage


urlpatterns = [
    path('', HomePage.as_view(), name='main_page'),
    path('api/', include('quizcard.api.urls'))
]
