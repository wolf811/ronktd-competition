from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.
class EventMixin(models.Model):
    """base class content"""

    title = models.CharField("Название", max_length=200)
    short_description = models.CharField(
        "Краткое описание",
        max_length=200,
        blank=True,
        null=True,
    )
    full_description = RichTextUploadingField(
        verbose_name="Текст",
        null=True,
        blank=True,
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
    number = models.PositiveIntegerField("Ordering", null=True, blank=True)
    json_data = models.JSONField(
        null=True,
        blank=True,
        default=None,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Event(EventMixin):
    period_start = models.DateField()
    period_end = models.DateField()

    logo = models.ImageField(
        upload_to="logos",
        null=True,
        blank=True,
    )
    phone = models.CharField(max_length=100, null=True, blank=True, default="---")
    email = models.EmailField(null=True, blank=True, default="info@naks.ru")

    active_now = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"


class Nomination(EventMixin):
    event = models.ForeignKey(
        Event,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = "Номинация"
        verbose_name_plural = "Номинации"


class Tag(models.Model):
    """docstring: tags"""

    name = models.CharField(max_length=64)
    json_data = models.JSONField("json-data", null=True, blank=True)

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class EventParticipant(models.Model):
    """
    fio = forms.CharField(max_length=150)
    phone = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    comment = forms.CharField(required=False)
    pdn_accept = forms.BooleanField()
    captcha = CaptchaField()
    """

    fio = models.CharField(max_length=300, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    pdn_accept = models.BooleanField(default=True)

    class Meta:
        verbose_name = "EventParticipant"
        verbose_name_plural = "EventParticipants"

    def __str__(self):
        if self.fio:
            return self.fio
        return f"Participant {self.pk}"
