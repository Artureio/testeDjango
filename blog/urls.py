from django.urls import path
from .views import NoticiaListView, NoticiaDetalhadaView, NoticiaPostarView, NoticiaAtualizarView, NoticiaDeletarView, \
    NoticiaUsuarioLista, CategoriaView

urlpatterns = [
    path('', NoticiaListView.as_view(), name='index'),
    path('post/<str:username>/', NoticiaUsuarioLista.as_view(), name='noticia-usuario'),
    path('categoria/<str:categ>/', CategoriaView, name='noticia-categoria'),
    path('posts/new/', NoticiaPostarView.as_view(), name='postar'),
    path('posts/<int:pk>/', NoticiaDetalhadaView.as_view(), name='vernoticia'),
    path('post/<int:pk>/atualizar', NoticiaAtualizarView.as_view(), name='atualizar'),
    path('post/<int:pk>/deletar', NoticiaDeletarView.as_view(), name='deletar'),
]
