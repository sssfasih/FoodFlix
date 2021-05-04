from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('login', views.login_view,name='login'),
    path('logout', views.logout_view,name='logout'),
    path('signup', views.signup,name='signup'),
    path('category/<str:cat>',views.category,name='category'),
    path('categories',views.all_categories,name='all_categories'),
    path('recipe/<str:name>',views.view_recipe,name='view_recipe'),
    path('add_recipe',views.add_recipe,name='add_recipe'),
    path('view_profile',views.view_profile,name='view_profile'),
    path('recipe_addfav/<int:id>',views.recipe_addfav,name='recipe_addfav'),
    path('recipe_remfav/<int:id>',views.recipe_remfav,name='recipe_remfav'),
    path('recipe_edit/<int:id>',views.recipe_edit,name='recipe_edit'),

]