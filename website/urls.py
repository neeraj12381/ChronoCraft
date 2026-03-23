from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    
    # Is line ko change karo (contact -> contact_view)
    path('contact/', views.contact_view, name='contact'), 
    
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('privacy/', views.privacy, name='privacy'),
]