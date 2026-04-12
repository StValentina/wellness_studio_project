from django.urls import path

from services.views import ServiceListView, ServiceCreateView, ServiceEditView, ServiceDeleteView, ServiceClassesView, \
    ServiceDetailView

urlpatterns = [
    path('', ServiceListView.as_view(), name='list-services'),
    path('create/', ServiceCreateView.as_view(), name='create-service'),
    path('dashboard/', ServiceListView.as_view(), name='services'),
    path('edit/<int:pk>/', ServiceEditView.as_view(), name='edit-service'),
    path('delete/<int:pk>/', ServiceDeleteView.as_view(), name='delete-service'),
    path('details/<int:pk>/', ServiceDetailView.as_view(), name='details-service'),
    path('<int:pk>/classes/', ServiceClassesView.as_view(), name='service-classes'),
]