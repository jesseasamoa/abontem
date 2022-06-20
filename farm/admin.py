from django.contrib import admin
from .models import FrontForm, DashboardLand, DashboardCrop, Invest, City, Finance
# Register your models here.


class FrontFormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'contact', 'email', 'password')


class DashboardCropAdmin(admin.ModelAdmin):
    list_display = ('name', 'cash')


class DashboardLandAdmin(admin.ModelAdmin):
    list_display = ('region', 'size')


class InvestAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'email')


admin.site.register(FrontForm, FrontFormAdmin)
admin.site.register(DashboardCrop, DashboardCropAdmin)
admin.site.register(DashboardLand, DashboardLandAdmin)
admin.site.register(Invest, InvestAdmin)
admin.site.register(City)
admin.site.register(Finance)
