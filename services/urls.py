from django.urls import path

from services.views import ServiceListView, ServiceCreateView, ServiceEditView, ServiceDeleteView

urlpatterns = [
    path('', ServiceListView.as_view(), name='list-service'),
    path('create/', ServiceCreateView.as_view(), name='create-service'),
    path('services/', ServiceListView.as_view(), name='services'),
    path('edit/<int:pk>/', ServiceEditView.as_view(), name='edit-service'),
    path('delete/<int:pk>/', ServiceDeleteView.as_view(), name='delete-service'),

]