from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
from .views import *


urlpatterns = [
    path('', views.homeView, name='home'),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
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

    path('groupofvisitors/<int:pk>/delete', 
        VisitorsDelete.as_view(
            model = GroupOfVisitor,
            template_name = 'confirm_delete.html',
        ),
        name='visitors_delete'),
        
]