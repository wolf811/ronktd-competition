from django.urls import include, path

import main.views as main

app_name = "main"

urlpatterns = [
    path("", main.index, name="index"),
    path("part_form/", main.participant_form),
    path(
        "about-competition-organizers/",
        main.about_competition_oraganizers,
        name="about-competition-organizers",
    ),  # view not ready
    path(
        "about-structure/",
        main.about_structure,
        name="about-structure",
    ),  # view not ready
    path(
        "about-orgcommitee/",
        main.about_orgcommitee,
        name="about-orgcommitee",
    ),
    path(
        "about-goals/",
        main.about_goals,
        name="about-goals",
    ),
    path(
        "about-docs/",
        main.about_docs,
        name="about-docs",
    ),
    path(
        "about-nominations/",
        main.about_nominations,
        name="about-nominations",
    ),
    path(
        "history-def2021/",
        main.history_def2021,
        name="history-def2021",
    ),
    path(
        "history-def2022/",
        main.history_def2022,
        name="history-def2022",
    ),
    path(
        "stages-centers/",
        main.stages_centers,
        name="stages-centers",
    ),
    path(
        "stages-rules/",
        main.stages_rules,
        name="stages-rules",
    ),
    path(
        "stages-requirements/",
        main.stages_requirements,
        name="stages-requirements",
    ),
    path(
        "final-stage-place/",
        main.final_stage_place,
        name="final-stage-place",
    ),
    path(
        "final-stage-selection/",
        main.final_stage_selection,
        name="final-stage-selection",
    ),
    path(
        "final-stage-requirements/",
        main.final_stage_requirements,
        name="final-stage-requirements",
    ),
    path(
        "final-stage-rules/",
        main.final_stage_rules,
        name="final-stage-rules",
    ),
    path("sponsorship/", main.sponsorship, name="sponsorship"),
    path("users/", include("users.urls", namespace="users")),
    path("news/", main.news, name="news"),
    path("news-detail/", main.news_detail, name="news-detail"),
    path("structure/", main.structure, name="structure"),
    path("stages/", main.stages, name="stages"),
    path("final-stage/", main.final_stage, name="final-stage"),
    path("memb-info/", main.memb_info, name="memb-info"),
    path("gallery/", main.gallery, name="gallery"),
    path("members/", main.members, name="members"),
    path("member-detail/", main.member_detail, name="member-detail"),
    # path("organizers/", main.organizers, name="organizers"),
    path("final-stage-organizers/", main.sponsors, name="final-stage-organizers"),
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
