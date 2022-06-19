from .models import DashboardCrop, DashboardLand, Invest
from django.views.generic import ListView, TemplateView
from itertools import chain
from operator import attrgetter
# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


class DashboardHome(ListView):
    template_name = 'dashboard.html'
    queryset = DashboardCrop.objects.all()
    context_object_name = 'crops'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['crops'] = DashboardCrop.objects.all()
        context['land'] = DashboardLand.objects.all()
        return context


class Invest(ListView):
    template_name = 'invest.html'
    queryset = DashboardLand.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        return context


class BuyRentFarmland(TemplateView):
    template_name = 'seeds.html'


class Services(ListView):
    template_name = 'services.html'


class Finance(ListView):
    template_name = 'finance.html'


class Business(ListView):
    template_name = 'business.html'


class FarmProducts(ListView):
    template_name = 'farm_products.html'


class DataTech(ListView):
    template_name = 'data_tech.html'


class FarmLands(ListView):
    template_name = 'farmlands.html'


class FarmManagement(ListView):
    template_name = 'farm_management.html'


class Forests(ListView):
    template_name = 'forest_preservation.html'


class Consultations(ListView):
    template_name = 'consultations.html'


class Premium(ListView):
    template_name = 'premium_services.html'
