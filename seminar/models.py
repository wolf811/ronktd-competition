from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models.signals import post_save  # post_delete
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from stdimage import StdImageField

# Create your models here.


class Seminar(models.Model):
    """docstring: edit me"""

    publish_on_main_page = models.BooleanField(default=False)
    title = models.CharField(max_length=500)
    logo = models.FileField(
        null=True,
        blank=True,
        upload_to="logotypes/",
    )
    sub_title = models.CharField(max_length=100, default="Семинар")
    sub_title_declension = models.CharField(max_length=100, default="Семинара")
    text_description = models.TextField(null=True, blank=True)
    begin_at = models.DateTimeField()
    phone = PhoneNumberField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    programm = models.FileField(
        null=True,
        blank=True,
        upload_to="upload/",
    )
    json_data = models.JSONField("json-data", null=True, blank=True)

    def __str__(self):
        begin_date = self.begin_at.strftime("%d.%m.%Y")
        return f"{self.sub_title} {self.title} ({begin_date})"

    def generate_promocodes(self):
        pass

    def send_promocodes_to_acsnk(self):
        pass


class SDescription(models.Model):
    """docstring: edit me"""

    seminar = models.ForeignKey(
        Seminar,
        on_delete=models.CASCADE,
        limit_choices_to={"publish_on_main_page": True},
        related_name="descriptions",
    )
    title = models.CharField(max_length=200)
    plain_html = models.TextField(null=True, blank=True)
    formatted_html = RichTextUploadingField(null=True, blank=True)
    stream_link = models.TextField(null=True, blank=True)
    embed_code = models.TextField(null=True, blank=True)
    number = models.PositiveSmallIntegerField(default=0)
    json_data = models.JSONField("json-data", null=True, blank=True)

    class Meta:
        verbose_name = "Description"

    def __str__(self):
        return f"Description {self.pk} for {self.seminar.title}"


class SBanner(models.Model):
    """docstring: edit me"""

    seminar = models.ForeignKey(
        Seminar,
        on_delete=models.CASCADE,
        # limit_choices_to={"publish_on_main_page": True},
        related_name="banners",
    )

    title = models.CharField("Название", default="Слайдер", max_length=50)

    image = StdImageField(
        "Фон баннера",
        upload_to="backgrounds/",
        variations={
            "thumbnail": {"width": 200, "height": 100, "crop": True},
            "large": {"width": 1920, "height": 1080, "crop": True},
        },
    )

    activated = models.BooleanField(
        "Активировать",
        null=True,
        default=False,
    )
    short_description = models.TextField(
        "short description",
        max_length=500,
        null=True,
        blank=True,
    )
    number = models.SmallIntegerField(
        verbose_name="ordering",
        default=0,
    )
    json_data = models.JSONField("json-data", null=True, blank=True)

    class Meta:
        verbose_name = "Banner"

    def __str__(self):
        return self.title

    def activate(self):
        """docstring: edit me"""
        if not self.activated:
            self.activated = True
            self.save()


class SSpeaker(models.Model):
    """docstring: edit me"""

    seminar = models.ForeignKey(
        Seminar,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="speakers",
    )
    fio = models.CharField(max_length=200)
    bio = models.TextField(null=True, blank=True)
    photo = StdImageField(
        "Speaker photo",
        upload_to="speakers_photos/",
        variations={
            "thumbnail": {"width": 80, "height": 80, "crop": True},
            "large": {"width": 300, "height": 300, "crop": True},
            "small": {"width": 100, "height": 100, "crop": True},
        },
    )
    number = models.PositiveSmallIntegerField(default=0)
    json_data = models.JSONField(
        "json-data",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Speaker"

    def __str__(self):
        return f"speaker {self.number} (id {self.pk}: {self.fio})"


class STheme(models.Model):
    """docstring: edit me"""

    speaker = models.ForeignKey(
        SSpeaker,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="themes",
    )
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    speak_time_start = models.DateTimeField()
    speak_time_end = models.DateTimeField(null=True, blank=True)
    number = models.PositiveSmallIntegerField(default=0)
    json_data = models.JSONField(
        "json-data",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Theme"
        verbose_name_plural = "Themes"

    def __str__(self):
        return f"{self.title}"


class SDocument(models.Model):
    """docstring: edit me"""

    document = models.ForeignKey(
        "publications.Document",
        on_delete=models.CASCADE,
    )
    theme = models.ForeignKey(
        STheme,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="documents",
    )
    number = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = "Document"

    def __str__(self):
        return f"doc {self.number} (id: {self.pk}) for {self.theme}"


class SParticipant(models.Model):
    """docstring: edit me"""

    fio = models.CharField(max_length=100)
    phone = PhoneNumberField(null=True)
    email = models.EmailField(unique=True)
    org = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    pdn_accepted = models.BooleanField(default=False)
    subscribe_accepted = models.BooleanField(default=False)
    json_data = models.JSONField("json-data", null=True, blank=True)

    class Meta:
        verbose_name = "Participant"

    def __str__(self):
        return f"participant {self.pk}: {self.fio}"


class SPartner(models.Model):
    """docstring: edit me"""

    logo = models.ImageField(
        upload_to="logotypes/",
        blank=True,
    )
    company = models.CharField(
        "Partner title",
        max_length=150,
    )
    seminar = models.ForeignKey(
        Seminar,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    total_promocodes = models.PositiveIntegerField(default=0)
    activated_promocodes = models.PositiveIntegerField(default=0)
    super_status = models.BooleanField(default=False)
    json_data = models.JSONField(
        "json-data",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Partner"
        verbose_name_plural = "Partners"

    def __str__(self):
        return f"logo {self.company}"


class SPromoCode(models.Model):
    """docstring: edit me"""

    code = models.CharField(max_length=50)
    seminar = models.ForeignKey(
        Seminar,
        on_delete=models.CASCADE,
    )
    participant = models.ForeignKey(
        SParticipant,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    promo_partner = models.ForeignKey(
        SPartner,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    activated = models.BooleanField(default=False)
    json_data = models.JSONField(
        "json-data",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Promocode"

    def __str__(self):
        return f"code {self.pk}: {self.code}"


class SSubscriber(models.Model):
    """docstring: edit me"""

    seminar = models.ForeignKey(
        Seminar,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    fio = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    email = models.EmailField()
    json_data = models.JSONField(
        "json-data",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Subscriber"


# @receiver(post_save, sender=EdoUser)
@receiver(post_save, sender=Seminar)
def deactivate_other_published_seminars(sender, instance, created, **kwargs):
    seminar = instance
    if seminar.publish_on_main_page == True:
        for sem in Seminar.objects.filter(publish_on_main_page=True).exclude(
            pk=seminar.pk
        ):
            if sem.publish_on_main_page:
                sem.publish_on_main_page = False
                sem.save()
