from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name="index"),
    path('contact/', views.contact, name="contact"),
    path('home/', views.Home,name="home1"),
    path('features/', views.features,name="features"),
    path('services/', views.services,name="services"),
    path('vehicles/', views.vehicles, name="vehicles"),
    path('contactdetails/', views.contactdetails, name="contactdetails"),
    path('signup/', views.signup, name="signup"),
    path('handelsignup/', views.handelsignup, name="handelsignup"),
    path('login/', views.handel_login, name="handel_login"),
]