from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.


class PartnerStatus(models.Model):
    """docstring: tags"""

    name = models.CharField(
        "status name",
        max_length=100,
    )

    def __str__(self):
        return f"{self.name}"


class Partner(models.Model):
    short_title = models.CharField("Название", max_length=200)
    full_title = models.CharField("Название", max_length=200)
    short_description = models.TextField(
        "Short description",
        max_length=500,
        null=True,
        blank=True,
    )
    full_description = RichTextUploadingField(
        verbose_name="Текст",
        config_name="default",
        extra_plugins=["youtube"],
        external_plugin_resources=[
            (
                "youtube",
                "plugins/youtube/",
                "plugin.js",
            )
        ],
    )

    logo = models.ImageField(
        "Логотип партнера",
        upload_to="upload/",
        null=True,
        blank=True,
    )
    status = models.ForeignKey(
        PartnerStatus,
        verbose_name="status",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    number = models.SmallIntegerField("Порядок вывода на сайт")
    json_data = models.JSONField("json-data", null=True, blank=True)

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"

    def __str__(self):
        return self.short_title
