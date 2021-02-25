from django.urls import path
from .views import index, vernoticia, contato, noticia
from core import views

urlpatterns = [
    path('', index, name='index'),
    path('vernoticia/<int:pk>', vernoticia, name='vernoticia'),
    path('contato/', contato, name='contato'),
    path('noticia/', noticia, name='noticia'),

]

handler404 = views.error404
handler500 = views.error500
