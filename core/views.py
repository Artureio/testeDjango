from django.db.transaction import commit
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.template import loader

from .forms import ContatoForm, NoticiaModelForm
from .models import Noticia



def index(request):
    if str(request.user) != 'AnonymousUser':
        logado = f'Bem vindo {request.user}'
    else:
        logado = f'Usuário não logado.'
    context = {
        'noticias': Noticia.objects.all(),
        'logado': logado,
    }
    return render(request, 'index.html', context)


def vernoticia(request, pk):
    if str(request.user) != 'AnonymousUser':
        logado = f'Bem vindo {request.user}'
    else:
        logado = f'Usuário não logado.'

    #seleciona noticia pelo id
    noticiapk = get_object_or_404(Noticia, id=pk)

    context = {
        'noticia': noticiapk,
        'logado':logado
    }
    return render(request, 'vernoticia.html', context)


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
        logado = f'Bem vindo {request.user}'
    else:
        logado = f'Usuário não logado.'

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
            'form': form,
            'logado': logado
        }
        return render(request, 'noticia.html', context)
    else:
        return redirect(to='../painel/')

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)