from .models import DashboardCrop, DashboardLand, Management, Products, FinancePage, City, ContactPage, \
                    ContactForm
from django.views.generic import ListView, TemplateView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
import requests
import random
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.mixins import LoginRequiredMixin
from abontem import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from abontem.tokens import generate_token
from django.core.mail import EmailMessage, send_mail
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


@method_decorator(csrf_exempt, name='dispatch')
class Home(DetailView):
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

    @method_decorator(csrf_protect)
    def post(self, request):
        if request.method == 'POST':
            email = request.POST["mail"]
            pass1 = request.POST["password"]
            user = authenticate(email=email, pass1=pass1)
            if user is not None:
                login(request, user)
                fname = user.first_name
                return render(request, 'dashboard.html', {'email': email})
            else:
                messages.error(request, 'Enter the right credentials!')
                return redirect(request, 'login.html')
        return render(request, 'login.html')

    # HOME PAGE SIGNUP FORM
    @method_decorator(csrf_protect)
    def post(self, request):
        if request.method == 'POST':
            fname = request.POST["fname"]
            contact = request.POST["contact"]
            email = request.POST["email"]
            pass1 = request.POST["pass1"]
            myuser = User.objects.create_user(fname, contact, email, pass1)
            myuser.first_name = fname
            myuser.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login.html')
        return render(request, 'register.html')


class DashboardHome(LoginRequiredMixin, ListView):
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


class FourHundred(TemplateView):
    template_name = '404.html'


class FiveHundred(TemplateView):
    template_name = '500.html'


@method_decorator(csrf_exempt, name='dispatch')
class Contact(TemplateView):
    template_name = 'contact_us.html'
    query_set = DashboardLand.objects.all()
    success_url = 'contact_us.html'
    form_class = ContactForm

    @method_decorator(csrf_protect)
    def post(self, request):
        f = ContactForm(request.POST)
        if f.is_valid():
            messages.info(request, 'Thank you! You will get a call shortly!')
            f.save()
            country = request.POST["country"]
            phone = request.POST["phone"]
            subject = request.POST["subject"]
            message = request.POST["message"]
            from_email = settings.EMAIL_HOST_USER
            recipients = ['farm@abontem.com', 'jesseasamoa@gmail.com']
            send_mail(f'You have a message from {country},\n'
                      f' the contact is {phone}, and {subject} as the subject,\n '
                      f'Message: {message}, {from_email}, {recipients}')
        return render(request, 'dashboard.html')

    # @method_decorator(csrf_protect)
    # def post(self, request):
    #     country = request.POST['country']
    #     phone = request.POST['phone']
    #     subject = request.POST['subject']
    #     message = request.POST['message']
    #     contact = ContactPage()
    #     contact.country = country
    #     contact.phone = phone
    #     contact.subject = subject
    #     contact.message = message
    #     contact.save()
    #     # try:
    #     send_mail(
    #         'Contact message from abontem.com',
    #         f'You have a contact message from:\n Name - {contact.country}\n'
    #         f'Contact - {contact.phone}\n'
    #         f'Subject - {contact.subject}\n'
    #         f'Message - {contact.message}\n',
    #         'farm@abontem.com',
    #         ['farm@abontem.com', 'jesseasamoa@gmail.com'],
    #         fail_silently=False,
    #     )
    #     # except ConnectionRefusedError:
    #     #     'No internet connection'
    #     messages.info(request, 'Thank You! You will get a call shortly.')
    #     return render(request, 'contact_us.html')



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = DashboardLand.objects.all()
        # context['country_list'] = ContactPage.objects.all()
        return context


class StartInvesting(TemplateView):
    template_name = 'start_investing.html'
    query_set = DashboardLand.objects.all()


class StartFarming(TemplateView):
    template_name = 'start_farming.html'
    query_set = DashboardLand.objects.all()


@method_decorator(csrf_exempt, name='dispatch')
class Register(TemplateView):
    template_name = 'register.html'

    @method_decorator(csrf_protect)
    def post(self, request):
        if request.method == 'POST':
            fname = request.POST['fname']
            lname = request.POST['lname']
            username = request.POST['uname']
            contact = request.POST['contact']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']
            if User.objects.filter(email=email):
                messages.error(request, 'Email already exists, kindly choose another email')
                return redirect('register.html')
            if User.objects.filter(uname=username):
                messages.error(request, 'Username already exists, kindly choose another username')
                return redirect('register.html')
            if len(username) > 10:
                messages.error(request, 'Username should not be more than 10 characters')
            if pass1 != pass2:
                messages.error(request, 'The passwords do not match. Please retype!')
            self.myuser = User.objects.create_user(username, email, pass1)
            self.myuser.first_name = fname
            self.myuser.is_active = False
            self.myuser.save()
            messages.success(request, 'Your account has been created successfully!')

            # WELCOME EMAIL
            subject = 'hi'
            message = 'hi + myuser.firs_name'
            from_email = settings.EMAIL_HOST_USER
            recipients = [self.myuser.email]
            send_mail(subject, message, from_email, recipients, fail_silently=True)

            # EMAIL ACTIVATION

            current_site = get_current_site(request)
            email_subject = "confirm your email "
            message2 = render_to_string("email_confirmation.html", {
                'name': self.myuser.first_name,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(self.myuser.pk)),
                'token': generate_token.make_token(self.myuser)
            })

            email = EmailMessage(
                email_subject,
                message2,
                settings.EMAIL_HOST_USER,

                [self.myuser.email],
            )
            email.fail_silently = True
            email.send()
            return redirect('login.html')
        return render(request, 'register.html')


@method_decorator(csrf_exempt, name='dispatch')
class Login(TemplateView):
    template_name = 'login.html'

    @method_decorator(csrf_protect)
    def post(self, request):
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                fname = user.first_name
                return render(request, 'dashboard.html', {'email': email})
            else:
                messages.error(request, 'Enter the right credentials!')
                return redirect(request, 'login.html')
        return render(request, 'login.html')


class Logout(TemplateView):
    template_name = 'login.html'
    next_page = 'login.html'


@method_decorator(csrf_exempt, name='dispatch')
class PasswordReset(TemplateView):
    template_name = 'password_reset.html'

    @method_decorator(csrf_protect)
    def post(self):
        pass


class PasswordResetCompleteView(TemplateView):
    pass


class Activate(TemplateView):
    template_name = 'activate.html'

    def post(self, request, uidb64, token):
        try:
            uid = str(urlsafe_base64_decode(uidb64))
            myuser = User.obj.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            myuser = None

        if myuser is not None and generate_token.check_token(myuser, token):
            myuser.is_active = True
            myuser.save()
            login(request, myuser)
            return redirect('home.html')
        else:
            return  render(request, 'activation_failed.html')


