from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from WellnessNewProject.mixins import HostOnlyMixin
from services.forms import ServiceCreateForm
from services.models import Service


# Create your views here.

class ServiceListView(ListView):
    model = Service
    template_name = 'services/list-services.html'
    context_object_name = 'services'
    paginate_by = 10
    ordering = '-created_at'

    def get_queryset(self):
        queryset = Service.objects.all()
        return queryset


class ServiceCreateView(LoginRequiredMixin, HostOnlyMixin, CreateView):
    model = Service
    form_class = ServiceCreateForm
    template_name = 'services/create-service.html'
    success_url = reverse_lazy('services')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)