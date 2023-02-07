from django.contrib.auth.forms import UserCreationForm

from .models import User

from django import forms

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'EnterUser name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'EnterUser email'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'EnterUser password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'confirm pass'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']