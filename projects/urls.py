from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'projects'
urlpatterns = [
    path('', TemplateView.as_view(template_name="projects/projects.html"), name='projects')
]