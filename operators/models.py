from django.db import models

# Create your models here.


class Company(models.Model):
    """docstring"""

    short_title = models.CharField("Company short title", max_length=200)
    full_title = models.CharField("Company full title", max_length=250)
    inn_number = models.CharField(
        "Inn number",
        max_length=12,
        null=True,
        blank=True,
    )
    address = models.CharField(
        "CompanyAddress",
        max_length=200,
        null=True,
        blank=True,
    )
    logo = models.ImageField(
        "Логотип партнера",
        upload_to="upload/",
        null=True,
        blank=True,
    )
    json_data = models.JSONField(
        "json-data",
        null=True,
        blank=True,
        default=dict,
    )

    class Meta:
        abstract = True


class Operator(Company):
    class Meta:
        verbose_name = "Оператор"
        verbose_name_plural = "Операторы"
