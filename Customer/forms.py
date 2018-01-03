from django import forms
from django.forms import SelectDateWidget, Textarea, EmailInput, HiddenInput
from .models import Customer
#from .choices import *
#from haystack.forms import SearchForm


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "firstName",
            "lastName",
            "billStreet",
            "billCity",
            "billState",
            "billZip",
            "phone1",
            "phone2",
            "email",
            "source"
        ]
        widgets = {'email':EmailInput}
