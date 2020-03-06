from django.contrib import admin
from django.urls import path,include
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('register/',views.register,name='register'),
    
]
