from django.contrib import admin

from partners.models import *

# Register your models here.


classes = [PartnerStatus]

for cls_ in classes:
    admin.site.register(cls_)


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ["id", "__str__", "number"]
    list_display_links = ["id", "__str__"]
