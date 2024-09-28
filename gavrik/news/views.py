from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView


# Create your views here.
def news_home(request):
    news = Articles.objects.order_by('-date')
    tittle = 'Новости на сайте'
    return render(request, 'news/news_home.html', {'news': news, 'tittle': tittle})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'


class AddNews(LoginRequiredMixin, CreateView):
    form_class = ArticlesForm
    template_name = 'news/create.html'
    success_url = reverse_lazy('news_home')

    def form_valid(self, form1):
        n = form1.save(commit = False)
        n.author = self.request.user

        return super().form_valid(form1)
