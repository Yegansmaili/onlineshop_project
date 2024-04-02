from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        # fields = UserCreationForm.Meta.fields + ('age',)
        fields = ('username', 'email', 'age',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'email', 'age',)
