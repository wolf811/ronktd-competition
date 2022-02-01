from django.contrib import admin

from common.models import Event, EventParticipant, Nomination, Tag


# Register your models here.
@admin.register(Nomination)
class NominationAdmin(admin.ModelAdmin):
    list_display = ["id", "__str__", "number"]
    list_display_links = ["id", "__str__"]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["id", "__str__", "active_now"]
    list_display_links = ["id", "__str__"]


@admin.register(EventParticipant)
class EventParticipantAdmin(admin.ModelAdmin):
    list_display = ["id", "__str__"]
    list_display_links = ["id", "__str__"]
