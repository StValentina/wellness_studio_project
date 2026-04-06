from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('manage_page', views.manage_page, name='manage_page'),
]