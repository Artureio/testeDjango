from django.db.transaction import commit
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContatoForm, NoticiaModelForm
from .models import Noticia

def index(request):
    context = {
        'noticias': Noticia.objects.all()
    }
    return render(request, 'index.html', context)


def login(request):
    return render(request, 'login.html')


def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()

            messages.success(request, 'E-mail enviado com sucesso! Entraremos em contato em breve!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar E-mail!')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def noticia(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = NoticiaModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()

                messages.success(request, 'Notícia salva com sucesso!')
                form = NoticiaModelForm()
            else:
                messages.error(request, 'Erro ao salvar notícia!')
        else:
            form = NoticiaModelForm()

        context = {
            'form': form
        }
        return render(request, 'noticia.html', context)
    else:
        return redirect(to='../painel/')
