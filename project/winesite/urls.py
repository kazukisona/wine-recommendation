from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/wine/', views.WineListCreate.as_view()),
    path('api/user/', views.UserListCreate.as_view()),
    path('api/wines/', views.WineTableListCreate.as_view()),
    path('recommendation/', views.recommendation, name='recommendation'),
    path('selector/', views.selector, name='selector'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('newuser', views.new_user, name='newuser'),
]