from django.contrib import admin
from .models import FrontForm, DashboardLand, DashboardCrop, Invest, City, Management, Products, ContactPage,\
                    MostCultivated, PaymentDetails


class MostCultivatedAdmin(admin.ModelAdmin):
    list_display = ('crop', 'hectares')


class DashboardCropAdmin(admin.ModelAdmin):
    list_display = ('name', 'production')


class DashboardLandAdmin(admin.ModelAdmin):
    list_display = ('region', 'size')


class InvestAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'email')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('country', 'phone', 'message')


class PaymentDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')


admin.site.register(DashboardCrop, DashboardCropAdmin)
admin.site.register(DashboardLand, DashboardLandAdmin)
admin.site.register(Invest, InvestAdmin)
admin.site.register(City)
admin.site.register(Management)
admin.site.register(Products)
admin.site.register(ContactPage, ContactAdmin)
admin.site.register(MostCultivated, MostCultivatedAdmin)
admin.site.register(PaymentDetails, PaymentDetailsAdmin)

