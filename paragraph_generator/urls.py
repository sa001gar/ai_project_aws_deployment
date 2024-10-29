from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    # Authentication URLs
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.user_logout, name='logout'),

    # Application URLs
    path('', views.index,name='index'),  # Welcome p
    path('dashboard/', views.dashboard, name='dashboard'),
    path('generate/', views.generate_paragraph, name='generate_paragraph'),
]
