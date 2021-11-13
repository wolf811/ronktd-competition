import os

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import FileExtensionValidator
from django.db import models
# from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone
from stdimage.models import StdImageField

# Create your models here.


class Tag(models.Model):

    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Category(models.Model):
    """category model class"""

    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class ContentMixin(models.Model):
    """base class for Post, Article and Documents"""

    title = models.CharField(u"Название", max_length=200)
    url_code = models.CharField(
        u"Код ссылки", max_length=30, blank=True, default="НЕ УКАЗАН"
    )
    short_description = models.CharField(
        u"Краткое описание", max_length=200, blank=True
    )
    tags = models.ManyToManyField(Tag, verbose_name="Тэги", blank=True)
    published_date = models.DateTimeField(u"Дата публикации", blank=True, null=True)
    created_date = models.DateTimeField(u"Дата создания", default=timezone.now)
    text = RichTextUploadingField(
        verbose_name="Текст",
        config_name="default",
        extra_plugins=["youtube"],
        external_plugin_resources=[
            (
                "youtube",
                "plugins/youtube/",
                # '/static_root/ckeditor/ckeditor/plugins/youtube/',
                # static/ckeditor_plugins/youtube/plugin.js
                "plugin.js",
            )
        ],
    )
    author = models.ForeignKey(
        "auth.User", verbose_name="Автор", on_delete=models.CASCADE
    )
    publish_on_main_page = models.BooleanField(
        verbose_name="Опубликовать на главной", default=False
    )

    class Meta:
        abstract = True
