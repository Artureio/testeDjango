from django.db import models

from stdimage import StdImageField
# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
    criado = models.DateTimeField('Data de Criação', auto_now_add=True)
    modificado = models.DateTimeField('Data de Atualização', auto_now_add=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Noticia(Base):
    titulo = models.CharField('Título:', max_length=100)
    corpo = models.TextField('Corpo da Notícia', max_length=9999)
    thumbnail = StdImageField('Thumbnail', upload_to='noticias', variations={'thumb': (640,400)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable= False)

    def __str__(self):
        return self.titulo

def noticia_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)

signals.pre_save.connect(noticia_pre_save, sender= Noticia)
