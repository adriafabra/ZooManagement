from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import *
from ZooWeb.forms import VisitorsForm

# Create your views here.

def homeView(req):
    animals = Animal.objects.order_by("species")
    workers = Worker.objects.order_by("name")
    sectors = Sector.objects.order_by("name")
    all_visitors = GroupOfVisitor.objects.order_by("date")
    group_of_visitor = []

    for group in all_visitors:
        if group.user.username == req.user.username:
            group_of_visitor.append(group)

    dic = {'Animals': animals, 'Workers': workers, 'Sectors': sectors, 'GroupOfVisitor': group_of_visitor}

    return render(req, 'home.html', dic)


class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj

class VisitorsUpdate(LoginRequiredMixin, CheckIsOwnerMixin, generic.UpdateView):
    template_name = 'form.html'

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class VisitorsCreate(LoginRequiredMixin, generic.CreateView):
    model = GroupOfVisitor
    template_name = 'form.html'
    form_class = VisitorsForm

    #Per crear el tour amb el current
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(VisitorsCreate, self).form_valid(form)

class VisitorsDetail(LoginRequiredMixin, CheckIsOwnerMixin, generic.DetailView):
    model = GroupOfVisitor
    template_name = 'visitors_detail.html'

    #def get_context_data(self, **kwargs):
     #   context = super(VisitorsDetail, self).get_context_data(**kwargs)
      #  return context