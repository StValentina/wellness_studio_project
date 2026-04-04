from django.urls import path
from . import views
from accounts.views import RegisterView

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
]