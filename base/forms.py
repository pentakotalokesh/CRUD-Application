from dataclasses import fields
from django.forms import ModelForm
from .models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['Person_name','Person_email','Person_phno']