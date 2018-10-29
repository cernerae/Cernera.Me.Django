from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'personal'
urlpatterns = [
    path('', TemplateView.as_view(template_name="personal/about.html"), name='about')
]
