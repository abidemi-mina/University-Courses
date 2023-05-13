from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(About)
admin.site.register(Team)
# admin.site.register(Department)
# admin.site.register(Faculty)

@admin.register(Department)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'fac',
        'job'
    ]

@admin.register(Faculty)
class PostAdmin(admin.ModelAdmin):
    
    list_display = [
        'f_name',
        'desc',
    ]