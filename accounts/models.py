from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

# from users.models import CustomUser

# Create your models here.


class Account(models.Model):

    ACCOUNT_STATUS_CHOICE = (
        ("open", "Open"),
        ("close", "Close"),
    )

    name = models.CharField(
        pgettext_lazy("Name of Account", "Name"),
        max_length=64,
    )
    email = models.EmailField()
    phone = PhoneNumberField(null=True)
    """
    industry = models.CharField(
        _("Industry Type"),
        max_length=255,
        choices=INDCHOICES,
        blank=True,
        null=True,
    )
    """
    billing_address_line = models.CharField(
        _("Address"), max_length=255, blank=True, null=True
    )
    billing_street = models.CharField(
        _("Street"),
        max_length=55,
        blank=True,
        null=True,
    )
    billing_city = models.CharField(
        _("City"),
        max_length=255,
        blank=True,
        null=True,
    )
    billing_postcode = models.CharField(
        _("Post/Zip-code"),
        max_length=64,
        blank=True,
        null=True,
    )
    website = models.URLField(
        _("Website"),
        blank=True,
        null=True,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    created_by = models.ForeignKey(
        "users.CustomUser",
        related_name="account_created_by",
        on_delete=models.SET_NULL,
        null=True,
    )
    created_on = models.DateTimeField(
        _("Created on"),
        auto_now_add=True,
    )
    is_active = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        "common.Tag",
        blank=True,
    )
    status = models.CharField(
        choices=ACCOUNT_STATUS_CHOICE,
        max_length=64,
        default="open",
    )
    """
    lead = models.ForeignKey(
        "leads.Lead", related_name="account_leads", on_delete=models.SET_NULL, null=True
    )
    """
    contact_name = models.CharField(
        pgettext_lazy("Name of Contact", "Contact Name"),
        max_length=120,
    )
    contacts = models.ManyToManyField(
        "contacts.Contact", related_name="account_contacts"
    )
    assigned_to = models.ManyToManyField(
        "users.CustomUser",
        related_name="account_assigned_users",
    )
    """
        ORG FOREIGN KEY ???
    """

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name
