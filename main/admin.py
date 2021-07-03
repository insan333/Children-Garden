from django.contrib import admin
from .models import Parent,Educator,Children_Garden,Children

admin.site.register(Parent)
admin.site.register(Educator)
admin.site.register(Children)
admin.site.register(Children_Garden)

