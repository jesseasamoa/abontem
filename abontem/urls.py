"""abontem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from farm.views import Home, DashboardHome, BuyRentFarmland, Invest, Services, Finance, Business, FarmProducts, \
                        DataTech, FarmLands, FarmManagement, Forests, Consultations, Premium, Login, Register, \
                        Contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('dashboard/', DashboardHome.as_view(), name='dashboard'),
    path('dashboard/buy_rent_farmland/', BuyRentFarmland.as_view(), name='buy_rent_farmland'),
    path('dashboard/invest/', Invest.as_view(), name='invest'),
    path('dashboard/services/', Services.as_view(), name='services'),
    path('dashboard/finance/', Finance.as_view(), name='finance'),
    path('dashboard/business/', Business.as_view(), name='business'),
    path('dashboard/farm_products/', FarmProducts.as_view(), name='farm_products'),
    path('dashboard/data_tech/', DataTech.as_view(), name='data_tech'),
    path('dashboard/farmlands/', FarmLands.as_view(), name='farmlands'),
    path('dashboard/farm_management/', FarmManagement.as_view(), name='farm_management'),
    path('dashboard/forest_preservation/', Forests.as_view(), name='forest_preservation'),
    path('dashboard/consultations/', Consultations.as_view(), name='consultations'),
    path('dashboard/premium_services/', Premium.as_view(), name='premium_services'),
    path('dashboard/login/', Login.as_view(), name='login'),
    path('dashboard/register/', Register.as_view(), name='register'),
    path('dashboard/contact_us/', Contact.as_view(), name='contact_us')
]
