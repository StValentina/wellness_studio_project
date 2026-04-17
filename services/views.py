from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from WellnessNewProject.mixins import HostOnlyMixin
from bookings.models import Booking
from services.forms import ServiceCreateForm
from services.models import Service
from studio_classes.models import StudioClass


# Create your views here.

class ServiceListView(ListView):
    model = Service
    template_name = 'services/list-services.html'
    context_object_name = 'services'
    ordering = 'created_at'

    def get_queryset(self):
        queryset = Service.objects.all()
        return queryset

class ServiceCreateView(LoginRequiredMixin, HostOnlyMixin, CreateView):
    model = Service
    form_class = ServiceCreateForm
    template_name = 'services/create-service.html'
    success_url = reverse_lazy('services')

    def form_valid(self, form):
        if not form.instance.pk:
            form.instance.created_by = self.request.user
        return super().form_valid(form)

class ServiceEditView(LoginRequiredMixin, HostOnlyMixin, UpdateView):
    model = Service
    form_class = ServiceCreateForm
    template_name = 'services/edit-service.html'
    success_url = reverse_lazy('services')

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)

class ServiceDeleteView(LoginRequiredMixin, HostOnlyMixin, DeleteView):
    model = Service
    template_name = 'services/delete-service.html'
    success_url = reverse_lazy('services')

class ServiceDetailView(LoginRequiredMixin, HostOnlyMixin, DetailView):
    model = Service
    template_name = 'services/details-service.html'
    context_object_name = 'service'

class ServiceClassesView(ListView):
    model = StudioClass
    template_name = 'services/service_classes.html'
    context_object_name = 'classes'

    def get_queryset(self):
        service_id = self.kwargs['pk']
        return StudioClass.objects.filter(studio_class_service=service_id).order_by('class_date', 'start_time')
