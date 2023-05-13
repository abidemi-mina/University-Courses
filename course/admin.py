from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(About)
admin.site.register(Team)
# admin.site.register(Department)
# admin.site.register(Faculty)

@admin.register(Department)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),'f_slug':('fac',)}

    list_display = [
        'name',
        'fac',
        'job',
        'desc',
    ]

@admin.register(Jobs)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'dept',
        
    ]

@admin.register(Faculty)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('f_name',)}
    
    list_display = [
        'f_name',
        'desc',
        
    ]