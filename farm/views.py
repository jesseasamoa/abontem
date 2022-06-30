from .models import DashboardCrop, DashboardLand, Management, Products, FinancePage, City, ContactPage
from django.views.generic import ListView, TemplateView
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
# from django.views.decorators.csrf import csrf_protect
import requests


class Home(TemplateView):
    template_name = 'home.html'


class DashboardHome(ListView):
    template_name = 'dashboard.html'
    queryset = DashboardCrop.objects.all()

    # def get(self, request):
    #     url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=f96dd9d99cc3fda5a23cef143e17f54f'
    #     cities = City.objects.all()
    #
    #     weather_data = []
    #
    #     for city in cities:
    #         response = requests.get(url.format(city))
    #         if response.status_code == 404:
    #             continue
    #         city_weather = response.json()
    #         weather = {
    #             'city': city,
    #             'coo': city_weather['coord']['lat']['lon'],
    #             'temperature': city_weather['main']['temp'],
    #             'description': city_weather['weather'][0]['description'],
    #             'icon': city_weather['weather'][0]['icon']
    #         }
    #
    #         weather_data.append(weather)  # add the data for the current city into our list
    #
    #     context = {'weather_data': weather_data}
    #     # self.object = self.get_object(context)
    #     return render(request, 'dashboard.html', context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        context['crops'] = DashboardCrop.objects.all()
        # context['weather_data'] = self.object
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

    # @csrf_protect
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
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
        else:
            return render(self.request, 'contact_us.html')
