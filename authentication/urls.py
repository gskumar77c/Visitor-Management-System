from django.contrib import admin
from django.urls import path,include
from .import views as auth_views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',auth_views.home)
    
]
