from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import AccountUserCreationForm, LoginUserForm


# Create your views here.

class RegisterView(CreateView):
    template_name = "accounts/register.html"
    form_class = AccountUserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)
        return result

class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'accounts/login.html'

    # да се махме, след като се направи профилна страница
    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)

def logout_user(request):
    logout(request)
    return redirect('home')