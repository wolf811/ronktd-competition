from django.urls import path, include
import main.views as main

app_name = "main"

urlpatterns = [
    path("", main.index, name="index"),
    path("news/", main.news, name="news"),
    path("news-detail/", main.news_detail, name="news-detail"),
    path("structure/", main.structure, name="structure"),
    path("docs/", main.docs, name="docs"),
    path("stages/", main.stages, name="stages"),
    path("final-stage/", main.final_stage, name="final-stage"),
    path("members/", main.members, name="members"),
    path("gallery/", main.gallery, name="gallery"),
    path("partners/", main.partners, name="partners"),
    path("contacts/", main.contacts, name="contacts"),
    path("authorization/", main.authorization, name="authorization"),
    # path("register/", main.register, name="register"),
]
