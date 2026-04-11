from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from WellnessNewProject.mixins import HostOnlyMixin
from bookings.models import Booking
from studio_classes.forms import StudioClassForm, TagsForm
from studio_classes.models import StudioClass, Tag


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
    success_url = reverse_lazy('manage_page')

class StudioClassesDetailsView(LoginRequiredMixin, DetailView):
    model = StudioClass
    template_name = 'studio_classes/details-class.html'
    context_object_name = 'studio_class'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_booked'] = Booking.objects.filter(
            user=self.request.user,
            booked_class=self.object,
        ).exists()
        return context

class StudioClassesDeleteView(LoginRequiredMixin, HostOnlyMixin, DeleteView):
    model = StudioClass
    template_name = 'studio_classes/delete-class.html'
    success_url = reverse_lazy('manage_page')

class TagsCreateView(LoginRequiredMixin, HostOnlyMixin, CreateView):
    model = Tag
    form_class = TagsForm
    template_name = 'tags/create-tag.html'
    success_url = reverse_lazy('manage_page')

class TagsDeleteView(LoginRequiredMixin, HostOnlyMixin, DeleteView):
    model = Tag
    template_name = 'tags/delete-tag.html'
    success_url = reverse_lazy('manage_page')