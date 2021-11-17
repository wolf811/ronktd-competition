from django.contrib import admin

from common.models import Event, Nomination, Tag

# Register your models here.
for cls_ in [Tag, Nomination]:
    admin.site.register(cls_)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["id", "__str__"]
    list_display_links = ["id", "__str__"]
