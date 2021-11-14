from django.contrib import admin

from publications.models import (Article, Banner, Category, Document,
                                 DocumentCategory, Post, PostPhoto)

# Register your models here.

imported_classes = [
    Article,
    Banner,
    Category,
    Document,
    DocumentCategory,
    Post,
    PostPhoto,
]

for cls_ in imported_classes:
    admin.site.register(cls_)
