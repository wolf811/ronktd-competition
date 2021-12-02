from django.contrib import admin
from django.utils.html import format_html
from django_object_actions import DjangoObjectActions

from seminar.models import (SBanner, SDescription, SDocument, Seminar,
                            SParticipant, SPartner, SPromoCode, SSpeaker,
                            SSubscriber, STheme)

# Register your models here.


def get_picture_preview(obj):
    if (
        obj.pk
    ):  # if object has already been saved and has a primary key, show picture preview
        if hasattr(obj, "image"):
            img = obj.image
        if hasattr(obj, "photo"):
            img = obj.photo
        if hasattr(obj, "title"):
            titl = obj.title
        if hasattr(obj, "fio"):
            titl = obj.fio
        return format_html(
            """<a href="{src}" target="_blank">
        <img src="{src}" alt="{title}" style="max-width: 200px; max-height: 200px;" />
        </a>""".format(
                src=img.url,
                title=titl,
            )
        )
    return "(После загрузки фотографии здесь будет ее миниатюра)"


get_picture_preview.allow_tags = True
get_picture_preview.short_description = "Предварительный просмотр:"


def get_url(obj):
    # Надо обязательно изменить на боевом сервере адрес ссылки
    if obj.pk:
        return format_html(
            '<a href="{}" target="_blank">http://127.0.0.0{}</a>'.format(
                obj.get_absolute_url(), obj.get_absolute_url()
            )
        )


get_url.allow_tags = True
get_url.short_description = "Ссылка на страницу"


models = [
    # SBanner,
    # SDescription,
    # STheme,
    # SSpeaker,
    # SDocument,
    SParticipant,
    # SPartner,
    # SPromoCode,
    SSubscriber,
]

for model_ in models:
    admin.site.register(model_)


@admin.register(SPromoCode)
class SPromoCodeAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "promo_partner",
        "participant",
        "activated",
    ]


@admin.register(SDocument)
class SDocumentAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "seminar",
        "theme",
    ]


@admin.register(STheme)
class SThemeAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "speaker",
        "id",
        "number",
    ]


@admin.register(Seminar)
class SeminarAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "__str__",
        "publish_on_main_page",
    ]
    list_display_links = [
        "id",
        "__str__",
    ]


@admin.register(SSpeaker)
class SSpeakerAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "seminar",
        get_picture_preview,
    ]


@admin.register(SDescription)
class SDescriptionAdmin(admin.ModelAdmin):
    list_display = ["__str__", "number"]


@admin.register(SBanner)
class SBannerAdmin(admin.ModelAdmin):
    list_display = ["title", get_picture_preview, "activated"]


@admin.register(SPartner)
class SPartnerAdmin(DjangoObjectActions, admin.ModelAdmin):
    def create_promocodes(self, request, obj):
        print(f"creating {obj.total_promocodes} promocodes...")

    def batch_create_promocodes(modeladmin, request, queryset):
        for obj in queryset:
            obj.generate_promocodes()
        print("<-DONE CREATING PROMOCODES->")

    create_promocodes.label = "Create promocodes"
    create_promocodes.short_description = "Creating promocodes with given number"

    change_actions = ("create_promocodes",)
    changelist_actions = ("batch_create_promocodes",)

    list_display = [
        "__str__",
        "seminar",
        "total_promocodes",
        "activated_promocodes",
    ]
