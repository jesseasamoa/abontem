from django.contrib import admin
from .models import FrontForm, Crop, Land
# Register your models here.


class FrontFormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'contact', 'email', 'password')


class CropAdmin(admin.ModelAdmin):
    list_display = ('name', 'cash')


class LandAdmin(admin.ModelAdmin):
    list_display = ('region', 'size')


admin.site.register(FrontForm, FrontFormAdmin)
admin.site.register(Crop, CropAdmin)
admin.site.register(Land, LandAdmin)
