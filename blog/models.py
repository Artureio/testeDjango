from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from stdimage import StdImageField
from PIL import Image
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
    CATEG = (
        ('games','games'),
        ('tech','tech'),
        ('meme','meme'),
        ('crypyo','crypto'),
        ('outros','outros')
    )
    titulo = models.CharField('Título:', max_length=100)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    corpo = models.TextField('Corpo da Notícia', max_length=9999)
    thumbnail = StdImageField('Thumbnail', upload_to='noticias')
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)
    categoria = models.CharField('Categoria', choices=CATEG,default='outros' ,max_length=20, blank=False, null=False)

    def __str__(self):
        return self.titulo

    def save(self):
        super().save()
        img = Image.open(self.thumbnail.path)
        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.thumbnail.path)

    def get_absolute_url(self):
        return reverse('vernoticia', kwargs={'pk': self.pk})
