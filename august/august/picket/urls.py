from django.urls import path

# from . import views
from picket.views import home, signup

urlpatterns = [
    path('api', home, name='index'),
    path('signup', signup, name='signup'),
]
