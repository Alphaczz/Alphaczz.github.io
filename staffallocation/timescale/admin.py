from re import A
from django.contrib import admin
from .models import Feedemp, taskAlloc

# Register your models here.
admin.site.register(Feedemp)
admin.site.register(taskAlloc)