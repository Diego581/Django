from django import forms
from .models import  Comment, Post
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

# Formulario de login 
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

# Formulario de registro 
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
        
class Comments(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

        widget = {
            'comment': forms.TextInput(attrs={"class": "form-control"}),
        }

class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widget = {
            'userId': forms.CharField(widget= forms.TextInput(attrs={"class": "form-control","id":"some_id"})),
            'title':  forms.TextInput(attrs={"class": "form-control"}),
            'info': forms.TextInput(attrs={"class": "form-control"}),
        }