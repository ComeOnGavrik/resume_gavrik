from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from .models import CustomUser
from .forms import CustomUserChangeForm

from .forms import LoginUserForm, RegisterUserForm
from django.contrib import messages


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'tittle': 'Авторизация'}


def logout_user(request):
    logout(request)
    return redirect('users:login')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'tittle': 'Регистрация'}
    success_url = reverse_lazy('users:login')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user_orders'] = self.request.user.orders.all()
    #     return context


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'users/edit_profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user