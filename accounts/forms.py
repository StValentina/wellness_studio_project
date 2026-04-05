from django.contrib.auth import get_user_model, authenticate
from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Profile

UserModel = get_user_model()


class AccountUserCreationForm(UserCreationForm):
    user = None

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)

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

class AccountEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'profile_picture', 'bio')
        widgets = {
            'first_name': forms.TextInput(attrs={'label': 'First Name'}),
            'last_name': forms.TextInput(attrs={'label': 'Last Name'}),
            'profile_picture': forms.FileInput(attrs={'label': 'Profile Picture'}),
            'bio': forms.Textarea(attrs={
                'class': 'form-field-bio',
                'label': 'Bio',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.profile_picture:
            self.fields['profile_picture'].disabled = True
