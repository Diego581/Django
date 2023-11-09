from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from .models import Comment, Post

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label=_("Username"))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}), label=_("Password"))

class Comments(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

        widgets = {
            'comment': forms.TextInput(attrs={"class": "form-control"}),
        }

class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'userId': forms.TextInput(attrs={"class": "form-control", "id": "some_id"}),
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'info': forms.TextInput(attrs={"class": "form-control"}),
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
