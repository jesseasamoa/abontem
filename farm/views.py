from .models import DashboardCrop, DashboardLand, Management, Products, FinancePage, City, ContactPage, \
                    MostCultivated, ContactForm
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.urls import reverse_lazy
import requests
import random
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect


@method_decorator(csrf_exempt, name='dispatch')
class Home(TemplateView):
    template_name = 'home.html'

    @method_decorator(csrf_protect)
    def get(self, request):
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=f96dd9d99cc3fda5a23cef143e17f54f'
        cities = City.objects.filter(name='East Legon')
        weather_data = []

        for city in cities:
            response = requests.get(url.format(city))
            if response.status_code == 404:
                continue
            city_weather = response.json()
            weather = {
                'city': city,
                'temperature': city_weather['main']['temp'],
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon']
            }

            weather_data.append(weather)
        context = {'weather_data': weather_data}
        return render(self.request, 'home.html', context)


class DashboardHome(ListView):
    template_name = 'dashboard.html'
    queryset = DashboardCrop.objects.all()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=f96dd9d99cc3fda5a23cef143e17f54f'
    cities = City.objects.all()
    weather_data = []

    for city in cities:
        response = requests.get(url.format(city))
        if response.status_code == 404:
            continue
        city_weather = response.json()
        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)  # add the data for the current city into our list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        context['crops'] = DashboardCrop.objects.all()
        context['weather_gh'] = random.sample(self.weather_data, k=3)
        context['random_city'] = random.choices(self.weather_data, k=1)
        # context['most_cultivated'] = MostCultivated.objects.all(name='crop')
        # context['most_hectares'] = MostCultivated.objects.all(name='hectares')
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
        context['products'] = Products.objects.all()
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

@method_decorator(csrf_exempt, name='dispatch')
class Login(TemplateView):
    template_name = 'login.html'

    @method_decorator(csrf_protect)
    def post(self):
        pass

@method_decorator(csrf_exempt, name='dispatch')
class Register(TemplateView):
    template_name = 'register.html'

    @method_decorator(csrf_protect)
    def post(self):
        pass


@method_decorator(csrf_exempt, name='dispatch')
class Weather(ListView):
    template_name = 'weather.html'
    queryset = DashboardLand.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        context['products'] = City.objects.all()
        return context

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        weather_data = []
        city_search = request.POST('city_search')
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=7fb276f6f47e92af3f066b383ddc9936'
        for city in city_search:
            response = requests.get(url.format(city_search))
            if response.status_code == 404:
                continue
            weather = response.json()
            weather_search = {
                'city': city,
                'temperature': weather['main']['temp'],
                'description': weather['weather'][0]['description'],
                'icon': weather['weather'][0]['icon']
            }
        context = {'weather_search': weather_search, 'city_search': city_search}
        weather_data.append(weather_search)
        return render(request, 'weather.html', context)


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


@method_decorator(csrf_exempt, name='dispatch')
class PasswordReset(TemplateView):
    template_name = 'password_reset.html'

    @method_decorator(csrf_protect)
    def post(self):
        pass


class FourHundred(TemplateView):
    template_name = '404.html'


class FiveHundred(TemplateView):
    template_name = '500.html'


class Contact(CreateView):
    template_name = 'contact_us.html'
    model = ContactPage
    # fields = ['country', 'phone', 'subject', 'message']
    success_url = reverse_lazy('contact_us')
    form_class = ContactForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        context['country_list'] = ContactPage.objects.all()
        return context


class StartInvesting(TemplateView):
    template_name = 'start_investing.html'
    query_set = DashboardLand.objects.all()


class StartFarming(TemplateView):
    template_name = 'start_farming'
    query_set = DashboardLand.objects.all()

