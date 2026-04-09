from django.urls import path
from . import views
from .views import ManagePageView

urlpatterns = [
    path('', views.home, name='home'),
    path('manage_page/', ManagePageView.as_view(), name='manage_page'),
]