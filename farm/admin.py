from django.contrib import admin
from .models import FrontForm
# Register your models here.


class FrontFormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'contact', 'email', 'password')


admin.site.register(FrontForm, FrontFormAdmin)
