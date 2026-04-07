from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from WellnessNewProject.mixins import HostOnlyMixin
from studio_classes.forms import StudioClassForm
from studio_classes.models import StudioClass


# Create your views here.
class StudioClassesCreateView(LoginRequiredMixin, HostOnlyMixin, CreateView):
    model = StudioClass
    form_class = StudioClassForm
    template_name = 'studio_classes/create-class.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class StudioClassesEditView(LoginRequiredMixin, HostOnlyMixin, UpdateView):
    model = StudioClass
    form_class = StudioClassForm
    template_name = 'studio_classes/edit-class.html'
    success_url = reverse_lazy('services')

class StudioClassesDeleteView(LoginRequiredMixin, HostOnlyMixin, DeleteView):
    model = StudioClass
    template_name = 'studio_classes/delete-class.html'
    success_url = reverse_lazy('services')
