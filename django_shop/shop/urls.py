from django.urls import path

from . import views


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('accounts/registration', views.registration, name='registration')
]