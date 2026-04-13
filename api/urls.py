from django.urls import path

from api.views import ServiceListViewApi, StudioClassListViewApi

urlpatterns = [
    path('services/', ServiceListViewApi.as_view(), name='api-services'),
    path('classes/', StudioClassListViewApi.as_view(), name='api-classes'),
]