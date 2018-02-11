from django import forms
from .models import *

class Registration_Form(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput
        (
            attrs= {'class': 'text',
                    'type':'text',
                    'pattern': '[A0-Z9]{3,11}',
                    'maxlength': '11',
                    'title': 'Minimum 3 character!',
                    'placeholder':"Can't be blank"
                    }
        ))
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput
            (
            attrs={'class': 'text',
                   'type': 'text',
                   'pattern': '[A0-Z9]{3,11}',
                   'maxlength': '11',
                   'title': 'Minimum 3 character!',
                   'placeholder': "Can't be blank"
                   }
        ))
    phone_number = forms.CharField(
        required=True,
        widget=forms.TextInput
            (
            attrs={'class': 'text',
                   'type': 'text',
                   'pattern': '[0-9]{3,11}',
                   'maxlength': '11',
                   'title': 'Minimum 3 character!',
                   'placeholder': "Can't be blank"
                   }
        ))
    email_address = forms.CharField(
        required=True,
        widget=forms.TextInput
            (
            attrs={'class': 'text',
                   'type': 'email',
                   'maxlength': '11',
                   'title': 'Minimum 3 character!',
                   'placeholder': "Can't be blank"
                   }
        ))
    user_name = forms.CharField(
        required=True,
        widget=forms.TextInput
            (
            attrs={'class': 'text',
                   'type': 'text',
                   'pattern': '[A0-Z9]{3,11}',
                   'maxlength': '11',
                   'title': 'Minimum 3 character!',
                   'placeholder': "Can't be blank"
                   }
        ))
    user_password = forms.CharField(
        required=True,
        widget=forms.TextInput
            (
            attrs={'class': 'text',
                   'type': 'password',
                   'pattern': '[A0-Z9]{3,11}',
                   'maxlength': '11',
                   'title': 'Minimum 3 character!',
                   'placeholder': "Can't be blank"
                   }
        ))
    user_address = forms.CharField(
        required=True,
        widget=forms.TextInput
            (
            attrs={'class': 'text',
                   'type': 'text',
                   'pattern': '[A0-Z9]{3,11}',
                   'maxlength': '11',
                   'title': 'Minimum 3 character!',
                   'placeholder': "Can't be blank"
                   }
        ))
