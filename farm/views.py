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



class Seeds(TemplateView):
    template_name = 'seeds.html'
