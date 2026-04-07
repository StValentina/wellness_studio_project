from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from studio_classes.forms import StudioClassForm
from studio_classes.models import StudioClass


# Create your views here.
class StudioClassesCreateView(CreateView):
    model = StudioClass
    form_class = StudioClassForm
    template_name = 'studio_classes/create-class.html'
    success_url = reverse_lazy('home')

