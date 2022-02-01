from django.urls import include, path

import main.views as main

app_name = "main"

urlpatterns = [
    path("", main.index, name="index"),
    path("part_form/", main.participant_form),
    path("users/", include("users.urls", namespace="users")),
    path("news/", main.news, name="news"),
    path("news-detail/", main.news_detail, name="news-detail"),
    path("structure/", main.structure, name="structure"),
    path("docs/", main.docs, name="docs"),
    path("stages/", main.stages, name="stages"),
    path("final-stage/", main.final_stage, name="final-stage"),
    path("memb-info/", main.memb_info, name="memb-info"),
    path("gallery/", main.gallery, name="gallery"),
    path("members/", main.members, name="members"),
    path("member-detail/", main.member_detail, name="member-detail"),
    path("organizers/", main.organizers, name="organizers"),
    path("organizer-detail/", main.organizer_detail, name="organizer-detail"),
    path("sponsors/", main.sponsors, name="sponsors"),
    path("sponsor-detail/", main.sponsor_detail, name="sponsor-detail"),
    path("spon-info/", main.spon_info, name="spon-info"),
    path("contacts/", main.contacts, name="contacts"),
    path("authorization/", main.authorization, name="authorization"),
    path("profile/", main.profile, name="profile"),
    # path("details/<slug:pk>/", main.page_detals, name="details"),
    # path("register/", main.register, name="register"),
]
