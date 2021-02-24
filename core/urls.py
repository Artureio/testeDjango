from django.urls import path
from .views import index, login, contato, noticia

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('contato/', contato, name='contato'),
    path('noticia/', noticia, name='noticia'),
]
