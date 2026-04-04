from django.contrib.auth import get_user_model
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