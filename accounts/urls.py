from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginPage.as_view(), name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.RegisterPage.as_view(), name='register'),
    path('', views.index, name='index'),
]
