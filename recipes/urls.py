from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('login', views.login_view,name='login'),
    path('logout', views.logout_view,name='logout'),
    path('signup', views.signup,name='signup'),
    path('category/<str:cat>',views.category,name='category'),
    path('categories',views.all_categories,name='all_category'),
    path('recipe/<str:name>',views.view_recipe,name='view_recipe'),
    path('add_recipe',views.add_recipe,name='add_recipe'),

]