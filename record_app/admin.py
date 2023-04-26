from django.contrib import admin
from .models import Employees, Files, Incoming, Outgoing

# Register your models here.
admin.site.register(Employees)
admin.site.register(Files)
admin.site.register(Incoming)
admin.site.register(Outgoing)
