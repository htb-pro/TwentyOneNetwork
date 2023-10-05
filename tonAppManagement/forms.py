from django import forms
from django.forms import ModelForm
from tonAppManagement.models import UserInformations


class UserForm(ModelForm):
    """User form"""
    class Meta:
        model=UserInformations
        fields=['firstname','secondname','service','number','email',]