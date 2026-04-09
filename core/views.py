from django.shortcuts import render

from services.models import Service
from studio_classes.models import StudioClass, Tag


# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def manage_page(request):
    services = Service.objects.all()
    classes = StudioClass.objects.all()
    tags = Tag.objects.all()
    return render(request, 'core/manage_page.html', {
        'services': services,
        'classes': classes,
        'tags': tags,
    })

