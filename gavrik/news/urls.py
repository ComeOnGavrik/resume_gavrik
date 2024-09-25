from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.AddNews.as_view(), name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete')
]
