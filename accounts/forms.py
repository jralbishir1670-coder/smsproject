from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_styles = {
            "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700"
        }
        self.fields['username'].widget = forms.TextInput(attrs={
            **field_styles,
            "type": "text",
            "placeholder": "Enter your username"
        })
        self.fields['email'].widget = forms.EmailInput(attrs={
            **field_styles,
            "type": "email",
            "placeholder": "Enter your email"
        })
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            **field_styles,
            "type": "password",
            "placeholder": "Enter your password"
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            **field_styles,
            "type": "password",
            "placeholder": "Confirm your password"
        })
        

# from django import forms 
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class RegisterForm(UserCreationForm):
#     email = forms.EmailInput(required=True)
    
#     class Meta:
#         model = User
#         fields = ["username", "email", "password1", "password2"]
        