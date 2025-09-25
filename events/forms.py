from django import forms
from .models import Event  # your event model

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'description'] 
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }  


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Enter username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'})
    )
