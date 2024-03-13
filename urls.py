from django.urls import path
from greetings import views


urlpatterns = [
    path('', views.home, name='home'),
]