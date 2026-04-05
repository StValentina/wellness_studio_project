from django.urls import path

from services.views import ServiceListView, ServiceCreateView

urlpatterns = [
    path('', ServiceListView.as_view(), name='list-service'),
    path('create/', ServiceCreateView.as_view(), name='create-service'),
    path('services/', ServiceListView.as_view(), name='services'),
]