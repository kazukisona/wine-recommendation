from django.urls import path
from . import views

urlpatterns = [
    path('api/wine/', views.WineListCreate.as_view()),
    path('api/user/', views.UserListCreate.as_view()),
    path('api/wines/', views.WineTableListCreate.as_view()),
    path('wine_list/', views.wine_list, name='wine_list')
]