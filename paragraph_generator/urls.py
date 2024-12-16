from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from . import views

from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

urlpatterns = [
     # Authentication URLs
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.user_logout, name='logout'),

    # Application URLs
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('generate/', views.generate_paragraph_index, name='generate_paragraph'),

    # Sitemap URL
    path('sitemap.xml', sitemap, {'sitemaps': {'static': StaticViewSitemap}}, name='sitemap'),
]
