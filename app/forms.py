from django import forms
from .models import User, Comment
from django.utils.translation import gettext as _

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            "username" : forms.TextInput(attrs={"class": "form-control"}),
            "password" : forms.TextInput(attrs={"class": "form-control"})
        }

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

        widgets = {
            "username" : forms.TextInput(attrs={"class": "form-control"}),
            "user_email" : forms.TextInput(attrs={"class": "form-control"}),
            "password" : forms.TextInput(attrs={"class": "form-control"})
        }
        
class Comments(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

        widget = {
            'comment': forms.TextInput(attrs={"class": "form-control"}),
        }