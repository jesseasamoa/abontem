from .models import DashboardCrop, DashboardLand, Management, Products, FinancePage, City, ContactPage
from django.views.generic import ListView, TemplateView, DetailView
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
import requests
import random


class Home(TemplateView):
    template_name = 'home.html'

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


class Login(TemplateView):
    template_name = 'login.html'


class Register(TemplateView):
    template_name = 'register.html'


class Weather(ListView):
    template_name = 'weather.html'
    queryset = DashboardLand.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        context['products'] = City.objects.all()
        return context

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


class PasswordReset(TemplateView):
    template_name = 'password_reset.html'


class FourHundred(TemplateView):
    template_name = '404.html'


class FiveHundred(TemplateView):
    template_name = '500.html'


class Contact(ListView):
    template_name = 'contact_us.html'
    queryset = DashboardLand.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        name = self.request.POST['name']
        phone = self.request.POST['phone']
        subject = self.request.POST['subject']
        message = self.request.POST['message']
        contact = ContactPage()
        contact.name = name
        contact.phone = phone
        contact.subject = subject
        contact.message = message
        contact.save()
        try:
            send_mail(
                'Contact message from abontem.com',
                f'You have a contact message from:\n Name - {contact.name},\n'
                f'Contact - {contact.phone}\n'
                f'Subject - {contact.subject}\n'
                f'Message - {contact.message}\n',
                'farm@abontem.com',
                ['farm@abontem.com', 'jesseasamoa@gmail.com'],
                fail_silently=False,
            )
        except ConnectionRefusedError:
            'No internet connection'
        messages.info(self.request, 'Thank You! You will get a call shortly.')
        return render(self.request, 'contact_us.html')


class StartInvesting(TemplateView):
    template_name = 'start_investing.html'
    query_set = DashboardLand.objects.all()

