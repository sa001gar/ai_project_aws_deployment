from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text="Enter a valid email address."
    )
    terms = forms.BooleanField(
        required=True,
        label="I agree to the terms and conditions",
        error_messages={"required": "You must agree to the terms and conditions to register."}
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

    def clean_terms(self):
        terms = self.cleaned_data.get('terms')
        if not terms:
            raise forms.ValidationError("You must agree to the terms and conditions to register.")
        return terms
