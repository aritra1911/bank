from django import forms

class LogInForm(forms.Form):
    customerid: forms.CharField = forms.CharField(label='Customer Id:')
    password: forms.CharField = forms.CharField(
        label='Password:',
        widget=forms.PasswordInput,
    )