from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)
    terms = forms.BooleanField(
        required=True,
        label="I agree to the terms and conditions"
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # Do not include 'terms' here

    def clean_terms(self):
        terms = self.cleaned_data.get('terms')
        if not terms:
            raise forms.ValidationError("You must agree to the terms and conditions to register.")
        return terms
