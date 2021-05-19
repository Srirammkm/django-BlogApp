from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.register),
    path('login/',views.view_login),
    path('logout/',views.logoutuser),
    path('home/<int:pk>/',views.home), 
    path('home/<int:pk>/profile/<int:up>/',views.profile , name='profile'),
    path('home/<int:pk>/createpost',views.createpost),
    path('home/<int:pk>/edit',views.editprofile),
    path('home/<int:pk>/deletepost/<int:pi>',views.deletepost),
    path('home/<int:pk>/editpost/<int:pi>',views.editpost),
]
