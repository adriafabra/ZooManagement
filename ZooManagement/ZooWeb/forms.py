from django.forms import ModelForm
from ZooWeb.models import GroupOfVisitor

class VisitorsForm(ModelForm):
    class Meta:
        model = GroupOfVisitor
        exclude = ()