from django.urls import path
from .views import NoticiaListView, NoticiaDetalhadaView, NoticiaPostarView, NoticiaAtualizarView, NoticiaDeletarView

urlpatterns = [
    path('', NoticiaListView.as_view(), name='index'),
    path('post/new/', NoticiaPostarView.as_view(), name='postar'),
    path('post/<int:pk>/', NoticiaDetalhadaView.as_view(), name='vernoticia'),
    path('post/<int:pk>/atualizar', NoticiaAtualizarView.as_view(), name='atualizar'),
    path('post/<int:pk>/deletar', NoticiaDeletarView.as_view(), name='deletar'),
]
