from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic.detail import DetailView
from accounts.forms import AccountUserCreationForm, LoginUserForm
from accounts.forms import AccountEditForm
from accounts.models import Profile


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

class AccountDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/detail-profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        user_id = self.kwargs.get('pk')
        return get_object_or_404(Profile, user__pk=user_id)

class AccountEditView(LoginRequiredMixin, UpdateView):
    form_class = AccountEditForm
    template_name = 'accounts/edit-profile.html'
    success_url = reverse_lazy('home')