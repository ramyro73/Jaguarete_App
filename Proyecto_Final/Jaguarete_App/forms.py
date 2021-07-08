from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import Producto

class CustomUserCreationForm(UserCreationForm):
       pass


class ProductoForm(forms.ModelForm):



       class Meta:
              model=Producto
              fields = '__all__'