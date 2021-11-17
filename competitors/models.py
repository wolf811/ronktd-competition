from django.db import models


# Create your models here.
class People(models.Model):
    photo = models.ImageField("Фотография", upload_to="uploads/", blank=True)
    name = models.CharField("ФИО", max_length=120, blank=False)
    job = models.CharField("Должность", max_length=120, blank=False)
    experience = models.CharField("Опыт работы", max_length=500, blank=True)
    ordering = models.SmallIntegerField("Ordering", default=0)
    json_data = models.JSONField("json-data", null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name}"


class Staff(People):
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Participant(People):

    winner = models.PositiveSmallIntegerField(default=0)
    nominations = models.ManyToManyField("common.Nomination", blank=True)

    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"
