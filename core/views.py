from django.shortcuts import render

from services.models import Service


# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def manage_page(request):
    services = Service.objects.all()
    return render(request, 'core/manage_page.html', {'services': services})

