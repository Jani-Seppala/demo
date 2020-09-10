from django import forms
from django.forms import ModelForm, modelformset_factory
from django.core import validators
from .models import Profile, Veikkaukset
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class VeikkauksetModelForm(forms.ModelForm):

    class Meta:
        model = Veikkaukset
        fields = '__all__'


# class BaseVeikkauksetFormSet:
#     VeikkauksetFormSet = modelformset_factory(Veikkaukset, fields='__all__')
