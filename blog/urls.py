from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='post_list'),
    path('<int:pk>/', views.PostView.as_view()),
]
