from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import *
from ZooWeb.forms import VisitorsForm

# Create your views here.

def homeView(req):
    animals = Animal.objects.order_by("species")
    workers = Worker.objects.order_by("name")
    sectors = Sector.objects.order_by("name")
    group_of_visitor = GroupOfVisitor.objects.order_by("date")

    dic = {'Animals': animals, 'Workers': workers, 'Sectors': sectors, 'GroupOfVisitor': group_of_visitor}

    return render(req, 'home.html', dic)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class VisitorsCreate(generic.CreateView):
    model = GroupOfVisitor
    template_name = 'form.html'
    form_class = VisitorsForm