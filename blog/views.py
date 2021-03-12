from django.db.transaction import commit
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.template import loader

from .forms import ContatoForm, NoticiaModelForm
from .models import Noticia
from django.core.paginator import Paginator, EmptyPage


def index(request):
    # PAGINAÇÃO
    noticias = Noticia.objects.all()
    p = Paginator(noticias, 8)
    page_num = request.GET.get('page',1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print('numero de páginas')
    print(p.num_pages)
    # Mostrar uruário logado
    if str(request.user) != 'AnonymousUser':
        logado = f'Bem vindo {request.user}'
        status = False
    else:
        logado = f'Não logado.'
        status = True

    # Confirmação de notícia salva
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
        'noticias': page,
        'logado': logado,
        'status': status,
        'form':form
    }
    return render(request, 'index.html', context)


def vernoticia(request, pk):
    # Mostrar uruário logado
    if str(request.user) != 'AnonymousUser':
        logado = f'Bem vindo {request.user}'
        status = False
    else:
        logado = f'Não logado.'
        status = True

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


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)