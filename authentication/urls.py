from django.contrib import admin
from django.urls import path,include
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('',auth_views.LoginView.as_view(template_name='authentication/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='authentication/logout.html'),name='logout'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('checkin_email/',views.checkin_email,name='checkin-email'),
    path('checkout_email/',views.checkout_email,name='checkout-email'),
    path('viewlog/',views.view_log,name='log')
    
]


