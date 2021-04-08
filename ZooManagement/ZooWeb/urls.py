from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
from .views import SignUpView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('', views.homeView, name='home'),
]