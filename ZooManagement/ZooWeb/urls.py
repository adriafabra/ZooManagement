from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
from .views import *


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('', views.homeView, name='home'),
    path('groupofvisitors/create', 
        VisitorsCreate.as_view(),
        name='visitors_create'),
    
    path('groupofvisitors/<int:pk>',
        VisitorsDetail.as_view(),
        name='visitors_detail'),

    path('groupofvisitors/<int:pk>/edit',
        VisitorsUpdate.as_view(
            model=GroupOfVisitor,
            form_class=VisitorsForm),
        name='visitors_edit'),
]