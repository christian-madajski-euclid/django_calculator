from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check_login/', views.check_login, name='check_login'),
    path('register/', views.register, name='register'),
    path('check_register/', views.check_register, name='check_register'),
    path('logout/', views.logout, name="logout")
]
