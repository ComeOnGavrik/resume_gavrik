from . import views
from django.urls import path, include
from .views import ProfileView, EditProfileView

app_name = 'users'

urlpatterns = [
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.RegisterUser.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name='edit_profile'),
]
