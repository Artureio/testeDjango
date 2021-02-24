from django import forms
from django.core.mail.message import EmailMessage

from .models import Noticia


class ContatoForm(forms.Form):  # nao faz contato com banco de dados
    nome = forms.CharField(label='Nome', max_length='100')
    email = forms.EmailField(label='E-Mail', max_length='100')
    assunto = forms.CharField(label='Assunto', max_length='100')
    texto = forms.CharField(label='Texto', widget=forms.Textarea)

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        texto = self.cleaned_data['texto']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nTexto: {texto}'

        mail = EmailMessage(
            subject='Email enviado pelo sistema Awarded',
            body=conteudo,
            from_email='artureio2@hotmail.com',  # usuário que receberá o email
            to=['artureio2@hotmail.com'],  # lista de usuarios que receberão o email(1 ou mais)
            headers={'Reply-To': email}  # usuario que receberá a resposta (mesmo email que preencheu no form)
        )
        mail.send()


class NoticiaModelForm(forms.ModelForm):  # faz conexão com banco de dados
    class Meta:
        model = Noticia
        fields = ['titulo', 'corpo', 'thumbnail']
