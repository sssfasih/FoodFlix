from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('login', views.login,name='login'),
    path('signup', views.signup,name='signup'),
    path('drinks', views.drinks,name='drinks'),
    path('breakfast', views.breakfast,name='breakfast'),
    path('lunch', views.lunch,name='lunch'),
    path('dinner', views.lunch,name='dinner'),
]