
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group, Permission, AbstractUser, BaseUserManager
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

from embed_video.fields import EmbedVideoField

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Custom fields
class IntegerRangeField(models.IntegerField):
    """
    """

    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


# Create your models here.
class Video(models.Model):
    """
    """

    titulo = models.CharField(verbose_name=_("Título"), max_length=100)
    video = EmbedVideoField(_("Video Url"))
    content_type = models.ForeignKey(ContentType, verbose_name=_("Tipo"), on_delete=models.CASCADE, null=True, related_name="content_type_video")
    object_id = models.PositiveIntegerField(default=1, verbose_name=_("Objeto"))
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")


    def __unicode__(self):
        return self.titulo

    def __str__(self):
        return self.titulo


class Imagen(models.Model):
    """
    """

    titulo = models.CharField(verbose_name=_("Título"), max_length=100)
    imagen = models.ImageField(_("Imagen"), upload_to="photos", default='photos/default.jpg')
    content_type = models.ForeignKey(ContentType, verbose_name=_("Tipo"), on_delete=models.CASCADE, null=True, related_name="content_type_image")
    object_id = models.PositiveIntegerField(default=1, verbose_name=_("Objeto"))
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _("Imagen")
        verbose_name_plural = _("Imagenes")


    def __unicode__(self):
        return str(self.imagen)

    def __str__(self):
        return str(self.imagen)


class Entidad(models.Model):
    """
    """

    ESTADO = (("Activo", "Activo"), ("Inactivo", "Inactivo"))
    estado = models.CharField(verbose_name=_("Estado"), max_length=20, choices=ESTADO, default=1)
    titulo = models.CharField(verbose_name=_("Título"), max_length=100)#, unique=True)
    en_titulo = models.CharField(verbose_name=_("En Título"), max_length=100, default='', blank=True)
    subtitulo = models.CharField(verbose_name=_("Subtítulo"), max_length=100, blank=True)
    en_subtitulo = models.CharField(verbose_name=_("En Subtítulo"), max_length=100, default='', blank=True)
    informacion = RichTextField(config_name='full', verbose_name=_("Información"), blank=True)
    en_informacion = RichTextField(config_name='full',verbose_name=_("En Información"), default='', blank=True)
    prioridad = models.IntegerField(verbose_name=_("Prioridad"), default=0, blank=True)
    created_date = models.DateTimeField(verbose_name=_("Fecha Creación"), auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name=_("Fecha Actualización"), auto_now=True)

    class Meta:
        abstract = True


class Categoria(Entidad):
    """
    """

    color = models.CharField(verbose_name=_("Color"), max_length=7, null=True, blank=True)
    images = GenericRelation(Imagen)
    videos = GenericRelation(Video)
    categoria_padre = models.ForeignKey('self', verbose_name=_("Categoría Padre"), related_name='parent_category', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Categoría")
        verbose_name_plural = _("Categorías")


    def __unicode__(self):
        return self.titulo

    def __str__(self):
        return self.titulo


class Lugar(Entidad):
    """
    """

    categoria = models.ForeignKey(Categoria, verbose_name=_("Categoria"), on_delete=models.CASCADE, related_name="place_category", null=True)
    puntuacion = IntegerRangeField(verbose_name=_("Puntuación"), null=True, blank=True, min_value=0, max_value=10)
    destacado = models.BooleanField(default=False, verbose_name=_("Destacado"), blank=True)
    images = GenericRelation(Imagen)
    videos = GenericRelation(Video)
    servicios = models.TextField(verbose_name=_("Servicios"), default='', blank=True)
    en_servicios = models.TextField(verbose_name=_("En Servicios"), default='', blank=True)
    latitud = models.CharField(_("Latitud"), max_length=20, null=True, blank=True)
    longitud = models.CharField(_("Longitud"), max_length=20, null=True, blank=True)
    telefono1 = models.CharField(_("Telefono 1"), max_length=20, null=True, blank=True)
    telefono2 = models.CharField(_("Telefono 2"), max_length=20, null=True, blank=True)
    url = models.URLField(_("Pagina Web"), null=True, blank=True)
    reserva = models.URLField(_("Reservar"), null=True, blank=True)
    compra = models.URLField(_("Comprar"), null=True, blank=True)
    vista360 = models.URLField(_("Vista 360"), null=True, blank=True)

    class Meta:
        verbose_name = _("Lugar")
        verbose_name_plural = _("Lugares")


    def __unicode__(self):
        return self.titulo

    def __str__(self):
        return self.titulo


class Publicacion(Entidad):
    """
    """

    TIPO = (("Noticia", "Noticia"), ("Evento", "Evento"))
    tipo = models.CharField(_("Tipo"), max_length=20, choices=TIPO, default=1)
    categoria = models.ForeignKey(Categoria, verbose_name=_("Categoría"), on_delete=models.CASCADE, related_name="publication_category", null=True)
    images = GenericRelation(Imagen)
    videos = GenericRelation(Video)

    class Meta:
        verbose_name = _("Publicacion")
        verbose_name_plural = _("Publicaciones")


    def __unicode__(self):
        return self.titulo

    def __str__(self):
        return self.titulo


class Promo(Entidad):
    """
    """

    images = GenericRelation(Imagen)
    videos = GenericRelation(Video)
    lugar = models.ForeignKey(Lugar, verbose_name=_("Lugar"), on_delete=models.CASCADE, related_name="promo_place", null=True)

    class Meta:
        verbose_name = _("Promo")
        verbose_name_plural = _("Promos")


    def __unicode__(self):
        return self.titulo

    def __str__(self):
        return self.titulo


class Precio(Entidad):
    """
    """

    lugar = models.ForeignKey(Lugar, verbose_name=_("Lugar"), on_delete=models.CASCADE, related_name="price_place", null=True)
    cantidad = models.DecimalField(verbose_name=_("Cantidad"), max_digits=6, decimal_places=2, default=0)

    class Meta:
        verbose_name = _("Precio")
        verbose_name_plural = _("Precios")


    def __unicode__(self):
        return self.titulo

    def __str__(self):
        return self.titulo


class Horario(Entidad):
    """
    """

    lugar = models.ForeignKey(Lugar, verbose_name=_("Lugar"), on_delete=models.CASCADE, related_name="schedule_place", null=True)

    class Meta:
        verbose_name = _("Horario")
        verbose_name_plural = _("Horarios")
        #db_table = 'book'


    def __unicode__(self):
        return self.titulo + ' de ' + str(self.lugar)

    def __str__(self):
        return self.titulo + ' de ' + str(self.lugar)


class PeriodoHorario(models.Model):
    """
    """

    DAYS  = (("Lunes", "Lunes"), ("Martes", "Martes"), ("Miercoles", "Miercoles"), ("Jueves", "Jueves"), ("Viernes", "Viernes"), ("Sábado", "Sábado"), ("Domingo", "Domingo"))
    dia = models.CharField(_("Día"), max_length=9, choices=DAYS, default="Lunes", blank=True)
    inicio = models.TimeField(verbose_name=_('Apertura'))
    fin = models.TimeField(verbose_name=_('Cierre'))
    horario = models.ForeignKey(Horario, verbose_name=_('Horario'), on_delete=models.CASCADE, related_name='schedule_day', blank=True)

    class Meta:
        verbose_name = _("Periodo Horario")
        verbose_name_plural = _("Periodos Horario")

    def __unicode__(self):
        return self.dia + ': ' + str(self.inicio) + ' a ' + str(self.fin)

    def __str__(self):
        return self.dia + ': ' + str(self.inicio) + ' a ' + str(self.fin)




#
