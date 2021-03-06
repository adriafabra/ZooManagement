from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import *
from django.core.exceptions import PermissionDenied
from ZooWeb.forms import VisitorsForm
from django.shortcuts import get_object_or_404

# Create your views here.

def homeView(req):
    animals = Animal.objects.order_by("classes")
    workers = Worker.objects.order_by("name")
    sectors = Sector.objects.order_by("name")
    all_visitors = GroupOfVisitor.objects.order_by("date")
    group_of_visitor = []

    for group in all_visitors:
        if group.user.username == req.user.username:
            group_of_visitor.append(group)

    dic = {'Animals': animals, 'Workers': workers, 'Sectors': sectors, 'GroupOfVisitor': group_of_visitor}

    return render(req, 'home.html', dic)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

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

class VisitorsCreate(LoginRequiredMixin, generic.CreateView):
    model = GroupOfVisitor
    template_name = 'form.html'
    form_class = VisitorsForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(VisitorsCreate, self).form_valid(form)

class VisitorsUpdate(LoginRequiredMixin, CheckIsOwnerMixin, generic.UpdateView):
    template_name = 'form.html'

class VisitorsDelete(LoginRequiredMixin, CheckIsOwnerMixin, generic.DeleteView):
    model = GroupOfVisitor
    success_url = reverse_lazy('home')

class VisitorsDetail(LoginRequiredMixin, CheckIsOwnerMixin, generic.DetailView):
    model = GroupOfVisitor
    template_name = 'visitors_detail.html'
