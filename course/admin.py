from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(About)
admin.site.register(Team)
# admin.site.register(Department)
# admin.site.register(Faculty)

@admin.register(Department)
class PostAdmin(admin.ModelAdmin):
    def job(self,obj):
        if obj.job :
            data = list(obj.job)
            for d in data:
                return d


    list_display = [
        'name',
        'job'
    ]

@admin.register(Faculty)
class PostAdmin(admin.ModelAdmin):
    
    list_display = [
        'name',
        'desc',
    ]