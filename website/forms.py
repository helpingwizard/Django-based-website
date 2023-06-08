from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import User
from django import forms

class SignUpForm(UserCreationForm):
	email = forms.EmailField(Label ="", widget = forms.TextInput(attrs={'class'}))
	first_name = forms.CharField()
	last_name = forms.CharField()