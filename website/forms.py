from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record









# create add record form
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "First Name", "class": "form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Last Name", "class": "form-control"}), label="")
    my_class = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Class", "class": "form-control"}), label="")
    timing = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Timing", "class": "form-control"}), label="")

    class Meta:
        model = Record
        exclude = ("user",)
