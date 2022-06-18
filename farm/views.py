from .models import Crop, Land
from django.views.generic import ListView, TemplateView
from itertools import chain
from operator import attrgetter
# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


class DashboardHome(ListView):
    template_name = 'dashboard.html'
    queryset = Crop.objects.all()
    context_object_name = 'crops'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['crops'] = Crop.objects.all()
        context['land'] = Land.objects.all()
        return context


class Seeds(TemplateView):
    template_name = 'seeds.html'
