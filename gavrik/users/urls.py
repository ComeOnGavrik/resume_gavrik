from . import views
from django.urls import path, include

app_name = 'users'

urlpatterns = [
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.RegisterUser.as_view(), name='register')
]
