from django import forms
from .models import Veikkaukset


class VeikkauksetModelForm(forms.ModelForm):

    class Meta:
        model = Veikkaukset
        fields = '__all__'
