from django.contrib.auth import get_user_model, authenticate
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

UserModel = get_user_model()


class AccountUserCreationForm(UserCreationForm):
    user = None

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class AccountChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel

class LoginUserForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'label': 'Email'}
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'label': 'Password'}
        ),
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(username=email, password=password)

        if not user or not user.is_active:
            raise forms.ValidationError('Invalid email or password.')
        self.user = user
        return self.cleaned_data

    def get_user(self):
        return self.user