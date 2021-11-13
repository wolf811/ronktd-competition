from django.db import models

# Create your models here.


class Contact(models.Model):
    salutation = models.CharField(
        _("Salutation"), max_length=255, default="", blank=True
    )
    first_name = models.CharField(_("First name"), max_length=255)
    last_name = models.CharField(_("Last name"), max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    organization = models.CharField(_("Organization"), max_length=255, null=True)
    title = models.CharField(_("Title"), max_length=255, default="", blank=True)
    primary_email = models.EmailField(unique=True)
    secondary_email = models.EmailField(default="", blank=True)
    mobile_number = PhoneNumberField(null=True, unique=True)
    secondary_number = PhoneNumberField(null=True)
    department = models.CharField(_("Department"), max_length=255, null=True)
    language = models.CharField(_("Language"), max_length=255, null=True)
    do_not_call = models.BooleanField(default=False)
    address = models.ForeignKey(
        Address,
        related_name="adress_contacts",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    description = models.TextField(blank=True, null=True)
    linked_in_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    twitter_username = models.CharField(max_length=255, null=True)
    created_by = models.ForeignKey(
        Profile, related_name="contact_created_by", on_delete=models.SET_NULL, null=True
    )
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    is_active = models.BooleanField(default=False)
    assigned_to = models.ManyToManyField(Profile, related_name="contact_assigned_users")
    teams = models.ManyToManyField(Teams, related_name="contact_teams")
    org = models.ForeignKey(Org, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ["-created_on"]
