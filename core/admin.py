from django.contrib import admin

from .models import Noticia

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'criado', 'slug','modificado', 'thumbnail', 'corpo','ativo')

