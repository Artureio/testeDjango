from django import forms
from django.core.mail.message import EmailMessage

from .models import Noticia

class NoticiaModelForm(forms.ModelForm):  # faz conexão com banco de dados

    class Meta:
        model = Noticia
        fields = ['titulo','categoria','corpo', 'thumbnail']
