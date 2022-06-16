from django.contrib import admin
from .models import FrontForm, Crop
# Register your models here.


class FrontFormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'contact', 'email', 'password')


class CropAdmin(admin.ModelAdmin):
    list_display = ('name', 'cash')


admin.site.register(FrontForm, FrontFormAdmin)
admin.site.register(Crop, CropAdmin)
