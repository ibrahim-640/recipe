from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('', views.recipe_list, name='list'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='detail'),
    path('new/', views.recipe_create, name='create'),
    path('<int:pk>/edit/', views.recipe_update, name='update'),
    path('<int:pk>/delete/', views.recipe_delete, name='delete'),
    path('logout/',views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('search/', views.search_recipes, name='search'),
]
