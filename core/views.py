from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from WellnessNewProject.mixins import HostOnlyMixin
from services.models import Service
from studio_classes.models import StudioClass, Tag


# Create your views here.

def home(request):
    return render(request, 'core/home.html')

class ManagePageView(LoginRequiredMixin, HostOnlyMixin, TemplateView):
    template_name = 'core/manage_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['studio_classes'] = StudioClass.objects.all()
        context['tags'] = Tag.objects.all()
        return context
