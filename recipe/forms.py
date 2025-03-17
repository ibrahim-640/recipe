
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Recipe

class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title','ingredients','instructions']
        widgets = {
            'description': forms.Textarea(attrs={'rows':'3',"placeholder":" enter your description"}),
        }

