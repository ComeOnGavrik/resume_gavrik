from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView

# Create your views here.
def index(request):

    data = {
        'tittle': 'Главная страница!',
        'values': ['a', 'b', 'sfsfd'],
        'obj': {
            'car': 'BMW',
            'age': 27,
            'hobbie': 'football'
        }
    }

    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

#Регистрация пользователей