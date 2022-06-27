from .models import DashboardCrop, DashboardLand, Management, Products, FinancePage, City
from django.views.generic import ListView, TemplateView
import requests
import json
import urllib


class Home(TemplateView):
    template_name = 'home.html'


class DashboardHome(ListView):
    template_name = 'dashboard.html'
    queryset = DashboardCrop.objects.all()
    paginate_by = 1
    model = DashboardCrop

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        context['crops'] = DashboardCrop.objects.all()
        context['weather'] = City.objects.all()
        return context


class Invest(ListView):
    template_name = 'invest.html'
    queryset = DashboardLand.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        return context


class BuyRentFarmland(TemplateView):
    template_name = 'buy_rent_farmland.html'
    queryset = DashboardLand.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        return context


class Services(ListView):
    template_name = 'services.html'
    queryset = DashboardLand.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        return context


class Finance(ListView):
    template_name = 'finance.html'
    queryset = DashboardLand.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        context['finance'] = FinancePage.objects.all()
        return context


class Business(ListView):
    template_name = 'business.html'
    queryset = DashboardLand.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        return context


class FarmProducts(ListView):
    template_name = 'farm_products.html'
    queryset = DashboardLand.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        context['products'] =Products.objects.all()
        return context


class DataTech(ListView):
    template_name = 'data_tech.html'
    queryset = DashboardLand.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        return context


class FarmLands(ListView):
    template_name = 'farmlands.html'
    queryset = DashboardLand.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        return context


class FarmManagement(ListView):
    template_name = 'farm_management.html'
    queryset = DashboardLand.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        context['management'] = Management.objects.all()
        return context


class Forests(ListView):
    template_name = 'forest_preservation.html'
    queryset = DashboardLand.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        return context


class Consultations(ListView):
    template_name = 'consultations.html'
    queryset = DashboardLand.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        return context


class Premium(ListView):
    template_name = 'premium_services.html'
    queryset = DashboardLand.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        return context


class Login(TemplateView):
    template_name = 'login.html'


class Register(TemplateView):
    template_name = 'register.html'


class Contact(ListView):
    template_name = 'contact_us.html'
    queryset = DashboardLand.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        return context


class Weather(ListView):
    template_name = 'weather.html'
    queryset = DashboardLand.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        context['products'] = City.objects.all()
        return context


class Payments(ListView):
    template_name = 'payments.html'
    queryset = DashboardLand.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        return context


class Profile(ListView):
    template_name = 'profile.html'
    queryset = DashboardLand.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        return context


class PasswordReset(TemplateView):
    template_name = 'password_reset.html'
