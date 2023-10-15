from django.urls import path
from django.contrib.auth import views as auth_views
from bases.views import Home

urlpatterns =[
    path('', auth_views.LoginView.as_view(template_name='bases/login.html'),
         name='login'),
    path('accounts/profile/',Home.as_view(), name='home'),
    
  
   
]