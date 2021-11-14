from django.db import models

# Create your models here.


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
