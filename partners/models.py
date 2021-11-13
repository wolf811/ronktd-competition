from django.db import models

# Create your models here.


class Partner(models.Model):
    short_title = models.CharField("Название", max_length=200)
    full_title = models.CharField("Название", max_length=200)
    short_description = models.TextField(
        "Short description",
        max_length=500,
        null=True,
        blank=True,
    )
    logo = models.ImageField(
        "Логотип партнера",
        upload_to="upload/",
        null=True,
        blank=True,
    )
    number = models.SmallIntegerField("Порядок вывода на сайт")
    json_data = models.JSONField("json-data", null=True, blank=True)

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"

    def __str__(self):
        return self.title
