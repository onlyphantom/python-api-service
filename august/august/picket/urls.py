from django.urls import path

from . import views

urlpatterns = [
    path('api', views.home, name='index'),
    path('signup', views.signup, name='signup')
]