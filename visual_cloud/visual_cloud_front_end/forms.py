from django import forms
from django.utils.translation import ugettext as _

class LoginForm(forms.Form):
    """Greater form for more data."""
    login_ak = forms.CharField(
        max_length=255,
        label='AK',
        widget=forms.TextInput(attrs={'value':'90UNFNG16GIGP9AX9MV8'}),
        help_text=_("Your account key"))
    login_sk = forms.CharField(
        max_length=255,
        label='SK',
        widget=forms.TextInput(attrs={'value':'ZQM7M9OVDH6WOubuL9zFTWnOlcnrwJdX4tTQGut1'}),
        help_text=_("Your secret key"))
    login_region = forms.CharField(
        max_length=255,
        label='Region',
        widget=forms.TextInput(attrs={'value':'eu-west-2'}),
        help_text=_("Your account region"))