from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.models import Perfil

class RegistroUsuario(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EditarUsuarioForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['imagem']