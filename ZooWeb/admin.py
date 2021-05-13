from django.contrib import admin

# Register your models here.

from .models import Animal, Worker, Sector, GroupOfVisitor, GuidedTour

admin.site.register(Animal)
admin.site.register(Worker)
admin.site.register(Sector)
admin.site.register(GroupOfVisitor)
admin.site.register(GuidedTour)