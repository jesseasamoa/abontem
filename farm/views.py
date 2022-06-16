from .models import Crop
from django.views.generic import ListView, TemplateView
# import datetime

# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


class DashboardHome(ListView):
    template_name = 'dashboard.html'
    queryset = Crop.objects.order_by('-published')


class Seeds(TemplateView):
    template_name = 'seeds.html'
