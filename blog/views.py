from django.shortcuts import get_object_or_404, render
from .models import Noticia
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



class NoticiaListView(ListView):
    model = Noticia
    template_name = 'index.html'
    context_object_name = 'noticias'
    ordering = ['-criado']
    paginate_by = 12



class NoticiaUsuarioLista(ListView):
    model = Noticia
    template_name = 'noticia-usuario.html'
    context_object_name = 'noticias'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Noticia.objects.filter(autor=user).order_by('-criado')


def CategoriaView(request,categ):
    categoria_posts = Noticia.objects.filter(categoria=categ)
    context={
        'categ':categ,
        'categoria_posts':categoria_posts
    }
    return render(request,'noticia-categoria.html',context)



class NoticiaDetalhadaView(DetailView):
    model = Noticia
    template_name = 'vernoticia.html'


class NoticiaPostarView(LoginRequiredMixin, CreateView):
    model = Noticia
    template_name = 'postar.html'

    fields = ['titulo', 'categoria', 'corpo', 'thumbnail']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class NoticiaAtualizarView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Noticia
    template_name = 'postar.html'

    fields = ['titulo', 'corpo','categoria' ,'thumbnail']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False


class NoticiaDeletarView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Noticia
    success_url = '/'
    template_name = 'deletar.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False
