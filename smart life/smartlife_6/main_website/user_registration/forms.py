from django import forms


class Registration_Form(forms.Form):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput
        (
            attrs= {
                    'type':'text',
                    'pattern': '[Aa-Zz]{1,11}',
                    'maxlength': '11',
                    'title': 'Minimum 3 character!',
                    'placeholder':"First Name"
                    }
        ))
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput
            (
            attrs={
                   'type': 'text',
                   'pattern': '[Aa-Zz]{1,11}',
                   'maxlength': '11',
                   'title': 'Minimum 3 character!',
                   'placeholder': "Last Name"
                   }
        ))

    phone_number = forms.CharField(
        required=True,
        widget=forms.TextInput
            (
            attrs={
                   'type': 'text',
                   'pattern': '^[\+][8][8]\d{11}',
                   'maxlength': '15',
                   'title': 'Start with +88',
                   'placeholder': "Phone Number"
                   }
        ))
    email_address = forms.CharField(
        required=True,
        widget=forms.TextInput
            (
            attrs={
                   'type': 'email',
                   'maxlength': '11',
                   'title': 'Minimum 3 character!',
                   'placeholder': "Email Address"
                   }
        ))
    user_name = forms.CharField(
        required=True,
        widget=forms.TextInput
            (
            attrs={
                   'type': 'text',
                   'pattern': '[A-Za-z0-9]{3,11}',
                   'maxlength': '11',
                   'title': 'Minimum 3 character!',
                   'placeholder': "User Name"
                   }
        ))
    user_password = forms.CharField(
        required=True,
        widget=forms.TextInput
            (
            attrs={
                   'type': 'password',
                   'pattern': '[A-Za-z0-9]{3,11}',
                   'maxlength': '11',
                   'title': 'Minimum 3 character!',
                   'placeholder': "User Password"
                   }
        ))
    user_address = forms.CharField(
        required=True,
        widget=forms.TextInput
            (
            attrs={
                   'type': 'text',
                   'maxlength': '30',
                   'title': 'Minimum 3 character!',
                   'placeholder': "User Address"
                   }
        ))

