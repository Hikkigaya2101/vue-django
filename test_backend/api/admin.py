from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import *
admin.site.register(Unit)
admin.site.register(UnitType)
admin.site.register(Consumer)
# Register your models here.

# class MyAdmin(TreeAdmin):
#     form = movenodeform_factory(Unit)
#
# admin.site.register(Unit, MyAdmin)