from django.contrib import admin

from publications.models import (
    Article,
    Banner,
    Category,
    Document,
    DocumentCategory,
    Post,
    PostPhoto,
)

# Register your models here.

imported_classes = [
    Article,
    Banner,
    Category,
    Document,
    DocumentCategory,
    PostPhoto,
]

for cls_ in imported_classes:
    admin.site.register(cls_)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "__str__"]
    list_display_links = ["id", "__str__"]
