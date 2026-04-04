from django.contrib.auth import login
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import AccountUserCreationForm


# Create your views here.

def home(request):
    return HttpResponse("Hello, world.")

class RegisterView(CreateView):
    template_name = "accounts/register.html"
    form_class = AccountUserCreationForm
    success_url = reverse_lazy('home')
    success_message = "Your profile was created successfully"

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, form.instance)

        return result