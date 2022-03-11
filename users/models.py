import requests
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save  # post_delete
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

# Create your models here.


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    # is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def can_see_miracles(self):
        if self.userprofile.can_see_miracles:
            return True
        return False


"""
class EdoUser(CustomUser):
    identifier = models.CharField(_("identifier"), max_length=20, unique=True)
    USERNAME_FIELD = "identifier"
    objects = EdoUserManager()
"""


class UserProfile(models.Model):
    STATUS_CHOICES = (
        ("UL", "Юридическое лицо"),
        ("FL", "Физическое лицо"),
    )

    USER_TYPE_CHOICES = (
        ("NA", "Naks Admin"),
        ("CNT", "Center"),
        ("PRT", "Participant"),
        ("PRNTR", "Partner"),
    )

    status = models.CharField(
        "Юридический статус",
        choices=STATUS_CHOICES,
        default="UL",
        max_length=2,
    )

    user_type = models.CharField(
        "Тип пользователя",
        choices=USER_TYPE_CHOICES,
        default="CNT",
        max_length=10,
    )
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="userprofile"
    )
    edo_token = models.CharField(
        "Основной токен ЭДО", max_length=50, blank=True, null=True
    )
    edo_refresh_token = models.CharField(
        "Токен обновления", max_length=50, blank=True, null=True
    )
    edo_token_created = models.DateTimeField(
        "Время создания основного токена", null=True, blank=True
    )
    can_see_miracles = models.BooleanField(
        "Видит тайное",
        null=True,
        default=False,
    )
    json_data = models.JSONField("Json", null=True, blank=True)

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"

    def __str__(self):
        return "Profile of {}".format(self.user)

    def save(self, *args, **kwargs):
        if self.edo_token and not self.edo_token_created:
            self.edo_token_created = timezone.now()
        # super(EdoUser, self).save(*args, **kwargs)
        super().save(*args, **kwargs)


# @receiver(post_save, sender=EdoUser)
@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()
