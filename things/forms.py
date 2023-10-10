from django import forms
from django.core.validators import RegexValidator
from .models import User

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields =['name', 'description', 'quantity', 'email', 'bio']
        widgets = {'description' : forms.Textarea(), 'quantity' : forms.NumberInput()}