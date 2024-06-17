"""Module that provides forms."""
from django.contrib.auth import forms, models


class Registration(forms.UserCreationForm):
    """Represents registration form."""

    class Meta:
        model = models.User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
